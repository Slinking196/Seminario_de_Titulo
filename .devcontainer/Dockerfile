FROM mcr.microsoft.com/devcontainers/python:3-3.13-trixie

# Install LaTeX toolchain for thesis compilation (pdflatex, biblatex/biber, latexmk).
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-latex-extra \
        texlive-fonts-recommended \
        texlive-lang-spanish \
        texlive-science \
        texlive-plain-generic \
        texlive-bibtex-extra \
        biber \
        latexmk \
        make \
        ghostscript \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
