# PXR-CAD Blog Post Master Raw Data: Data Dictionary

This README accompanies `PXR_CAD_Blog_Post_Master_Raw_Data.xlsx`. It describes what is contained in each worksheet, what each column represents, and how the CAD-corrected potency and uncertainty values are calculated.

The workbook contains three worksheets:

| Worksheet | Contents |
| --- | --- |
| `Crude-SP to Pure Correlation` | Validation data comparing crude and semi-pure PXR dose-response results against pure-reference PXR dose-response results. |
| `HTChem Libraries` | PXR DRC and CAD correction data for two HTChem crude follow-up libraries. |
| `96-Compound µScale Semi-Pure` | PXR DRC and CAD correction data for a 96-compound µscale semi-pure synthesis library. |

## Key Concepts

### Compound and Batch IDs

Compounds are identified by a normalized root identifier in the form `OCNT-#######`. Batch suffixes indicate the material form used in an experiment. In this dataset, `ZZ` generally denotes a crude batch, `TL` denotes a semi-pure batch, and `AA`/`AQ` generally denote a pure-reference batch.

### Screening Values

`EC50` values are reported in micromolar (`µM`). `pEC50` values are log-scale potency values calculated from EC50:

```text
pEC50 = -log10(EC50_µM * 10^-6)
```

Higher pEC50 values indicate higher apparent potency. `Emax normalized` values are normalized to the positive control. `Emax raw` values are the corresponding raw assay-response estimates.

### CAD Values

CAD peak area is reported in `pA*min`. The workbook uses the CAD peak area to estimate the amount of product present on-column:

```text
Actual mass-on-column (ng) = 12.5 * CAD peak area (pA*min)
Product yield (%) = actual mass-on-column / theoretical mass-on-column * 100
Correction factor = product yield (%) / 100
Corrected EC50 (µM) = measured EC50 (µM) * correction factor
Corrected pEC50 = -log10(corrected EC50_µM * 10^-6)
```

For the HTChem library worksheet, `Not sufficiently synthesized` in the `CAD Yield/Volatility Note` column indicates a nonzero crude CAD peak area below the lower limit of quantification (`0 < Crude Peak Area (pA*min) < 1.0`). In those rows, the `Crude Peak Area (pA*min)` cell contains the qualitative value `Below LLOQ` rather than a numeric peak area. Rows designated as `True 0% Yield / No Synthesis` remain distinct; their peak-area cells contain `Undetected`. Rows with numeric crude CAD peak areas at or above 1.0 pA*min are not labeled `Not sufficiently synthesized`.

Product yield is not capped at 100%. Therefore, yields above 100% produce correction factors greater than 1 and decrease corrected pEC50 values relative to the measured pEC50. Applying this downward correction for yields above 100% is appropriate in this dataset because CAD-derived yields can exceed 100% for reasons independent of CAD response variability. Crude libraries are synthesized with a stoichiometric excess of both fragments and reagents, and intrinsic dispense-volume variability from the liquid-handling instrument can result in core overdispensing, leading to observed product concentrations above the nominal theoretical maximum and yields above 100%.

### Volatility and CAD Evaporator Temperature

The `Volatility` column indicates whether a compound was treated as non-volatile or semi-volatile for CAD quantification. Non-volatile compounds use 65 °C CAD data. Semi-volatile compounds use 20 °C CAD data. The `EvapT (°C)` columns report which CAD evaporator temperature was used for the yield and correction calculations.

### Missing-Value Conventions

The text `no data` indicates that no fitted screening value is reported for that compound in the relevant screening experiment. The symbol `-` is used for uncertainty terms that are not calculable or not applicable. The current workbook does not use blank cells within the documented data ranges as a missing-value marker.

## Uncertainty Calculations

The workbook includes both ±1 standard error (`±1 SE`) values and approximate 95% confidence interval half-widths (`±95% CI`) on the pEC50/log scale. The 95% CI columns are the values intended for figures with error bars and tables that report pEC50 values as `value ± uncertainty`.

