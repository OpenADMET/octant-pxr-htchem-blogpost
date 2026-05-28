# Interactive PXR Figures

These standalone HTML files are the interactive blog-post figures, Figures 9A-E.
Each file embeds Plotly, figure data, molecule images, and hover-card assets for
viewing through GitHub Pages or direct download. Displayed high-level values are
drawn from `PXR_CAD_Blog_Post_Master_Raw_Data.xlsx`.

Files:
- Figure 9A: `Figure 9A - Beeswarm.html`
- Figure 9B: `Figure 9B - OCNT-2432456 Library.html`
- Figure 9C: `Figure 9C - OCNT-0002416 Library.html`
- Figure 9D: `Figure 9D - OCNT-2432456 Priority Rank.html`
- Figure 9E: `Figure 9E - OCNT-0002416 Priority Rank.html`

Regeneration scripts:
- `scripts/build_interactive_figures.py`

Primary data source:
- `data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data.xlsx` (`HTChem Libraries` and `96-Compound µScale Semi-Pure` tabs)

Regenerate with:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/build_interactive_figures.py
```
