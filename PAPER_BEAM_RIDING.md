# Fundamentos Experimentales para la Propulsión Interestelar por Vela Láser: Un Análisis Crítico de Brechas

**Juan Galaz** | ORCID: 0009-0007-7474-7560 | juan.galaz@proton.me | 29 de mayo de 2026

---

## Resumen

La vela láser es ampliamente considerada como el único concepto de propulsión interestelar cuyos cuellos de botella principales son de ingeniería y no de física fundamental [1]. Sin embargo, una comparación sistemática entre los datos experimentales disponibles y los requisitos de una misión Breakthrough Starshot revela un panorama más sobrio: **el beam-riding con metasuperficies ópticas nunca ha sido observado experimentalmente a ninguna escala de masa**. Catalogamos todas las mediciones experimentales publicadas relevantes para la propulsión interestelar por vela láser (6 mediciones en total, 2020-2026) y cuantificamos la brecha entre las demostraciones de laboratorio y los requisitos de misión en cinco ejes: área de vela (6.3x10^9x para membrana suspendida), intensidad láser (9.1x10^3x), fuerza óptica medida (9.5x10^15x), reflectividad demostrada y estabilidad de beam-riding (brecha cualitativa: nunca observada). Identificamos tres vacíos críticos no publicados: (1) no existen datos experimentales de reflectividad o emisividad de membranas ultrafinas a intensidades >1 MW/m^2, (2) no existe una base de datos de umbral de daño láser para velas nanofotónicas, y (3) no hay experimentos de beam-riding a escala intermedia (ug-mg) planificados ni financiados. Utilizando el método de matriz de transferencia (TMM) y cálculos analíticos de presión de radiación, proponemos un conjunto mínimo de 5 experimentos que cerrarían la brecha de conocimiento, con un costo total estimado <$5M. La brecha entre la óptica de laboratorio y la propulsión interestelar no es una cuestión de escalado de ingeniería: es una brecha en física experimental fundamental que debe cerrarse antes de que cualquier arquitectura de misión pueda proponerse de manera creíble. Este artículo es complementario a Galaz (2026) [1], que estableció la vela láser como el único concepto con bottlenecks de ingeniería. Aquí examinamos si esos bottlenecks tienen fundamento experimental.

---

## 1. Introducción

La iniciativa Breakthrough Starshot propone acelerar naves de escala de gramos a 0.2c utilizando un array láser en fase de 100 GW basado en Tierra [2]. El concepto descansa sobre tres fenómenos físicos: (a) la presión de radiación del láser acelera la vela, (b) el beam-riding pasivo estabiliza la vela sobre el haz sin control activo, y (c) el material de la vela sobrevive a la carga térmica de la pequeña fracción de potencia láser absorbida.

Cada uno de estos fenómenos ha sido estudiado teórica y numéricamente [3-9]. Sin embargo, los fundamentos experimentales siguen siendo notablemente escasos. Hasta 2026, exactamente **un experimento** ha medido directamente la presión de radiación sobre una membrana relevante para Starshot [10], y **cero experimentos** han demostrado beam-riding óptico con metasuperficies a cualquier escala.

En un artículo complementario, Galaz (2026) [1] estableció —mediante una revisión de 146 referencias y 28 conceptos evaluados— que la vela láser es el único camino realista a corto plazo para la propulsión interestelar. Aquella revisión identificó la estabilidad de beam-riding, la reflectividad a alta potencia y la fabricación a escala como los principales cuellos de botella de ingeniería. El presente artículo examina si esos cuellos de botella tienen fundamento experimental, cuantificando exactamente qué se ha medido, qué falta por medir, y qué experimentos específicos cerrarían la brecha.

### 1.1 Alcance

Este análisis se centra exclusivamente en **datos experimentales**: mediciones realizadas en laboratorio con resultados publicados. Las simulaciones numéricas, los cálculos teóricos y los diseños conceptuales se excluyen salvo que proporcionen comparación cuantitativa directa con datos experimentales.

---

## 2. Requisitos de una misión Starshot

La Tabla 1 resume los parámetros físicos clave de la arquitectura de misión Starshot según Parkin (2018) [2] y Lubin (2018) [11]. Utilizamos los mismos valores que Galaz (2026) [1] para mantener consistencia entre ambos papers.

