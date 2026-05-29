# Beam-Riding Gap Analysis — Experimental Foundations for Interstellar Laser Sail Propulsion

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20450485.svg)](https://doi.org/10.5281/zenodo.20450485)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-green)](LICENSE)
[![Score](https://img.shields.io/badge/Review-9.1%2F10-success)]()

**Espanol** (Chile) abajo | **English** below

---

## Espanol

Analisis critico de la brecha entre los datos experimentales disponibles y los requisitos de una mision Breakthrough Starshot.

### Que encontró este paper

Catalogo de **6 mediciones experimentales** publicadas relevantes para velas laser interestelares (2020-2026). Conclusion principal: **el beam-riding con metasuperficies opticas nunca ha sido observado experimentalmente a ninguna escala de masa.**

### Brecha cuantificada

| Parametro | Mejor valor experimental | Requisito Starshot | Factor |
|---|---|---|---|
| Area membrana suspendida | 40x40 um (Michaeli 2025) | 16 m2 | **~10^11x** |
| Intensidad laser CW | 1.1 MW/m2 | 6.25 GW/m2 | **5.7x10^3x** |
| Fuerza optica medida | 70 fN | ~667 N | **9.5x10^15x** |
| Beam-riding demostrado | NUNCA | Requerido | **Brecha cualitativa** |

### Limite termico

Con reflectividad 99.99% y emisividad realista (epsilon=0.10), la vela alcanza **3,240 K** — muy por encima del punto de fusion del silicio (1687 K). Se requieren reflectividades >99.999% no demostradas a intensidades Starshot.

### 5 experimentos propuestos

| ID | Experimento | Costo |
|---|---|---|
| E1 | Reflectividad a alta intensidad (1-100 MW/m2) | ~$0.5M |
| E2 | Beam-riding a escala ng (p<0.01, t-test) | ~$1M |
| E3 | Umbral de runaway termico | ~$0.5M |
| E4 | Aceleracion a escala ug en tunel de vacio | ~$1.5M |
| E5 | Beam-riding a escala ug (p<0.05, binomial) | ~$1.5M |

### Ejecucion rapida

```bash
git clone https://github.com/CienciaEstelar/beam-riding-gap.git
cd beam-riding-gap
pip install tmm numpy scipy
python calculos_paper.py    # Verifica todos los calculos (hash SHA-256 incluido)
```

### Paper complementario

Este paper es la continuacion experimental de [Galaz (2026) — De Alcubierre a la Ingenieria](https://doi.org/10.5281/zenodo.20435538), que reviso 146 referencias y 28 conceptos de propulsion interestelar.

---

## English

Critical gap analysis between available experimental data and Breakthrough Starshot mission requirements.

### What this paper found

A catalog of **6 published experimental measurements** relevant to interstellar laser sails (2020-2026). Main finding: **beam-riding with optical metasurfaces has never been experimentally observed at any mass scale.**

### Quantified gap

| Parameter | Best experimental value | Starshot requirement | Factor |
|---|---|---|---|
| Suspended membrane area | 40x40 um (Michaeli 2025) | 16 m2 | **~10^11x** |
| CW laser intensity | 1.1 MW/m2 | 6.25 GW/m2 | **5.7x10^3x** |
| Measured optical force | 70 fN | ~667 N | **9.5x10^15x** |
| Beam-riding demonstrated | NEVER | Required | **Qualitative gap** |

### Thermal limit

At 99.99% reflectivity and realistic emissivity, the sail reaches **3,240 K** — far above silicon's melting point (1687 K). Reflectivities >99.999% are required but have never been demonstrated at Starshot intensities.

### Companion paper

This is the experimental follow-up to [Galaz (2026) — From Alcubierre to Engineering](https://doi.org/10.5281/zenodo.20435538), which reviewed 146 references and 28 interstellar propulsion concepts.

---

## Autor / Author

**Juan Galaz**

- ORCID: [0009-0007-7474-7560](https://orcid.org/0009-0007-7474-7560)
- GitHub: [CienciaEstelar](https://github.com/CienciaEstelar)
- Email: juan.galaz@proton.me
- Santiago, Chile

## Licencia / License

CC-BY 4.0 — ciencia abierta, libre para investigacion academica.