DRC fitting error is taken from the screening analysis export as `ec50_std_error (log10([M]))`. This value is already on the log scale. When multiple pure-reference pEC50 values are averaged, the pure-reference uncertainty is calculated as:

```text
Pure pEC50 ±1 SE = sqrt(sum(SE_i^2)) / n
```

CAD peak-area measurement uncertainty is modeled as a function of CAD peak area:

```text
CV(Area, %) = 43.15 / CAD peak area + 0.86
```

The universal CAD calibration slope uncertainty is:

```text
CV(Slope, %) = 31.74
```

The CAD-yield uncertainty is converted to the log10 scale as:

```text
CAD yield SE (log10) = sqrt((CV(Area)/100)^2 + (CV(Slope)/100)^2) / ln(10)
```

The final corrected pEC50 uncertainty combines DRC fitting error with CAD yield uncertainty:

```text
Corrected pEC50 ±1 SE = sqrt(DRC pEC50 SE^2 + CAD yield SE(log10)^2)
```

The 95% CI half-width columns are calculated from the corresponding SE values using the normal approximation:

```text
pEC50 ±95% CI = 1.96 * pEC50 SE
```

Rows with missing or zero CAD peak areas report `-` for CAD-derived uncertainty terms.

## Worksheet: `Crude-SP to Pure Correlation`

This worksheet contains the CAD-correction validation set. Each row represents a compound-level comparison between crude and/or semi-pure material and pure-reference screening data. The two rows for `OCNT-2315472` are intentional: they share the same pure-reference compound identity but represent different crude and semi-pure syntheses/analyzes.

