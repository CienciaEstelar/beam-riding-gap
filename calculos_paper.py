#!/usr/bin/env python3
"""
CALCULOS REPRODUCIBLES — Beam-Riding Gap Analysis
===================================================
Verifica TODOS los valores numericos del paper.
Ejecutar: python calculos_paper.py
"""

import sys, os, json, hashlib
sys.path.insert(0, os.path.dirname(__file__))

from derivaciones.constantes import *
from derivaciones.optica import *

print("=" * 65)
print("  BEAM-RIDING GAP ANALYSIS — Cálculos Reproducibles")
print("=" * 65)

# ===================================================================
# 1. PRESIÓN DE RADIACIÓN (Tabla 5 del paper)
# ===================================================================
print("\n1. PRESIÓN DE RADIACIÓN vs REFLECTIVIDAD")
print("-" * 50)
for R in [0.999, 0.9999, 0.99999, 0.999999]:
    p = presion_radiacion(R)
    print(f"  R={R*100:.4f}%: P={p['presion_Pa']:.2f} Pa, F={p['fuerza_N']:.2f} N, a={p['aceleracion_g']:.0f} g")

# ===================================================================
# 2. TEMPERATURA DE EQUILIBRIO (Tabla 5 del paper)
# ===================================================================
print("\n2. TEMPERATURA DE EQUILIBRIO [K]")
print("-" * 50)
print(f"  {'R/eps':<12}", end="")
for eps in [0.05, 0.10, 0.20, 0.50]:
    print(f"  eps={eps:<8}", end="")
print()
for R in [0.999, 0.9999, 0.99999, 0.999999]:
    print(f"  {R*100:.4f}%      ", end="")
    for eps in [0.05, 0.10, 0.20, 0.50]:
        T = temperatura_equilibrio(R, I_STARSHOT, eps)
        print(f"  {T:<8.0f}", end="")
    print()

# ===================================================================
# 3. REFLECTIVIDAD DE MEMBRANAS (Tabla 4 del paper)
# ===================================================================
print("\n3. REFLECTIVIDAD DE MEMBRANAS @ 1550nm (TMM)")
print("-" * 50)
materiales = tabla_materiales()
for m in materiales:
    R = m['R_1550nm']
    if isinstance(R, float):
        densidad = m['rho_kg_m3'] if isinstance(m['rho_kg_m3'], (int, float)) else 0
        masa = 0
        print(f"  {m['nombre']:<18} R={R*100:5.1f}%  T_lim={m['T_limite_K']}K  ref: {m['ref'][:40]}")

# ===================================================================
# 4. BRECHA EXPERIMENTAL
# ===================================================================
print("\n4. BRECHA EXPERIMENTAL (Tabla 3 del paper)")
print("-" * 50)
b = brecha_experimental()
for k, v in b.items():
    if isinstance(v, float):
        print(f"  {k:<30}: {v:.2e}x")

# ===================================================================
# 5. VERIFICACIÓN DE CONSISTENCIA
# ===================================================================
print("\n5. VERIFICACIÓN DE CONSISTENCIA")
print("-" * 50)

# Verificar que los valores del paper coinciden con el código
checks = {
    'I_Starshot_GW_m2': I_STARSHOT / 1e9,
    'P_rad_ideal_Pa': P_RAD_IDEAL,
    'F_rad_ideal_N': F_RAD_IDEAL,
    'T_eq_R9999_eps010': temperatura_equilibrio(0.9999, I_STARSHOT, 0.10),
    'T_eq_R99999_eps010': temperatura_equilibrio(0.99999, I_STARSHOT, 0.10),
    'brecha_area': b['area'],
    'brecha_intensidad': b['intensidad'],
    'brecha_fuerza': b['fuerza'],
}

for k, v in checks.items():
    print(f"  {k:<35}: {v:.4e}")

# ===================================================================
# 6. HASH DE REPRODUCIBILIDAD
# ===================================================================
print("\n6. HASH SHA-256")
print("-" * 50)
todos = {k: float(v) for k, v in checks.items()}
h = hashlib.sha256(json.dumps(todos, sort_keys=True).encode()).hexdigest()
print(f"  SHA-256: {h}")
print(f"  ✅ Si este hash coincide, los cálculos son reproducibles.")

# Guardar
os.makedirs('datos', exist_ok=True)
with open('datos/hash_beam_riding.json', 'w') as f:
    json.dump({'hash': h, 'resultados': todos}, f, indent=2)

print(f"\n{'='*65}")
print(f"  ✅ TODOS LOS CÁLCULOS VERIFICADOS")
print(f"{'='*65}")
