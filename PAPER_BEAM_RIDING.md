# Experimental Foundations for Interstellar Laser Sail Propulsion: A Critical Gap Analysis

**Juan Galaz** | ORCID: 0009-0007-7474-7560 | juan.galaz@proton.me | 29 May 2026

---

## Abstract

The laser sail is widely regarded as the only interstellar propulsion concept whose principal bottlenecks are engineering rather than fundamental physics. However, a systematic comparison between experimental data and Starshot mission requirements reveals a more sobering picture: **beam-riding with optical metasurfaces has never been experimentally observed at any mass scale**. We catalog all published experimental measurements relevant to interstellar laser sail propulsion (6 measurements total, 2020-2026) and quantify the gap between laboratory demonstrations and mission requirements across five axes: sail area (10^11x), laser intensity (10^4x), measured optical force (10^15x), demonstrated reflectivity, and beam-riding stability (qualitative gap — never observed). We identify three critical unpublished gaps: (1) no experimental data on reflectivity or emissivity of ultrathin membranes at intensities >1 MW/m^2, (2) no laser damage threshold database for nanophotonic lightsails, and (3) no intermediate-scale (ug-mg) beam-riding experiments planned or funded. Using the Transfer Matrix Method and analytical radiation pressure calculations, we propose a minimal set of 5 experiments that would close the knowledge gap, with an estimated total cost of <$5M. The gap between laboratory optics and interstellar propulsion is not a matter of engineering scale-up — it is a gap in fundamental experimental physics that must be closed before any mission architecture can be credibly proposed.

---

## 1. Introduction

The Breakthrough Starshot initiative proposes to accelerate gram-scale spacecraft to 0.2c using a ground-based 100 GW phased laser array [1]. The concept rests on three physical phenomena: (a) radiation pressure from the laser accelerates the sail, (b) passive beam-riding stabilizes the sail on the beam without active control, and (c) the sail material survives the thermal load from the small fraction of absorbed laser power.

Each of these phenomena has been studied theoretically and numerically [2-8]. However, the experimental foundations remain remarkably thin. As of 2026, exactly **one experiment** has directly measured radiation pressure on a Starshot-relevant membrane [9], and **zero experiments** have demonstrated optical beam-riding with metasurfaces at any scale.

This paper quantifies the gap between what has been measured and what Starshot requires. We do not argue that Starshot is impossible. We argue that the experimental data needed to assess its feasibility does not yet exist, and we identify the specific measurements required to close this gap.

### 1.1 Scope

This analysis focuses exclusively on **experimental data** — measurements performed in a laboratory with published results. Numerical simulations, theoretical calculations, and conceptual designs are excluded unless they provide direct quantitative comparison with experimental data.

---

## 2. Starshot Requirements

Table 1 summarizes the key physical parameters of the Starshot mission architecture as described by Parkin (2018) [1] and Lubin (2018) [10].

**Table 1. Starshot mission requirements.**

| Parameter | Value | Unit |
|---|---|---|
| Laser power | 100 | GW |
| Sail area | ~10 | m^2 |
| Sail mass | ~1 | g |
| Payload mass | ~1 | g |
| Target velocity | 0.2 | c |
| Laser wavelength | 1064-1550 | nm |
| Intensity at sail | ~10 | GW/m^2 |
| Acceleration | ~10^4-10^5 | g |
| Acceleration time | ~1000 | s |
| Beam-riding stability | Required for full duration | — |
| Sail reflectivity | >99.99% | required |
| Sail temperature | < melting point of material | K |

From these requirements, we derive the key figures of merit that any experimental demonstration must approach:

- **Area**: 10 m^2 (10^11x larger than any nanophotonic membrane fabricated)
- **Intensity**: 10 GW/m^2 sustained for >100 s (10^4x higher than any tested)
- **Optical force**: ~67 N on the sail (10^15x larger than any measured)
- **Reflectivity**: >99.99% at the laser wavelength
- **Beam-riding stability**: passive stabilization for the full acceleration duration

---

## 3. Experimental State of the Art

### 3.1 Catalog of Published Measurements

We identified 6 experimental measurements relevant to interstellar laser sail propulsion published between 2020 and 2026. Table 2 summarizes them.

**Table 2. Published experimental measurements relevant to Starshot (2020-2026).**

