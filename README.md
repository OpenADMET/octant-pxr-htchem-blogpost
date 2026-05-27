# octant-pxr-htchem-blogpost

Code, raw data, and standalone interactive figures for the blog post:

> Navigating PXR Chemical Space with High-Throughput Chemistry and Standard-Free Quantification

## Blog post

The rendered blog post is published to GitHub Pages via CI on every push to `main`:

```text
https://openadmet.github.io/octant-pxr-htchem-blogpost/
```

The source is [`index.qmd`](index.qmd). The CI workflow (`.github/workflows/render-deploy.yml`) renders it with Quarto and deploys to the `gh-pages` branch.

## Contents

- [Blog post source](index.qmd)
- [Interactive figures: Figures 9A-E](#interactive-figures)
  - [Standalone HTML figure files](figures/interactive/)
- [Static figures: Figures 1-8](#static-figures)
  - [Static blog-post figure image files](figures/static/)
  - [Figure 6 Python-generated validation panels](figures/static/figure-6-python/)
- [Data](#data)
  - [Master raw data workbook and README](data/raw/master/)
  - [DRC point-level data](data/raw/drc/)
  - [HTChem library DRC data](data/raw/drc/htchem-libraries/)
  - [96-compound microscale DRC data](data/raw/drc/microscale-synthesis/)
  - [Reference-hit DRC data](data/raw/drc/reference-hits/)
  - [Citation hover index](data/raw/citations/citation_hover_index.md)
  - [UHPLC-CAD-MS method details](data/raw/method-details/)
  - [UHPLC-CAD-MS method markdown](data/raw/method-details/Octant_UHPLC-CAD-MS_Method_Details.md)
  - [PXR activation assay protocol](<data/raw/protocols/PXR Activation Assay Protocol.md>)
- [Rebuilding figures](#rebuilding-figures)
  - [Interactive figure builder](scripts/build_interactive_figures.py)
  - [Figure 6 static-panel builder](scripts/build_figure_6_validation_panels.py)

## Interactive figures

The interactive blog-post figures are Figures 9A-E. They are self-contained HTML files in `figures/interactive/`.
They embed Plotly, figure data, molecule images, and hover-card assets, so they
can be served directly by GitHub Pages or embedded in an external blog post.

The interactive figures are also embedded in the blog post, and are individually accessible at:

```text
https://openadmet.github.io/octant-pxr-htchem-blogpost/figures/interactive/<figure-file>.html
```

Current exported interactive figures:

- Figure 9A: `Figure 9A - Beeswarm.html`
- Figure 9B: `Figure 9B - OCNT-2432456 Library.html`
- Figure 9C: `Figure 9C - OCNT-0002416 Library.html`
- Figure 9D: `Figure 9D - OCNT-2432456 Priority Rank.html`
- Figure 9E: `Figure 9E - OCNT-0002416 Priority Rank.html`

## Static figures

Static blog-post figure files are under `figures/static/`.

- `figures/static/` contains the final static/non-interactive Figure 1-8 PNG and GIF files prepared for blog-post upload. Figure 2 is represented by two GIF files.
- `figures/static/figure-6-python/` contains the Python-generated Figure 6 CAD-correction validation panels as PNG and SVG files, plus a generated panel-summary CSV with sample counts and MAE values.

## Data

Data and method documentation are under `data/raw/`.

- `data/raw/master/` contains `PXR_CAD_Blog_Post_Master_Raw_Data.xlsx` and its README. The workbook contains the displayed high-level values such as uncorrected pEC50, adjusted pEC50, CAD yield, yield source, CAD detection status, and SMILES.
- `data/raw/drc/` contains PXR DRC point-level and summary tables used for hover-card dose-response context, including the two HTChem library screens, the 96-compound microscale semipure screen, and the pure reference-hit screens.
- `data/raw/citations/` contains the numbered source-to-hover-text mapping for the blog-post citations.
- `data/raw/method-details/` contains `Octant_UHPLC-CAD-MS_Method_Details.md` for UHPLC-CAD-MS method details.
- `data/raw/protocols/` contains `PXR Activation Assay Protocol.md` for the PXR activation assay protocol.

## Rebuilding figures

The blog-post figures can be regenerated from the data and scripts in this
repository. The interactive-figure builder recreates the standalone HTML files
from the master workbook and DRC tables, and checks key displayed values against
the master workbook during the build.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/build_interactive_figures.py
```

To regenerate the static Figure 6 validation panels:

```bash
python scripts/build_figure_6_validation_panels.py
```

Outputs:

- `figures/interactive/*.html`: deployable GitHub Pages figures.
- `figures/static/*`: static Figure 1-8 PNG and GIF upload assets.
- `figures/static/figure-6-python/*`: Python-generated Figure 6 panel images and summary CSV.
