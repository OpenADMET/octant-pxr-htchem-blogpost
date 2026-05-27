# Figure 6 Python-Generated Validation Panels

These files are generated from `data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data.xlsx`
with:

```bash
python scripts/build_figure_6_validation_panels.py
```

Generated panels:

- `figure-6a-uncorrected-crude-vs-pure-95ci`
- `figure-6b-corrected-crude-vs-pure-95ci`
- `figure-6c-corrected-crude-vs-corrected-semipure-95ci`

The script writes PNG and SVG versions by default and records panel counts and
MAE values in `figure-6-panel-summary.csv`.