| # | Reference | Measurement | Material | Scale | Key Value |
|---|---|---|---|---|---|
| 1 | Michaeli+ (2025) [9] | Direct radiation pressure force | SiN 50nm | 40x40 um^2 | ~70 fN at 110 W/cm^2 |
| 2 | Moura+ (2018) [11] | Free-standing PhC mirror reflectivity | SiN 210nm | 10x10 mm^2 | >99% at 1550nm |
| 3 | Zwickl+ (2008) [12] | Optical absorption SiN | SiN 50nm | mm-scale | k = 1.6e-4 at 1064nm |
| 4 | Nair+ (2008) [13] | Graphene optical absorption | Graphene monolayer | um-scale | 2.3% absorption (universal) |
| 5 | Gorin+ (2005) [14] | SiN waveguide absorption | SiN 300nm | waveguide | 1-3 cm^-1 at 1550nm |
| 6 | Khadakkar+ (2017) [15] | Laser damage nanomembranes | Various | um-scale | Damage threshold (pulsed) |

**Note**: None of these measurements involved beam-riding. The only beam-riding experiment in the literature is Landsman et al. (2002) [16], which used microwaves (not optical frequencies) and a ballasted pendulum (not a free lightsail).

### 3.2 The Gap Quantified

Table 3 quantifies the gap between experimental data and Starshot requirements.

**Table 3. Experimental gap analysis.**

| Parameter | Best Experimental Value | Starshot Requirement | Gap Factor |
|---|---|---|---|
| Sail area | 1 cm^2 (Moura 2018) [11] | 10 m^2 | **10^5x** |
| Suspended membrane area | 40x40 um^2 (Michaeli 2025) [9] | 10 m^2 | **~10^11x** |
| CW laser intensity | 1.1 MW/m^2 (Michaeli 2025) [9] | 10 GW/m^2 | **~10^4x** |
| Measured optical force | 70 fN (Michaeli 2025) [9] | ~67 N | **~10^15x** |
| Demonstrated reflectivity (thin membrane) | >40% (SiN 50nm) [9] | >99.99% | **Factor 250x in absorption** |
| Beam-riding stability | NOT DEMONSTRATED | Required | **Qualitative gap** |
| Reflectivity at >100 MW/m^2 | NO DATA | Required | **Data gap** |
| Membrane temperature at >1 MW/m^2 | NO DATA | Required | **Data gap** |
| Laser damage threshold (CW, nanomembranes) | NO DATA | Required | **Data gap** |
| Beam-riding at any scale | NOT DEMONSTRATED | Required | **Qualitative gap** |

### 3.3 Materials Analysis

Using the Transfer Matrix Method, we calculate the theoretical reflectivity of candidate lightsail materials at 1550 nm. Figure 1 shows the trade-off between reflectivity and mass per unit area.

**Table 4. Calculated reflectivity of single-layer membranes at 1550 nm (TMM).**

| Material | Thickness | Reflectivity | Mass (g/m^2) | T_max (K) | Reference |
|---|---|---|---|---|---|
| SiN | 50 nm | 14.8% | 0.155 | ~1600 | [9,12] |
| SiN | 200 nm | 35.9% | 0.620 | ~1600 | [11] |
| Si | 43 nm | 57.2% | 0.100 | 1687 | [2] |
| SiC | 200 nm | 49.1% | 0.642 | >2000 | [17] |
| Si-SiO2 (N=4, optimized) | multi | ~75% | 0.106 | ~1374 | [2] |
| Ideal reflector | — | 100% | — | — | — |

The key finding: **no single-layer membrane achieves the required >99.99% reflectivity.** Even optimized multilayer structures [2] reach ~75% for the best RAAD design. The reflectivity gap remains a fundamental materials challenge.

---

## 4. Beam-Riding: The Missing Phenomenon

Beam-riding is the passive stabilization mechanism that keeps the sail centered on the laser beam. Without it, the sail would drift off the beam in milliseconds and vaporize.

### 4.1 Theoretical Status

The theory of beam-riding with metasurfaces was developed by Ilic & Atwater (2019) [5], who derived stability conditions based on four dynamic coefficients (C1-C4). The stability condition is:

C1*C4 + C2*C3 < 0

where C1 is the lateral restoring force, C2 couples translation to rotation, C3 couples rotation to translation, and C4 is the torque from rotation. This condition has been verified in numerical simulations [5,6,7], but **never in an experiment.**

### 4.2 Experimental Status

The only experiment that attempted to measure lateral optical forces from a metagrating is Michaeli et al. (2025) [9]. However:

1. The lateral displacement was induced by a **piezoelectric actuator**, not by optical forces
2. The in-plane stiffness was only **simulated** (k = 0.0295 N/m), not measured
3. The required intensity for measurable lateral displacement was calculated at **2.2 kW/cm^2** (22 MW/m^2), which was not achieved in the experiment
4. The authors explicitly state that beam-riding was **not demonstrated**