| Column | Field | Description |
| --- | --- | --- |
| A | `Compound ID` | Normalized compound root ID. |
| B | `SMILES` | Chemical structure as a SMILES string. |
| C | `Crude Batch ID` | Crude batch identifier. |
| D | `Semi-Pure Batch ID` | Semi-pure batch identifier. |
| E | `Pure Batch ID` | Pure-reference batch identifier. |
| F | `Phase 1 or 2` | Phase assignment from the PXR challenge reference sheet when available. |
| G | `OPA_PXR-032 (µM)` | Pure-reference EC50 from OPA_PXR-032. |
| H | `OPA_PXR-032 pEC50 (log)` | pEC50 calculated from the OPA_PXR-032 EC50. |
| I | `OPA_PXR-035 (µM)` | Pure-reference EC50 from OPA_PXR-035. |
| J | `OPA_PXR-035 pEC50 (log)` | pEC50 calculated from the OPA_PXR-035 EC50. |
| K | `OPA_PXR-036 (µM)` | Pure-reference EC50 from OPA_PXR-036. |
| L | `OPA_PXR-036 pEC50 (log)` | pEC50 calculated from the OPA_PXR-036 EC50. |
| M | `Pure pEC50s (log)` | Average of available pure-reference pEC50 values. |
| N | `OPA_PXR-032 (Emax normalized)` | Positive-control-normalized Emax from OPA_PXR-032. |
| O | `OPA_PXR-032 (Emax raw)` | Raw Emax estimate from OPA_PXR-032. |
| P | `OPA_PXR-035 (Emax normalized)` | Positive-control-normalized Emax from OPA_PXR-035. |
| Q | `OPA_PXR-035 (Emax raw)` | Raw Emax estimate from OPA_PXR-035. |
| R | `OPA_PXR-036 (Emax normalized)` | Positive-control-normalized Emax from OPA_PXR-036. |
| S | `OPA_PXR-036 (Emax raw)` | Raw Emax estimate from OPA_PXR-036. |
| T | `OPA_PXR-038 (Emax normalized)` | Positive-control-normalized Emax from the crude validation DRC experiment. |
| U | `OPA_PXR-038 (Emax raw)` | Raw Emax estimate from the crude validation DRC experiment. |
| V | `OPA_PXR-039 (Emax normalized)` | Positive-control-normalized Emax from the semi-pure validation DRC experiment. |
| W | `OPA_PXR-039 (Emax raw)` | Raw Emax estimate from the semi-pure validation DRC experiment. |
| X | `OPA_PXR-048 (Emax normalized)` | Positive-control-normalized Emax from the 96-compound semi-pure DRC experiment, where applicable. |
| Y | `OPA_PXR-048 (Emax raw)` | Raw Emax estimate from the 96-compound semi-pure DRC experiment, where applicable. |
| Z | `OPA_PXR-049 (Emax normalized)` | Positive-control-normalized Emax from the 96-compound crude DRC experiment, where applicable. |
| AA | `OPA_PXR-049 (Emax raw)` | Raw Emax estimate from the 96-compound crude DRC experiment, where applicable. |
| AB | `Volatility` | Volatility class used to select CAD data. |
| AC | `Crude EvapT (°C)` | CAD evaporator temperature used for crude quantification. |
| AD | `Crude Theoretical Mass-on-Column (ng)` | Theoretical crude mass-on-column. |
| AE | `Crude Peak Area (pA*min)` | CAD peak area used for crude yield calculation. |
| AF | `Crude Actual Mass-on-Column (ng)` | Actual crude mass-on-column calculated from CAD peak area. |
| AG | `Crude Product Yield (%)` | Uncapped crude product yield. |
| AH | `Crude Correction Factor` | Crude product yield divided by 100. |
| AI | `Crude EC50s (µM)` | Measured crude EC50. |
| AJ | `Corrected Crude EC50 (µM)` | Crude EC50 corrected using CAD-derived crude product yield. |
| AK | `Crude pEC50s (log)` | pEC50 calculated from measured crude EC50. |
| AL | `Corrected Crude pEC50 (log)` | pEC50 calculated from corrected crude EC50. |
| AM | `Semi-pure EvapT (°C)` | CAD evaporator temperature used for semi-pure quantification. |
| AN | `Semi-Pure Theoretical Mass-on-Column (ng)` | Theoretical semi-pure mass-on-column. |
| AO | `Semi-Pure Peak Area (pA*min)` | CAD peak area used for semi-pure yield calculation. |
| AP | `Semi-Pure Actual Mass-on-Column (ng)` | Actual semi-pure mass-on-column calculated from CAD peak area. |
| AQ | `Semi-Pure Product Yield (%)` | Uncapped semi-pure product yield. |
| AR | `Semi-Pure Correction Factor` | Semi-pure product yield divided by 100. |
| AS | `Semi-Pure EC50s (µM)` | Measured semi-pure EC50. |
| AT | `Corrected Semi-Pure EC50 (µM)` | Semi-pure EC50 corrected using CAD-derived semi-pure product yield. |
| AU | `Semi-Pure pEC50s (log)` | pEC50 calculated from measured semi-pure EC50. |
| AV | `Corrected Semi-Pure pEC50 (log)` | pEC50 calculated from corrected semi-pure EC50. |
| AW | `OPA_PXR-032 pEC50 SE (log)` | DRC fit SE for OPA_PXR-032 pEC50. |
| AX | `OPA_PXR-035 pEC50 SE (log)` | DRC fit SE for OPA_PXR-035 pEC50. |
| AY | `OPA_PXR-036 pEC50 SE (log)` | DRC fit SE for OPA_PXR-036 pEC50. |
| AZ | `Pure pEC50 ±1 SE (log)` | Combined ±1 SE for averaged pure-reference pEC50. |
| BA | `Crude DRC pEC50 SE (log)` | DRC fit SE for measured crude pEC50. |
| BB | `Crude CAD Peak Area CV (%)` | Peak-area-dependent CAD CV for crude CAD data. |
| BC | `Crude CAD Slope CV (%)` | Universal CAD calibration slope CV. |
| BD | `Crude CAD Yield SE (log10)` | CAD yield uncertainty converted to the log10 scale for crude correction. |
| BE | `Corrected Crude pEC50 ±1 SE (log)` | Combined DRC and CAD uncertainty for corrected crude pEC50. |
| BF | `Semi-Pure DRC pEC50 SE (log)` | DRC fit SE for measured semi-pure pEC50. |
| BG | `Semi-Pure CAD Peak Area CV (%)` | Peak-area-dependent CAD CV for semi-pure CAD data. |
| BH | `Semi-Pure CAD Slope CV (%)` | Universal CAD calibration slope CV. |
| BI | `Semi-Pure CAD Yield SE (log10)` | CAD yield uncertainty converted to the log10 scale for semi-pure correction. |
| BJ | `Corrected Semi-Pure pEC50 ±1 SE (log)` | Combined DRC and CAD uncertainty for corrected semi-pure pEC50. |
| BK | `Pure pEC50 ±95% CI (log)` | Approximate 95% CI half-width for averaged pure-reference pEC50. |
| BL | `Crude pEC50 ±95% CI (log)` | Approximate 95% CI half-width for measured crude pEC50. |
| BM | `Corrected Crude pEC50 ±95% CI (log)` | Approximate 95% CI half-width for corrected crude pEC50. |
| BN | `Semi-Pure pEC50 ±95% CI (log)` | Approximate 95% CI half-width for measured semi-pure pEC50. |
| BO | `Corrected Semi-Pure pEC50 ±95% CI (log)` | Approximate 95% CI half-width for corrected semi-pure pEC50. |

