# Octant Bio UHPLC-CAD-MS Method

External UHPLC-CAD-MS method summary.

## Method Summary

| Parameter | Method setting |
| --- | --- |
| LC system | Agilent 1290 Infinity II UHPLC configured with two binary pumps |
| CAD detector | Thermo Scientific Corona Veo RS |
| Mass spectrometer | Thermo Scientific TSQ Quantis Plus triple quadrupole |
| Column | Waters ACQUITY UPLC HSS C18, 100 Å, 1.8 µm, 2.1 x 50 mm |
| Column compartment temperature | 60 °C on the active/right column position |
| Analytical column flow rate | 0.600 mL/min from binary pump 1 |
| Inverse-gradient makeup flow rate | 0.600 mL/min from binary pump 2, added post-column before detector splitting |
| Total flow before detector splitter | 1.200 mL/min |
| Detector split ratio | 10:1 fixed-flow split after addition of inverse-gradient flow |
| CAD flow rate after split | 90.91% of total flow = 1090.91 µL/min |
| MS flow rate after split | 9.09% of total flow = 109.09 µL/min |
| Run time | 4.000 min |

## Column and Mobile Phases

| Parameter | Specification |
| --- | --- |
| Stationary phase | Waters ACQUITY UPLC HSS C18 |
| Column dimensions | 2.1 x 50 mm |
| Particle size | 1.8 µm |
| Pore size | 100 Å |
| Separation mode | Reversed phase |
| Mobile phase A | 80:20 water:methanol (v/v) |
| Mobile phase B | 80:20 acetonitrile:methanol (v/v) |

## UHPLC Gradient Program

### Binary Pump 1: Analytical Gradient

Pump 1 delivers the analytical gradient through the column at 0.600 mL/min. Pressure limits set to 1300 bar.

| Time (min) | A (%) | B (%) | Flow (mL/min) | Pressure limit (bar) |
| ---: | ---: | ---: | ---: | ---: |
| 0.00 | 90.00 | 10.00 | 0.600 | 1300 |
| 0.60 | 90.00 | 10.00 | 0.600 | 1300 |
| 1.20 | 50.00 | 50.00 | 0.600 | 1300 |
| 2.50 | 40.00 | 60.00 | 0.600 | 1300 |
| 3.20 | 0.00 | 100.00 | 0.600 | 1300 |
| 3.60 | 0.00 | 100.00 | 0.600 | 1300 |
| 3.62 | 90.00 | 10.00 | 0.600 | 1300 |
| 4.00 | 90.00 | 10.00 | 0.600 | 1300 |

### Binary Pump 2: Inverse-Gradient Makeup Program

Pump 2 delivers an inverse-gradient stream at 0.600 mL/min. This flow is combined with the column effluent after the column and before detector splitting to stabilize CAD response across the analytical gradient.

| Time (min) | A (%) | B (%) | Flow (mL/min) | Pressure limit (bar) |
| ---: | ---: | ---: | ---: | ---: |
| 0.00 | 10.00 | 90.00 | 0.600 | 1300 |
| 0.95 | 10.00 | 90.00 | 0.600 | 1300 |
| 1.55 | 50.00 | 50.00 | 0.600 | 1300 |
| 2.85 | 60.00 | 40.00 | 0.600 | 1300 |
| 3.55 | 100.00 | 0.00 | 0.600 | 1300 |
| 3.95 | 100.00 | 0.00 | 0.600 | 1300 |
| 3.97 | 10.00 | 90.00 | 0.600 | 1300 |
| 4.00 | 10.00 | 90.00 | 0.600 | 1300 |

## Post-Column Flow Splitting

The 0.600 mL/min column effluent and 0.600 mL/min inverse-gradient makeup stream are combined after the column, giving a total detector-bound flow of 1.200 mL/min before the fixed-flow splitter.

| Component | Value |
| --- | --- |
| Splitter configuration | 10:1 fixed-flow splitter |
| Splitter hardware | Binary Fixed Flow Splitter Replacement Resistor Set for Model 63 Splitter |
| Manifold | 10:1, SKU 63-440 |
| Total flow entering splitter | 1.200 mL/min |
| Low-flow leg to MS | 1/11 of total flow = 9.09% = 0.10909 mL/min = 109.09 µL/min |
| High-flow leg to CAD | 10/11 of total flow = 90.91% = 1.09091 mL/min = 1090.91 µL/min |

## Autosampler and Column Compartment Settings

| Parameter | Setting |
| --- | --- |
| Autosampler | Agilent multisampler G7167B |
| Needle wash | Standard Wash |
| Draw speed | 100.0 µL/min |
| Eject speed | 400.0 µL/min |
| Wait time after draw | 1.2 s |
| Needle height offset | 0.0 mm |
| Vial/well bottom sensing | Off |
| Sample flush-out factor | 5.0 |
| Overlapped injection | Off |
| Column compartment | Agilent G1316C |
| Column compartment temperature | Left side 40.0 °C; right side 60.0 °C |
| Temperature-ready criterion | Within ±0.8 °C |

## Charged Aerosol Detector Settings

| Parameter | Setting |
| --- | --- |
| Detector | Thermo Scientific Corona Veo RS |
| Detector flow path | High-flow splitter leg, 1090.91 µL/min |
| Detector channel | CAD_1 |
| Power function value | 1.15 |
| Data collection rate | 10 Hz |
| Filter time constant | 1.0 s |
| Gas regulation mode | Analytical |
| Peak-width setting | 0.02 min |
| Evaporator temperature | 65 °C |
| Evaporator ready tolerance | ±5.0 K |

## Mass Spectrometer Settings

| Parameter | Setting |
| --- | --- |
| Mass spectrometer | Thermo Scientific TSQ Quantis Plus triple quadrupole |
| Ionization source | H-ESI |
| MS flow path | Low-flow splitter leg, 109.09 µL/min |
| Spray voltage mode | Static |
| Positive ion spray voltage | 3500 V |
| Negative ion spray voltage | 2500 V |
| Sheath gas | 35 Arb |
| Auxiliary gas | 7 Arb |
| Sweep gas | 0 Arb |
| Ion transfer tube temperature | 300 °C |
| Vaporizer temperature | 275 °C |
| APPI lamp | Not in use |
| FAIMS mode | Not installed |
| Default charge state | 1 |
| Internal mass calibration | Off |
| Current lock mass | Current |

## MS Acquisition Program

| Parameter | Setting |
| --- | --- |
| Experiment type | Full Scan Q3 |
| Acquisition time | 0.00-4.00 min |
| Polarity | Positive |
| Scan range | m/z 100-1000 |
| Scan rate | 1000 Da/s |
| Q3 resolution | 0.7 FWHM |
| Source fragmentation | 0 |
| CID gas | 0 mTorr |
| Chromatographic peak width | 6 s |
| Chromatographic filter | Enabled |