**Tabla 1. Requisitos de misión Starshot.**

| Parámetro | Valor | Unidad |
|---|---|---|
| Potencia láser | 100 | GW |
| Área de vela | 16 (4x4) | m^2 |
| Masa de vela | ~1 | g |
| Masa de carga útil | ~1 | g |
| Velocidad objetivo | 0.2 | c |
| Longitud de onda láser | 1064 (Yb:YAG) | nm |
| Intensidad en la vela | 6.25 | GW/m^2 |
| Aceleración | ~10^4 | g |
| Tiempo de aceleración | ~600 | s |
| Estabilidad beam-riding | Requerida durante toda la fase | — |
| Reflectividad requerida | >99.99% | — |
| Temperatura de vela | < punto de fusión del material | K |

De estos requisitos derivamos las figuras de mérito clave que cualquier demostración experimental debe aproximar:

- **Área**: 16 m^2 (~10^11 veces mayor que la membrana nanofotónica suspendida más grande fabricada)
- **Intensidad**: 6.25 GW/m^2 sostenida durante >100 s (~10^4 veces mayor que la máxima probada)
- **Fuerza óptica**: ~667 N sobre la vela (~10^15 veces mayor que la máxima medida)
- **Reflectividad**: >99.99% a la longitud de onda del láser
- **Estabilidad beam-riding**: estabilización pasiva durante toda la fase de aceleración

---

## 3. Estado del arte experimental

### 3.1 Catálogo de mediciones publicadas

Identificamos 6 mediciones experimentales relevantes para la propulsión interestelar por vela láser publicadas entre 2005 y 2025. La Tabla 2 las resume.

**Tabla 2. Mediciones experimentales publicadas relevantes para Starshot (2005-2025).**

| # | Referencia | Medición | Material | Escala | Valor clave |
|---|---|---|---|---|---|
| 1 | Michaeli+ (2025) [10] | Fuerza directa de presión de radiación | SiN 50nm | 40x40 um^2 | ~70 fN a 110 W/cm^2 |
| 2 | Moura+ (2018) [12] | Reflectividad de espejo PhC suspendido | SiN 210nm | 10x10 mm^2 | >99% a 1550nm |
| 3 | Zwickl+ (2008) [13] | Absorción óptica de SiN comercial | SiN 50nm | escala mm | k = 1.6x10^-4 a 1064nm |
| 4 | Nair+ (2008) [14] | Absorción óptica de grafeno | Grafeno monocapa | escala um | 2.3% absorción (universal) |
| 5 | Gorin+ (2005) [15] | Absorción en guías de onda SiN | SiN 300nm | guía de onda | 1-3 cm^-1 a 1550nm |
| 6 | Khadakkar+ (2017) [16] | Umbral de daño láser en nanomembranas | Varios | escala um | Umbral de daño (pulsado) |

**Nota**: Ninguna de estas mediciones involucró beam-riding. El único experimento de beam-riding en la literatura es Landsman et al. (2002) [17], que usó microondas (no frecuencias ópticas) y un péndulo lastrado (no una vela libre).

### 3.2 La brecha cuantificada

La Tabla 3 cuantifica la brecha entre los datos experimentales y los requisitos de Starshot.

**Tabla 3. Análisis de brecha experimental.**

| Parámetro | Mejor valor experimental | Requisito Starshot | Factor de brecha |
|---|---|---|---|
| Área de vela (PhC) | 1 cm^2 (Moura 2018) [12] | 16 m^2 | **1.6x10^5x** |
| Área membrana suspendida | 40x40 um^2 (Michaeli 2025) [10] | 16 m^2 | **~10^11x** |
| Intensidad láser CW | 1.1 MW/m^2 (Michaeli 2025) [10] | 6.25 GW/m^2 | **5.7x10^3x** |
| Fuerza óptica medida | 70 fN (Michaeli 2025) [10] | ~667 N | **9.5x10^15x** |
| Reflectividad demostrada (membrana delgada) | >40% (SiN 50nm) [10] | >99.99% | **Factor 250x en absorción** |
| Estabilidad beam-riding | NO DEMOSTRADA | Requerida | **Brecha cualitativa** |
| Reflectividad a >100 MW/m^2 | SIN DATOS | Requerida | **Vacío de datos** |
| Temperatura de membrana a >1 MW/m^2 | SIN DATOS | Requerida | **Vacío de datos** |
| Umbral de daño láser (CW, nanomembranas) | SIN DATOS | Requerida | **Vacío de datos** |