## Worksheet: `HTChem Libraries`

This worksheet contains PXR DRC follow-up and CAD correction data for two HTChem crude libraries. `Library 66534` corresponds to core `OCNT-2432456`; `Library 66535` corresponds to core `OCNT-0002416`.

| Column | Field | Description |
| --- | --- | --- |
| A | `HTChem Library` | Source HTChem library label. |
| B | `Core` | Core/scaffold compound ID. |
| C | `Compound ID` | Normalized compound root ID. |
| D | `SMILES` | Chemical structure as a SMILES string. |
| E | `Crude Batch ID` | Crude batch identifier. |
| F | `Hit or Chemisimilar` | Indicates whether the compound was selected as a primary hit or chemisimilar. |
| G | `PXR DRC Experiment` | DRC experiment ID. |
| H | `Crude EC50s (µM)` | Measured crude EC50. |
| I | `Crude pEC50s (log)` | pEC50 calculated from measured crude EC50. |
| J | `Crude Emax normalized` | Positive-control-normalized Emax. |
| K | `Crude Emax raw` | Raw Emax estimate. |
| L | `Volatility` | Volatility class used to select CAD data. |
| M | `CAD Yield/Volatility Note` | Normalized CAD/yield note. `Not sufficiently synthesized` indicates nonzero crude CAD peak area below 1.0 pA*min; `True 0% Yield / No Synthesis` indicates source-designated zero-yield/no-synthesis rows; otherwise, this field reports the applicable volatility/yield classification. |
| N | `Crude EvapT (°C)` | CAD evaporator temperature used for crude quantification. |
| O | `Crude Theoretical Mass-on-Column (ng)` | Theoretical crude mass-on-column. |
| P | `Crude Peak Area (pA*min)` | CAD peak area used for crude yield calculation. Qualitative entries are used when a numeric peak area is not appropriate: `Below LLOQ` for not-sufficiently-synthesized rows and `Undetected` for true 0% yield/no-synthesis rows. |
| Q | `Crude Actual Mass-on-Column (ng)` | Actual crude mass-on-column calculated from CAD peak area. |
| R | `Crude Product Yield (%)` | Uncapped crude product yield. |
| S | `Crude Correction Factor` | Crude product yield divided by 100. |
| T | `Corrected Crude EC50 (µM)` | Crude EC50 corrected using CAD-derived crude product yield. |
| U | `Corrected Crude pEC50 (log)` | pEC50 calculated from corrected crude EC50. |
| V | `Crude DRC pEC50 SE (log)` | DRC fit SE for measured crude pEC50. |
| W | `Crude CAD Peak Area CV (%)` | Peak-area-dependent CAD CV for crude CAD data. |
| X | `Crude CAD Slope CV (%)` | Universal CAD calibration slope CV. |
| Y | `Crude CAD Yield SE (log10)` | CAD yield uncertainty converted to the log10 scale. |
| Z | `Corrected Crude pEC50 ±1 SE (log)` | Combined DRC and CAD uncertainty for corrected crude pEC50. |
| AA | `Crude pEC50 ±95% CI (log)` | Approximate 95% CI half-width for measured crude pEC50. |
| AB | `Corrected Crude pEC50 ±95% CI (log)` | Approximate 95% CI half-width for corrected crude pEC50. |

