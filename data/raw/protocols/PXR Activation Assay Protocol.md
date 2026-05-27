# **PXR Activation Assay Protocol**

**Assays:** 
1) PXR \- Pregnane X Receptor Primary Assay, WT Reporter  
2) PCA \- Pregnane X Receptor Counter Assay, KO Reporter

**Plate format:** 1536-well (Greiner Bio-One White Cell Culture Microplate, Cat. 782080)


## **Screening Format**
Compounds were tested in single-dose format, then promoted to dose-response curves, with the following formats:
> **Tiered screen**
>- Tier 1: 10 uM & 30 uM single dose per compound
>- Tier 2: 9-point dose-response curves ranging from 5 nM to 50 uM
>- Use for >1000 compound screens
>- Run Tier 1 format assay using the PXR WT cell line.
>- Based on activity profiles, downselect compounds to run in the Tier 2 format assay for each of PXR WT and PCA KO cell lines.

>**Non-tiered screen:** 22-point dose-response curves ranging from 1 nM to 100 uM
>- Use for <1000 compound screens
## **Assay Parameters**
**Cell lines:**
- WT PXR reporter line
- KO PXR reporter line
  
**Reagents:**

- Gibco™ DMEM, high glucose, GlutaMAX™ Supplement (Cat. 10-566-024)  
- Gibco™ Fetal Bovine Serum, Premium (Cat. A5670701)  
- Gibco™ TrypLE™ Select Enzyme (1X) (Cat. 12563011)  
- Gibco™ Trypan Blue Solution, 0.4% (Cat. 15250061)  
- Promega Nano-Glo® Luciferase Assay System (Cat. N1150)  
- Doxycycline hyclate, 10mM in 1mL DMSO (Apex Bio, Cat. A4052)
- DNAse/RNAse free water
- Gibco™ PBS, pH 7.4 (Cat. 10010049)
- Sterile filtered Poly-D-lysine solution, 100mg/L  
  - Poly-D-lysine hydrobromide solid dissolved in PBS
    
| Cell Slurry Parameters |  |
| ----- | ----- |
| **Parameter** | **Value** |
| Base media | DMEM |
| Qualified FBS concentration | 10% |
| Cell concentration | 1.5e6 cells/mL |
| PDL solution concentration | 2ug/mL |
| Doxycycline concentration | 100 nM |

| Assay Parameters |  |
| ----- | ----- |
| **Parameter** | **Value** |
| Compound concentration range | **Select one format:**<br>10 uM and 30 uM (2 dose)<br>5 nM-50 uM (9-point DRC)<br>1 nM-100 uM (22-point DRC) |
| Cell slurry volume | 3 uL/well |
| Cell quantity | 4500 cells/well |
| Drug incubation | O/N, 18-24 hours at 37°C, 5% CO2 |
| Nano-Glo® Luciferase Assay Reagent (0.25X) volume | 3 uL/well |
| Detection reagent post-dispense incubation | 10 mins at RT |
| Total assay volume | 6 uL/well |
| Readout | Luminescence, 100ms integration time (Molecular Devices SpectraMax i3x) |
## **Protocol**
*Identical between WT and KO assay. Use appropriate cell line for selected assay.*
### **1\. Generate drug plates**

1\. Pre-add drug to empty 1536-well plates using either a Beckman Coulter Echo acoustic liquid handler or Tecan D300e digital liquid dispenser.

- DMSO content should not exceed 1% of the 3 uL assay volume, or 30 nL.
- All wells should be normalized to contain identical DMSO content.
- Plates can be sealed and frozen for at least two weeks at -20°C until needed.
### **2\. Passage cells**

1. Thaw cells from a fresh cryovial stock. Cells should undergo at least 1 passage post-thaw and prior to seeding for assay, and can be used for 2-3 weeks of additional assays after the first passage.
2. Passage cells 1-4 days in advance of scheduled assay day. Seed at an appropriate cell density to achieve 80-90% confluency on assay day. In a T225, 100% confluency for either cell line is \~60e6 cells.

    | Days until assay | Cell split |
    | :---- | :---- |
    | 1 | 1:2.5 |
    | 2 | 1:5 |
    | 3 | 1:10 |

### **3\. Prep reagents**
   - Set out pre-drugged 1536-well plates 2 hours in advance of assay.
   - Warm DMEM and thaw FBS to 37°C
   - Thaw an aliquot of 10 mM dox (<10 uL needed)
   - Examine flasks under incubator to confirm \~80-90% confluency
   - Once thawed, add 50 mL FBS to a 500 mL bottle of DMEM and shake to mix

### **4\. Lift and count cells**
*For a T-225 flask of cells, use 8 mL TrypLE and 16 mL media. For other flask types, scale up or down according to surface area.*

   1. Aspirate media. Add 8 mL TrypLE to bottom of flask. Let sit for 2-5 minutes.
   3. Add 16 mL media to quench TrypLE. Pipette up and down to collect all cells, then dispense into a 50 mL conical.
   4. Centrifuge 300g x 3 mins to pellet cells.
   5. Aspirate media. Resuspend pellet using a P1000 to ensure homogeneous slurry.
   6. Resuspend slurry to an estimated final volume of \~2e6 cells/mL
        - For example, if working with 8 flasks and estimate each is at \~50-60e6 cells total, aim to resuspend & combine all slurries to a total volume of \~240 mL, in a 250mL sterile conical.
