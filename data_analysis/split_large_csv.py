#!/usr/bin/env python3
"""Split a large CSV file into N smaller CSV files (default 4) without loading it all into memory.

Usage (from repo root or inside data_analysis/):
    python split_large_csv.py \
        --input data_analysis/data/Chile_all(1).csv \
        --parts 4 \
        --method contiguous \
        --output-dir data_analysis/data/splits

Methods:
  contiguous (default): first chunk gets the first rows, then next, preserving original ordering in blocks.
  roundrobin: distributes lines one-by-one across output files (keeps overall ordering but interleaves).

Extra options:
  --compress : gzip each output (.csv.gz)
  --prefix   : prefix for output filenames (default derives from input base name)

The script writes a header line to every part file.
"""
from __future__ import annotations
import argparse
import csv
import gzip
import math
import os
import sys
from pathlib import Path

def human(n: int) -> str:
    if n < 1000:
        return str(n)
    for unit in ["K","M","G","T"]:
        n /= 1000.0
        if n < 1000:
            return f"{n:.2f}{unit}"
    return f"{n:.2f}P"

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Split large CSV into smaller parts (memory efficient)")
    p.add_argument("--input", required=True, help="Path to input CSV file")
    p.add_argument("--parts", type=int, default=4, help="Number of parts to create (default 4)")
    p.add_argument("--method", choices=["contiguous","roundrobin"], default="contiguous", help="Splitting strategy")
    p.add_argument("--output-dir", default=None, help="Directory to place output files (default: alongside input)")
    p.add_argument("--prefix", default=None, help="Output filename prefix (default: input base name without extension)")
    p.add_argument("--compress", action="store_true", help="Compress each part with gzip (.gz)")
    return p.parse_args()

def open_writer(path: Path, compress: bool):
    if compress:
        f = gzip.open(path, 'wt', newline='')
    else:
        f = open(path, 'w', newline='')
    return f

def count_data_lines(path: Path) -> int:
    with open(path, 'r', newline='') as f:
        # Skip header
        header = f.readline()
        if not header:
            return 0
        # Count remaining lines efficiently
        return sum(1 for _ in f)

def split_contiguous(in_path: Path, parts: int, out_dir: Path, prefix: str, compress: bool):
    total = count_data_lines(in_path)
    if total == 0:
        print("Input appears empty (no data rows). Nothing to do.")
        return
    base = total // parts
    remainder = total % parts
    sizes = [base + (1 if i < remainder else 0) for i in range(parts)]
    print(f"Total data rows={total} -> part sizes={sizes}")

    # Prepare writers lazily
    writers = []
    files = []
    try:
        # Open input and iterate
        with open(in_path, 'r', newline='') as fin:
            header = fin.readline()
            reader = fin  # iterate raw lines to keep speed; we preserve header only once
            current_part = 0
            written_in_part = 0
            out_name = f"{prefix}_part{current_part+1}.csv" + (".gz" if compress else "")
            out_path = out_dir / out_name
            fout = open_writer(out_path, compress)
            files.append(fout)
            fout.write(header)
            for idx, line in enumerate(reader):
                if written_in_part >= sizes[current_part]:
                    fout.close()
                    current_part += 1
                    if current_part >= parts:
                        print("Warning: more lines than expected; extra lines discarded")
                        break
                    written_in_part = 0
                    out_name = f"{prefix}_part{current_part+1}.csv" + (".gz" if compress else "")
                    out_path = out_dir / out_name
                    fout = open_writer(out_path, compress)
                    files.append(fout)
                    fout.write(header)
                fout.write(line)
                written_in_part += 1
            fout.close()
    finally:
        for f in files:
            if not f.closed:
                f.close()
    print("Done.")


def split_roundrobin(in_path: Path, parts: int, out_dir: Path, prefix: str, compress: bool):
    paths = [out_dir / (f"{prefix}_part{i+1}.csv" + (".gz" if compress else "")) for i in range(parts)]
    files = []
    try:
        for p in paths:
            f = open_writer(p, compress)
            files.append(f)
        with open(in_path, 'r', newline='') as fin:
            header = fin.readline()
            for f in files:
                f.write(header)
            for i, line in enumerate(fin):
                files[i % parts].write(line)
    finally:
        for f in files:
            f.close()
    print("Done. (roundrobin)")


def main():
    args = parse_args()
    in_path = Path(args.input).expanduser().resolve()
    if not in_path.exists():
        print(f"Input not found: {in_path}", file=sys.stderr)
        sys.exit(1)
    parts = args.parts
    if parts < 2:
        print("--parts must be >= 2", file=sys.stderr)
        sys.exit(1)
    out_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else in_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix or in_path.stem.replace(' ', '_').replace('(', '').replace(')', '')

    print(f"Splitting '{in_path.name}' into {parts} parts (method={args.method}, compress={args.compress})")
    print(f"Output dir: {out_dir}")

    if args.method == 'contiguous':
        split_contiguous(in_path, parts, out_dir, prefix, args.compress)
    else:
        split_roundrobin(in_path, parts, out_dir, prefix, args.compress)

if __name__ == "__main__":
    main()