## Worksheet: `96-Compound µScale Semi-Pure`

This worksheet contains semi-pure PXR DRC and CAD correction data for the 96-compound µscale synthesis library.

| Column | Field | Description |
| --- | --- | --- |
| A | `Library` | Source library label. |
| B | `Compound ID` | Normalized compound root ID. |
| C | `SMILES` | Chemical structure as a SMILES string. |
| D | `Semi-Pure Batch ID` | Semi-pure batch identifier. |
| E | `PXR DRC Experiment` | DRC experiment ID. |
| F | `Semi-Pure EC50s (µM)` | Measured semi-pure EC50. |
| G | `Semi-Pure pEC50s (log)` | pEC50 calculated from measured semi-pure EC50. |
| H | `Semi-Pure Emax normalized` | Positive-control-normalized Emax. |
| I | `Semi-Pure Emax raw` | Raw Emax estimate. |
| J | `Volatility` | Volatility class used to select CAD data. |
| K | `Semi-pure EvapT (°C)` | CAD evaporator temperature used for semi-pure quantification. |
| L | `Semi-Pure Theoretical Mass-on-Column (ng)` | Theoretical semi-pure mass-on-column. |
| M | `Semi-Pure Peak Area (pA*min)` | CAD peak area used for semi-pure yield calculation. Qualitative entries such as `Undetected` are used when no numeric CAD peak area is available. |
| N | `Semi-Pure Actual Mass-on-Column (ng)` | Actual semi-pure mass-on-column calculated from CAD peak area. |
| O | `Semi-Pure Product Yield (%)` | Uncapped semi-pure product yield. |
| P | `Semi-Pure Correction Factor` | Semi-pure product yield divided by 100. |
| Q | `Corrected Semi-Pure EC50 (µM)` | Semi-pure EC50 corrected using CAD-derived semi-pure product yield. |
| R | `Corrected Semi-Pure pEC50 (log)` | pEC50 calculated from corrected semi-pure EC50. |
| S | `Semi-Pure DRC pEC50 SE (log)` | DRC fit SE for measured semi-pure pEC50. |
| T | `Semi-Pure CAD Peak Area CV (%)` | Peak-area-dependent CAD CV for semi-pure CAD data. |
| U | `Semi-Pure CAD Slope CV (%)` | Universal CAD calibration slope CV. |
| V | `Semi-Pure CAD Yield SE (log10)` | CAD yield uncertainty converted to the log10 scale. |
| W | `Corrected Semi-Pure pEC50 ±1 SE (log)` | Combined DRC and CAD uncertainty for corrected semi-pure pEC50. |
| X | `Semi-Pure pEC50 ±95% CI (log)` | Approximate 95% CI half-width for measured semi-pure pEC50. |
| Y | `Corrected Semi-Pure pEC50 ±95% CI (log)` | Approximate 95% CI half-width for corrected semi-pure pEC50. |