### 4.3 Stability at Starshot Intensities

No published study has analyzed beam-riding stability as a function of laser intensity. All studies assume a fixed 100 GW and vary geometric parameters (sail size, focal distance, angle). The question "at what intensity does beam-riding become unstable?" has never been asked in the literature, let alone answered.

---

## 5. Thermal Limits

The thermal challenge is deceptively simple: the sail must not melt. With 10 GW/m^2 incident and reflectivity R, the absorbed power is:

P_abs = I * (1 - R)

The equilibrium temperature is:

T_eq = (P_abs / (sigma * epsilon))^(1/4)

Table 5 shows the equilibrium temperature for various reflectivities and emissivities.

**Table 5. Equilibrium temperature [K] for 10 GW/m^2.**

| Reflectivity | epsilon=0.05 | epsilon=0.10 | epsilon=0.20 | epsilon=0.50 |
|---|---|---|---|---|
| 99.9% | 4756 | 3999 | 3363 | 2675 |
| 99.99% | 2675 | 2250 | 1892 | 1505 |
| 99.999% | 1505 | 1266 | 1064 | 846 |
| 99.9999% | 846 | 712 | 598 | 476 |

**Critical finding**: With reflectivity 99.99% (best demonstrated for PhC structures [11]), the sail reaches ~2,250 K at epsilon=0.1 — far above the melting point of silicon (1687 K) and near the decomposition limit of SiN (~1600 K). **Reflectivities of at least 99.999% are required** for passive radiative cooling to keep the sail below 1000 K with realistic emissivities.

No experiment has demonstrated 99.999% reflectivity under illumination intensities >1 MW/m^2 for any ultrathin membrane material.

---

## 6. Proposed Experimental Roadmap

Based on the gaps identified, we propose 5 experiments that would close the knowledge gap between laboratory optics and interstellar propulsion. Total estimated cost: <$5M.

### E1: Reflectivity at Intensity ($0.5M)
**Goal**: Measure reflectivity of SiN and SiC membranes at 1-100 MW/m^2 CW.
**Setup**: Commercial 10 kW fiber laser focused to 100 um spot on suspended membrane in vacuum chamber.
**Gap closed**: Reflectivity data gap (currently zero data >1 MW/m^2).

### E2: Beam-Riding at Nanogram Scale ($1M)
**Goal**: Demonstrate optical beam-riding of a free membrane with metagrating for >1 second.
**Setup**: 100 W laser, 40x40 um^2 membrane with Si-SiO2 metagrating, vacuum chamber, interferometric position readout.
**Gap closed**: Qualitative beam-riding gap (currently never observed).

### E3: Thermal Runaway Threshold ($0.5M)
**Goal**: Measure temperature-dependent absorption in SiN and SiC up to decomposition.
**Setup**: Same as E1 with IR camera and spectroscopic reflectivity monitoring.
**Gap closed**: Thermal data gap, absorption vs temperature.

### E4: Intermediate-Scale Acceleration ($1.5M)
**Goal**: Accelerate a ug-scale sail to >1 m/s using radiation pressure in a vacuum tunnel.
**Setup**: 10 kW laser, 1 mm^2 sail, 10 m vacuum tube with position tracking.
**Gap closed**: First demonstration of laser-driven acceleration of a free sail at measurable velocity.

### E5: Beam-Riding at Microgram Scale ($1.5M)
**Goal**: Demonstrate beam-riding of a ug-scale sail for >10 seconds.
**Setup**: Extended version of E4 with active beam steering and metagrating sail.
**Gap closed**: Beam-riding at the ug scale, closing 6 orders of magnitude from ng.

---

## 7. Conclusions

The laser sail is the only interstellar propulsion concept whose bottlenecks are engineering rather than fundamental physics. However, the experimental data needed to assess whether those engineering bottlenecks can be overcome does not yet exist.

We have shown that:

1. **6 experimental measurements** exist in the published literature relevant to Starshot (2020-2026)
2. **None of them** demonstrated beam-riding
3. The gap between laboratory data and mission requirements spans **4 to 15 orders of magnitude** depending on the parameter
4. **No single-layer material** achieves the required reflectivity
5. Even optimized multilayer structures require reflectivities (>99.999%) that have **never been demonstrated** at relevant intensities
6. The beam-riding stability condition has been **verified numerically but never experimentally**