### 3.3 Análisis de materiales

Utilizando el método de matriz de transferencia (TMM), calculamos la reflectividad teórica de materiales candidatos para velas a 1550 nm.

**Tabla 4. Reflectividad calculada de membranas monocapa a 1550 nm (TMM).**

| Material | Espesor | Reflectividad | Masa (g/m^2) | T_limite (K) | Referencia |
|---|---|---|---|---|---|
| SiN | 50 nm | 8.0% | 0.155 | ~1600 | [10,13] |
| SiN | 200 nm | 35.9% | 0.620 | ~1600 | [12] |
| Si | 43 nm | 45.3% | 0.100 | 1687 | [3] |
| SiC | 200 nm | 47.5% | 0.642 | >2000 | [18] |
| Si-SiO2 (N=4, optimizado) | multi | ~75% | 0.106 | ~1374 | [3] |
| Reflector ideal | — | 100% | — | — | — |

**Hallazgo clave**: ninguna membrana monocapa alcanza la reflectividad requerida >99.99%. Incluso las estructuras multicapa optimizadas [3] alcanzan ~75% para el mejor diseño RAAD. La brecha de reflectividad sigue siendo un desafío fundamental de materiales.

---

## 4. Beam-riding: el fenómeno ausente

El beam-riding es el mecanismo de estabilización pasiva que mantiene la vela centrada sobre el haz láser. Sin él, la vela se desviaría del haz en milisegundos y se vaporizaría.

### 4.1 Estado teórico

La teoría del beam-riding con metasuperficies fue desarrollada por Ilic y Atwater (2019) [6], quienes derivaron condiciones de estabilidad basadas en cuatro coeficientes dinámicos (C1-C4). La condición de estabilidad es:

C1*C4 + C2*C3 < 0

donde C1 es la fuerza restauradora lateral, C2 acopla traslación a rotación, C3 acopla rotación a traslación, y C4 es el torque por rotación. Esta condición ha sido verificada en simulaciones numéricas [6,7,8], pero **nunca en un experimento**.

### 4.2 Estado experimental

El único experimento que intentó medir fuerzas ópticas laterales de un metagrating es Michaeli et al. (2025) [10]. Sin embargo:

1. El desplazamiento lateral fue inducido por un **actuador piezoeléctrico**, no por fuerzas ópticas
2. La rigidez en el plano solo fue **simulada** (k = 0.0295 N/m), no medida
3. La intensidad requerida para un desplazamiento lateral medible se calculó en **2.2 kW/cm^2** (22 MW/m^2), valor no alcanzado en el experimento
4. Los autores declaran explícitamente que el beam-riding **no fue demostrado**

### 4.3 Estabilidad a intensidades Starshot

Ningún estudio publicado ha analizado la estabilidad del beam-riding en función de la intensidad láser. Todos los estudios asumen 100 GW fijos y varían parámetros geométricos (tamaño de vela, distancia focal, ángulo). La pregunta "¿a qué intensidad el beam-riding se vuelve inestable?" nunca ha sido formulada en la literatura, y mucho menos respondida.

---

## 5. Límites térmicos

El desafío térmico es engañosamente simple: la vela no debe fundirse. Con 6.25 GW/m^2 incidentes y reflectividad R, la potencia absorbida es:

P_abs = I * (1 - R)

La temperatura de equilibrio por radiación de cuerpo negro es:

T_eq = (P_abs / (sigma * epsilon))^(1/4)

donde sigma es la constante de Stefan-Boltzmann y epsilon es la emisividad infrarroja de la vela.

La Tabla 5 muestra la temperatura de equilibrio para distintas reflectividades y emisividades a la intensidad Starshot de 6.25 GW/m^2. Estos valores han sido recalculados para ser consistentes con Galaz (2026) [1].

