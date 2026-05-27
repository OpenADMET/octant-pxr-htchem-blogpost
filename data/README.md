# Data

This repository contains the raw data and method documentation associated with
the PXR HTChem blog post.

## Master Workbook

`data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data.xlsx` contains the high-level
values shown in the selected PXR HTChem figures.

Relevant tabs:

- `HTChem Libraries`
- `96-Compound µScale Semi-Pure`

Companion documentation:

- `data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data_README.md`

## DRC point-level data

HTChem library DRC screens:

- `data/raw/drc/htchem-libraries/OPA_PXR-045_55548_processed-data_OCNT-2432456/`
- `data/raw/drc/htchem-libraries/OPA_PXR-046_55547_processed-data_OCNT-0002416/`

96-compound microscale semipure DRC screen:

- `data/raw/drc/microscale-synthesis/OPA_PXR-048_56149_processed-data_96_semipures/`

Pure reference-hit screens:

- `data/raw/drc/reference-hits/OPA_PXR-032_51622_reference_hits/`
- `data/raw/drc/reference-hits/OPA_PXR-036_53138_reference_hits/`

The `stats.tsv` and `drc.csv` files provide the point-level dose-response data
needed for the blog-post figures.

## CAD yield data

CAD yield, yield-source, CAD detection-status, and corrected-pEC50 values are in
`data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data.xlsx`.

## Citation hover index

The numbered source-to-hover-text mapping for blog-post citations is included at:

- `data/raw/citations/citation_hover_index.md`

## Protocol and method details

The CAD-MS method document and PXR activation assay protocol are included for
experimental-method details:

- `data/raw/method-details/Octant_UHPLC-CAD-MS_Method_Details.md`
- `data/raw/protocols/PXR Activation Assay Protocol.md`
