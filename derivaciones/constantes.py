#!/usr/bin/env python3
"""
CONSTANTES FISICAS — Beam-Riding Gap Analysis
===============================================
Todas las constantes utilizadas en el paper, trazables a CODATA 2022.

Autor: Juan Galaz | Fecha: 2026-05-29
"""

import numpy as np
from scipy import constants as _const

# --- Fundamentales [CODATA 2022] ---
C: float = _const.c                     # Velocidad de la luz [m/s] EXACTA
G: float = _const.G                     # Gravitacion [m3/(kg.s2)] +-2.2e-5
H_PLANCK: float = _const.h              # Planck [J.s] EXACTA
HBAR: float = _const.hbar               # Planck reducida [J.s] EXACTA
SIGMA_SB: float = _const.sigma          # Stefan-Boltzmann [W/(m2.K4)] EXACTA
K_B: float = _const.k                   # Boltzmann [J/K] EXACTA

# --- Unidades ---
AU: float = _const.au                   # [m]
YR_S: float = _const.Julian_year        # [s]
DAY_S: float = 86400.0                  # [s]
LY: float = C * YR_S                    # [m]
MEV: float = 1.602176634e-13            # MeV -> J
GEV: float = 1.602176634e-10            # GeV -> J

# --- Starshot (Parkin 2018) ---
P_LASER: float = 100e9                  # 100 GW
A_SAIL: float = 10.0                    # 10 m2
M_SAIL: float = 1e-3                    # 1 g (solo vela)
M_PAYLOAD: float = 1e-3                # 1 g (starchip)
V_TARGET_C: float = 0.2                 # 0.2c
LAMBDA_LASER: float = 1550e-9           # 1.55 um (NIR, Starshot)
DISTANCIA_AL: float = 4.37              # Alpha Centauri [ly]

# --- Constantes derivadas ---
I_STARSHOT: float = P_LASER / A_SAIL    # Intensidad [W/m2]
F_RAD_IDEAL: float = 2 * P_LASER / C    # Fuerza radiacion ideal [N]
P_RAD_IDEAL: float = F_RAD_IDEAL / A_SAIL  # Presion radiacion [Pa]

# --- Material properties (literatura) ---
# SiN (Zwickl 2008, Michaeli 2025)
N_SIN_1064: complex = 2.0 + 0.000016j   # indice complejo @ 1064nm
N_SIN_1550: complex = 2.0 + 0.000005j   # @ 1550nm
RHO_SIN: float = 3100.0                 # kg/m3
T_DECOMP_SIN: float = 1600.0            # K (estimado, 1% perdida masa en 1000s)

# SiC (Choyke 1997)
N_SIC_1064: complex = 2.6 + 0.0j        # virtualmente transparente
RHO_SIC: float = 3210.0                 # kg/m3

# Si (Ilic 2018)
N_SI_1550: complex = 3.48 + 0.0j
RHO_SI: float = 2330.0                  # kg/m3
T_MELT_SI: float = 1687.0               # K

# SiO2 (Ilic 2018)
N_SIO2_1550: complex = 1.44 + 0.0j
RHO_SIO2: float = 2200.0                # kg/m3

# --- Brecha experimental (Michaeli 2025) ---
EXP_AREA_MAX_M2: float = 1.6e-9        # 40x40 um2 = 1.6e-9 m2
EXP_FUERZA_MAX_N: float = 70e-15       # 70 fN
EXP_INTENSIDAD_MAX_W_M2: float = 1.1e6 # 110 W/cm2 = 1.1 MW/m2
EXP_REFLECTIVIDAD: float = 0.40        # >40% @ 514nm SiN 50nm


def imprimir_constantes() -> None:
    """Imprime todas las constantes para verificacion."""
    print("=" * 55)
    print("  CONSTANTES — Beam-Riding Gap Analysis")
    print("=" * 55)
    print(f"  c       = {C:.6e} m/s")
    print(f"  sigma   = {SIGMA_SB:.6e} W/(m2.K4)")
    print(f"  P_laser = {P_LASER/1e9:.0f} GW")
    print(f"  A_sail  = {A_SAIL} m2")
    print(f"  I_Starshot = {I_STARSHOT/1e9:.2f} GW/m2")
    print(f"  P_rad (ideal) = {P_RAD_IDEAL:.2f} Pa")
    print(f"  F_rad (ideal) = {F_RAD_IDEAL:.2f} N")
    print(f"  Brecha area: {A_SAIL/EXP_AREA_MAX_M2:.2e}x")
    print(f"  Brecha intensidad: {I_STARSHOT/EXP_INTENSIDAD_MAX_W_M2:.2e}x")
    print(f"  Brecha fuerza: {F_RAD_IDEAL/EXP_FUERZA_MAX_N:.2e}x")
    print("=" * 55)


if __name__ == "__main__":
    imprimir_constantes()