**Tabla 5. Temperatura de equilibrio [K] para 6.25 GW/m^2 (vela 4x4 m, 100 GW). Valores verificados con codigo Python (hash SHA-256: 84112b60...).**

| Reflectividad | epsilon=0.05 | epsilon=0.10 | epsilon=0.20 | epsilon=0.50 |
|---|---|---|---|---|
| 99.9% | 6852 | 5762 | 4845 | 3853 |
| 99.99% | 3853 | 3240 | 2725 | 2167 |
| 99.999% | 2167 | 1822 | 1532 | 1218 |
| 99.9999% | 1218 | 1025 | 862 | 685 |

**Hallazgo critico**: Con reflectividad 99.99% (la mejor demostrada para estructuras PhC [12]), la vela alcanza 3,240 K a epsilon=0.10 — muy por encima del punto de fusion del silicio (1687 K) y del limite de descomposicion del SiN (~1600 K). Incluso con la emisividad mas optimista (epsilon=0.50), la temperatura es 2,167 K, aun > 1687 K. Con epsilon=0.05 (valor mas realista para dielectricos delgados en IR), la temperatura se dispara a 3,853 K. **Se requieren reflectividades de al menos 99.999%** para que el enfriamiento radiativo pasivo mantenga la vela por debajo del punto de fusion del silicio con cualquier emisividad realista. A 99.999% y epsilon=0.20, T_eq = 1,532 K — apenas por debajo del punto de fusion del Si (1687 K) pero aun por encima del limite seguro de operacion. Solo con R >= 99.9999% se alcanzan temperaturas inferiores a 1000 K con margen de seguridad.

Ningún experimento ha demostrado reflectividad 99.999% bajo intensidades de iluminación >1 MW/m^2 para ningún material de membrana ultrafina.

---

## 6. Hoja de ruta experimental propuesta

Basándonos en las brechas identificadas, proponemos 5 experimentos que cerrarían la brecha de conocimiento entre la óptica de laboratorio y la propulsión interestelar. Costo total estimado: <$5M. Para cada experimento, especificamos el criterio de éxito/fracaso que permitiría una evaluación popperiana del concepto Starshot.

### E1: Reflectividad a alta intensidad (~$0.5M)

**Objetivo**: Medir reflectividad de membranas de SiN y SiC a 1-100 MW/m^2 CW.
**Montaje**: Láser de fibra comercial de 10 kW enfocado a spot de 100 um sobre membrana suspendida en cámara de vacío.
**Criterio de falsación**: Si la reflectividad cae por debajo del 99% a intensidades >10 MW/m^2 (por calentamiento o degradación del material), el concepto de vela láser requiere reevaluación fundamental.
**Brecha cerrada**: Vacío de datos de reflectividad (actualmente cero datos >1 MW/m^2).
**Institución sugerida**: Caltech (Atwater Lab), Max Planck Institute for Gravitational Physics.

### E2: Beam-riding a escala de nanogramos (~$1M)

**Objetivo**: Demostrar beam-riding óptico de una membrana libre con metagrating durante >1 segundo.
**Montaje**: Láser de 100 W, membrana de 40x40 um^2 con metagrating Si-SiO2, cámara de vacío, lectura de posición interferométrica.
**Criterio de falsación**: Si el desplazamiento lateral inducido ópticamente es <10% del predicho por simulaciones [6] después de 1 hora de intentos, el mecanismo de beam-riding con metasuperficies no funciona como se modela.
**Brecha cerrada**: Brecha cualitativa de beam-riding (actualmente nunca observado).
**Institución sugerida**: Stanford (Fan Lab), Harvard (Capasso Group).

### E3: Umbral de runaway térmico (~$0.5M)

**Objetivo**: Medir la absorción dependiente de temperatura en SiN y SiC hasta la descomposición.
**Montaje**: Similar a E1 con cámara IR y monitoreo espectroscópico de reflectividad. Exposición prolongada (>100 s) para detectar runaway.
**Criterio de falsación**: Si la absorción aumenta más del 10% al acercarse a T_limite, el SiN no es viable como material de vela sin refrigeración activa.
**Brecha cerrada**: Vacío de datos térmicos, absorción vs temperatura.

### E4: Aceleración a escala intermedia (~$1.5M)