7. Collect and count 2-4 biological replicates of well-mixed cell slurry
    - For each replicate, mix 25 uL Trypan Blue with 25 uL cells, then dispense 10 uL of the combined mix onto a Countess slide and measure.
8. Calculate the average cell concentration.
     - If the CV across counts is greater than 15%, collect new samples and recount.
     - Confirm average viability is 90-100%.

### **5\. Prepare slurry**

1. Resuspend cells to 1.5e6 / mL
4. Add PDL stock to a concentration of 0.02X.
     - Divide slurry volume by 50.
     - 10 mL of cell slurry receives 200 uL PDL.
6. Add doxycycline stock to a concentration of  100 nM.
   -  For stock doxycycline, divide slurry volume by 100,000.
   - If the necessary amount is <1 uL, dilute dox 1:10 in DMSO.
     - 50 mL of cell slurry receives 0.5 uL of stock doxycycline, or 5 uL of 1:10 diluted stock.

### **6\. Set up Multiflo for Cell Dispense**

1. Set the MultiFlo to 1 uL cassette mode.
2. Ensure there is a protocol pre-set on the MultiFlo to dispense 3 uL into 1536-well Greiner plates, with an appropriate height and dispense speed.
3. Run a cell-specific cassette cleaning protocol on the MultiFlo, consisting of priming with CoulterClenz, water, ethanol, then water.
> Optional: thorough cleanse prior to 1536-well dispenses
 >1. Purge line, loosen cassette fully, and place dongle into an empty conical.
 >2. Flush each pin with a syringe of water connected by tubing to the pin, until water cleanly jets out the dongle for each pin.
   >5. Tighten cassette again.
4. Prime with H2O x 3, PBS x 3, and spare DMEM x 3
3. Dispense media into a test 1536-well plate. Confirm no splashes or misdispenses.
> If dispensing cells into >6 drug plates, use a spin vessel to keep cells in suspension and homogeneous
 >1. Thoroughly spray spin vessel lid with ethanol, then rinse off with milliQ
> 2. Replace disposable slurry container with a new sterile container, and cover with lid.
> 4. Program spin vessel to 100 RPM, 4 rotations, and 500 ms pause
### **7\. Dispense cells**
   1. Resuspend conical of cell slurry thoroughly. If the volume is too large to resuspend with a 50 mL serological pipet, gently invert the entire conical several times.
   2. If using a spin vessel, pour cells into the sterile container, replace lid, turn on. If using a conical of cells, continue swirling and inverting the conical by hand or using a benchtop shaker until it's time to dispense cells.
   3. Prime media x 2. Monitor dispense for clogs.
   4. Place dongle into cell conical or spin vessel.
   5. Prime with cells x 2. Monitor for clogs.
   6. Dispense cells into a test 1536-well plate. Confirm no splashes or misdispenses
   7.  Dispense 3 uL cells per well into pre-drugged assay plates.
   8.  Spin plates for 30s at 150g.
   9.  Place in incubator or SteriStore, for 18-24 hours at 37°C, 5% CO2

### **8\. O/N Incubation**

### **9\. Prepare for readout**
- 60-120 minutes prior to readout, thaw Nano-Glo® Luciferase Assay Buffer at RT. Do **not** thaw above 25°C.
- 30 mins before dispense, remove plates from incubator and equilibrate to room temperature.
1. Set the MultiFlo to 1 uL cassette mode and locate the 3 uL 1536-well Greiner plate protocol.
2. Prime with H2O x 2. Monitor for clogs.
3. Dispense H2O into a test 1536-well plate. Confirm no splashes or misdispenses.
4. Combine Nano-Glo® Luciferase Assay Substrate and Nano-Glo® Luciferase Assay Buffer at a 50 to 1 ratio as per manufacturer's protocol. Refer to manufacturer's protocol for additional guidance.
5. Dilute the Nano-Glo reagent to 0.25X by adding 3X the existing volume in H2O.
6. Prime MultiFlo cassette with Nano-Glo reagent. Monitor for clogs.
7. Dispense Nano-Glo reagent into a test 1536-well plate. Confirm no splashes or misdispenses.

### **10\. Dispense luciferase reagent**
1. Dispense 3 uL Nano-Glo reagent per well into drugged cell plates.
2. Centrifuge for 30s at 150g
3. Cover plates from light and incubate for 10 minutes at RT.

### **11\. Reagent Incubation**

### **12\. Readout**

Submit plates to i3x reader for luminescent detection.

---
*This protocol was developed and finalized by Bryan Jiang, Sam Sabaat, Theo Tarver, and Ayesha Tasneem Ghazali.*