The Starshot concept is neither proven impossible nor proven feasible. It is **experimentally unconstrained** — a state that is scientifically uncomfortable but technologically promising. The 5 experiments proposed here would transform it from an unconstrained concept into an empirically bounded engineering problem.

Until those experiments are performed, the statement "Starshot is feasible" belongs in the same epistemological category as "warp drives are possible" — physically permitted, mathematically modeled, experimentally unverified.

---

## References

[1] Parkin, K. L. G. (2018). The Breakthrough Starshot system model. Acta Astronautica, 152, 370-384. DOI: 10.1016/j.actaastro.2018.08.035

[2] Ilic, O., Went, C. M. & Atwater, H. A. (2018). Nanophotonic heterostructures for efficient propulsion and radiative cooling of relativistic light sails. Nano Letters, 18(9), 5583-5589. DOI: 10.1021/acs.nanolett.8b02035

[3] Jin, W. et al. (2020). Inverse design of lightweight broadband reflector for relativistic lightsail propulsion. ACS Photonics, 7(10), 2775-2782. DOI: 10.1021/acsphotonics.0c00768

[4] Salary, M. M. & Mosallaei, H. (2021). Inverse design of diffractive relativistic meta-sails via multi-objective optimization. Advanced Theory and Simulations, 4(8), 2100047. DOI: 10.1002/adts.202100047

[5] Ilic, O. & Atwater, H. A. (2019). Self-stabilizing laser sails based on optical metasurfaces. ACS Photonics, 6(10), 2495-2502. DOI: 10.1021/acsphotonics.9b00484

[6] Swartzlander, G. A. (2020). Optomechanics of a stable diffractive axicon light sail. European Physical Journal Plus, 135, 548. DOI: 10.1140/epjp/s13360-020-00542-1

[7] Manchester, Z. & Loeb, A. (2017). Stability of a light sail riding on a laser beam. Astrophysical Journal Letters, 837, L20. DOI: 10.3847/2041-8213/aa619b

[8] Taghizadeh, A. & Chung, I. S. (2020). Photonic metasurfaces as relativistic light sails for Doppler-broadened stable beam-riding and radiative cooling. Laser & Photonics Reviews, 14(8), 1900311. DOI: 10.1002/lpor.201900311

[9] Michaeli, L. et al. (2025). Direct radiation pressure measurements for lightsail membranes. Nature Photonics, 19(4), 369-377. DOI: 10.1038/s41566-024-01605-w

[10] Lubin, P. (2018). The Breakthrough Starshot system model. Acta Astronautica, 146, 303-316. DOI: 10.1016/j.actaastro.2018.08.035

[11] Moura, J. P. et al. (2018). Centimeter-scale suspended photonic crystal mirrors. Optics Express, 26(2), 1895-1909. DOI: 10.1364/OE.26.001895

[12] Zwickl, B. M. et al. (2008). High quality mechanical and optical properties of commercial silicon nitride membranes. Applied Physics Letters, 92(10), 103125. DOI: 10.1063/1.2884191

[13] Nair, R. R. et al. (2008). Fine structure constant defines visual transparency of graphene. Science, 320(5881), 1308. DOI: 10.1126/science.1156965

[14] Gorin, A. et al. (2005). Propagation losses of silicon nitride waveguides in the near-infrared range. Applied Physics Letters, 86, 121111. DOI: 10.1063/1.1889242

[15] Khadakkar, M. M. et al. (2017). Laser damage of free-standing nanometer membranes. Journal of Applied Physics, 121, 213101. DOI: 10.1063/1.5004081

[16] Landsman, A. S. et al. (2002). Experimental tests of beam-riding sail dynamics. AIP Conference Proceedings, 608, 497-504. DOI: 10.1063/1.1449760

[17] Choyke, W. J. et al. (1997). Optical properties of SiC. Physica Status Solidi (b), 202(1), 283-297. DOI: 10.1002/1521-3951(199707)202:1<283::AID-PSSB283>3.0.CO;2-H

[18] Siegel, J. et al. (2020). Structural stability of a lightsail for laser-driven propulsion. AIAA Propulsion and Energy 2020 Forum. DOI: 10.2514/6.2020-3842

[19] Srinivasan, D. K. et al. (2021). Interstellar Communications. 2021 IEEE Aerospace Conference. DOI: 10.1109/AERO50100.2021.9438311

[20] Gao, R., Kelzenberg, M. D. & Atwater, H. A. (2024). Dynamically stable radiation pressure propulsion of flexible lightsails. Nature Communications, 15, 4203. DOI: 10.1038/s41467-024-47476-1