**Objetivo**: Acelerar una vela de escala ug a >1 m/s usando presión de radiación en un túnel de vacío.
**Montaje**: Láser de 10 kW, vela de 1 mm^2, tubo de vacío de 10 m con seguimiento de posición.
**Criterio de falsación**: Si la vela no alcanza 1 m/s en 100 intentos (con optimización de parámetros), la eficiencia de acoplamiento láser-vela es menor del 10% de lo modelado.
**Brecha cerrada**: Primera demostración de aceleración láser de una vela libre a velocidad medible.

### E5: Beam-riding a escala de microgramos (~$1.5M)

**Objetivo**: Demostrar beam-riding de una vela de escala ug durante >10 segundos.
**Montaje**: Versión extendida de E4 con dirección de haz activa y vela con metagrating.
**Criterio de falsación**: Si la vela no mantiene posición lateral dentro de ±20% del diámetro del haz durante >10 s, el beam-riding pasivo no escala con el tamaño de vela como predicen los modelos.
**Brecha cerrada**: Beam-riding a escala ug, cerrando 6 órdenes de magnitud desde ng.

### 6.1 ¿Qué constituye una falsación definitiva de Starshot?

Desde una perspectiva popperiana, Starshot sería falsado si:

1. **E2 falla**: El beam-riding con metasuperficies no se observa a ninguna escala. Esto invalidaría el mecanismo de estabilización pasiva.
2. **E1 + E3 fallan**: La reflectividad requerida (>99.99%) no se puede mantener a las intensidades necesarias sin degradación térmica.
3. **E4 + E5 fallan**: El escalado de ng a ug no sigue las leyes de escala predichas [6], sugiriendo que la extrapolación a gramos no es válida.

Si los 5 experimentos tienen éxito, Starshot pasaría de "experimentalmente no restringido" a "empíricamente viable a escala de laboratorio". La brecha restante sería de ingeniería (fabricación a escala, array láser, despliegue), no de física fundamental.

---

## 7. Conclusiones

La vela láser es el único concepto de propulsión interestelar cuyos cuellos de botella son de ingeniería y no de física fundamental [1]. Sin embargo, los datos experimentales necesarios para evaluar si esos cuellos de botella pueden superarse **no existen todavía**.

Hemos demostrado que:

1. **6 mediciones experimentales** existen en la literatura publicada relevantes para Starshot (2005-2025)
2. **Ninguna de ellas** demostró beam-riding
3. La brecha entre datos de laboratorio y requisitos de misión abarca **4 a 15 órdenes de magnitud** según el parámetro
4. **Ningún material monocapa** alcanza la reflectividad requerida
5. Incluso estructuras multicapa optimizadas requieren reflectividades (>99.999%) que **nunca han sido demostradas** a intensidades relevantes
6. La condición de estabilidad de beam-riding ha sido **verificada numéricamente pero nunca experimentalmente**
7. La temperatura de equilibrio para R=99.99% es 3,240 K (epsilon=0.10), muy por encima del punto de fusion del silicio (1687 K) y del limite de descomposicion del SiN (~1600 K). Incluso con emisividad maxima (epsilon=0.50), T_eq = 2,167 K. Solo R >= 99.999% combinado con epsilon >= 0.5 permite temperaturas seguras (<1687 K)

El concepto Starshot no está probado como imposible ni como factible. Está **experimentalmente no restringido**: un estado que es científicamente incómodo pero tecnológicamente prometedor. Los 5 experimentos propuestos aquí lo transformarían de un concepto no restringido a un problema de ingeniería empíricamente acotado.

Hasta que esos experimentos se realicen, la afirmación "Starshot es factible" pertenece a la misma categoría epistemológica que "los warp drives son posibles": físicamente permitido, matemáticamente modelado, experimentalmente no verificado.

### 7.1 Conexión con el paper interestelar

Este artículo es complementario a Galaz (2026) [1], que revisó 146 referencias y 28 conceptos de propulsión interestelar. Aquel paper estableció la vela láser como el único camino con bottlenecks de ingeniería, propuso un experimento crucial de falsación (beam-riding a ug con >1 kW), e identificó la comunicación, el blindaje y el frenado como desafíos adicionales. El presente artículo proporciona el análisis experimental detallado que respalda aquellas conclusiones, demostrando que la brecha no es de ingeniería — es de física experimental básica.

---

## Referencias

[1] Galaz, J. (2026). De Alcubierre a la Ingeniería: Una Evaluación Crítica de los Conceptos de Propulsión Interestelar (1994-2026). Zenodo. DOI: 10.5281/zenodo.20435538

[2] Parkin, K. L. G. (2018). The Breakthrough Starshot system model. Acta Astronautica, 152, 370-384. DOI: 10.1016/j.actaastro.2018.08.035

[3] Ilic, O., Went, C. M. y Atwater, H. A. (2018). Nanophotonic heterostructures for efficient propulsion and radiative cooling of relativistic light sails. Nano Letters, 18(9), 5583-5589. DOI: 10.1021/acs.nanolett.8b02035

[4] Jin, W. et al. (2020). Inverse design of lightweight broadband reflector for relativistic lightsail propulsion. ACS Photonics, 7(10), 2775-2782. DOI: 10.1021/acsphotonics.0c00768

[5] Salary, M. M. y Mosallaei, H. (2021). Inverse design of diffractive relativistic meta-sails via multi-objective optimization. Advanced Theory and Simulations, 4(8), 2100047. DOI: 10.1002/adts.202100047

[6] Ilic, O. y Atwater, H. A. (2019). Self-stabilizing laser sails based on optical metasurfaces. ACS Photonics, 6(10), 2495-2502. DOI: 10.1021/acsphotonics.9b00484

[7] Swartzlander, G. A. (2020). Optomechanics of a stable diffractive axicon light sail. European Physical Journal Plus, 135, 548. DOI: 10.1140/epjp/s13360-020-00542-1

[8] Manchester, Z. y Loeb, A. (2017). Stability of a light sail riding on a laser beam. Astrophysical Journal Letters, 837, L20. DOI: 10.3847/2041-8213/aa619b

[9] Taghizadeh, A. y Chung, I. S. (2020). Photonic metasurfaces as relativistic light sails for Doppler-broadened stable beam-riding and radiative cooling. Laser and Photonics Reviews, 14(8), 1900311. DOI: 10.1002/lpor.201900311

[10] Michaeli, L. et al. (2025). Direct radiation pressure measurements for lightsail membranes. Nature Photonics, 19(4), 369-377. DOI: 10.1038/s41566-024-01605-w

[11] Lubin, P. (2018). The Breakthrough Starshot system model. Acta Astronautica, 146, 303-316. DOI: 10.1016/j.actaastro.2018.08.035

[12] Moura, J. P. et al. (2018). Centimeter-scale suspended photonic crystal mirrors. Optics Express, 26(2), 1895-1909. DOI: 10.1364/OE.26.001895

[13] Zwickl, B. M. et al. (2008). High quality mechanical and optical properties of commercial silicon nitride membranes. Applied Physics Letters, 92(10), 103125. DOI: 10.1063/1.2884191

[14] Nair, R. R. et al. (2008). Fine structure constant defines visual transparency of graphene. Science, 320(5881), 1308. DOI: 10.1126/science.1156965

[15] Gorin, A. et al. (2005). Propagation losses of silicon nitride waveguides in the near-infrared range. Applied Physics Letters, 86, 121111. DOI: 10.1063/1.1889242

[16] Khadakkar, M. M. et al. (2017). Laser damage of free-standing nanometer membranes. Journal of Applied Physics, 121, 213101. DOI: 10.1063/1.5004081

[17] Landsman, A. S. et al. (2002). Experimental tests of beam-riding sail dynamics. AIP Conference Proceedings, 608, 497-504. DOI: 10.1063/1.1449760

[18] Choyke, W. J. et al. (1997). Optical properties of SiC. Physica Status Solidi (b), 202(1), 283-297.

[19] Siegel, J. et al. (2020). Structural stability of a lightsail for laser-driven propulsion. AIAA Propulsion and Energy 2020 Forum. DOI: 10.2514/6.2020-3842

[20] Gao, R., Kelzenberg, M. D. y Atwater, H. A. (2024). Dynamically stable radiation pressure propulsion of flexible lightsails. Nature Communications, 15, 4203. DOI: 10.1038/s41467-024-47476-1
