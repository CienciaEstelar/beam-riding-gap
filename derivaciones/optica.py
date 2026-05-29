#!/usr/bin/env python3
"""
OPTICA DE MEMBRANAS — Reflectividad, presion de radiacion, temperatura.
Usa Transfer Matrix Method (tmm) para calculos precisos.
"""

import numpy as np
from .constantes import *

# Intentar importar tmm (Transfer Matrix Method)
try:
    import tmm
    HAS_TMM = True
except ImportError:
    HAS_TMM = False


def reflectividad_tmm(n_list, d_list_nm, lambda_nm=1550, theta_deg=0):
    """
    Calcula reflectividad de un stack multicapa usando TMM.

    Parametros
    ----------
    n_list : list
        Indices de refraccion de cada capa (complejos si hay absorcion).
    d_list_nm : list
        Espesores en nm (inf para capas semi-infinitas).
    lambda_nm : float
        Longitud de onda en nm.
    theta_deg : float
        Angulo de incidencia en grados.

    Retorna
    -------
    dict : {'R_s', 'R_p', 'R_avg', 'T_s', 'T_p', 'A'}
    """
    if not HAS_TMM:
        return reflectividad_analitica(n_list, d_list_nm, lambda_nm)

    theta_rad = np.radians(theta_deg)
    R_s = tmm.coh_tmm('s', n_list, d_list_nm, theta_rad, lambda_nm)['R']
    R_p = tmm.coh_tmm('p', n_list, d_list_nm, theta_rad, lambda_nm)['R']
    T_s = tmm.coh_tmm('s', n_list, d_list_nm, theta_rad, lambda_nm)['T']

    return {
        'R_s': R_s, 'R_p': R_p,
        'R_avg': (R_s + R_p) / 2,
        'T_s': T_s,
        'A': 1 - R_s - T_s if R_s + T_s < 1 else 0
    }


def reflectividad_analitica(n_list, d_list_nm, lambda_nm):
    """Calculo analitico simplificado para una membrana delgada."""
    # Formula de Airy para Fabry-Perot de 1 capa
    n1, n2 = n_list[0], n_list[1]  # medio incidente, membrana
    if isinstance(n2, complex):
        n2_real = n2.real
    else:
        n2_real = n2

    d = d_list_nm[1] if len(d_list_nm) > 1 else 200
    # Reflectividad normal (aproximacion interfaz simple)
    R = ((n1 - n2_real) / (n1 + n2_real))**2
    return {'R_avg': R, 'R_s': R, 'R_p': R, 'T_s': 1 - R, 'A': 0.0}


def presion_radiacion(R, I_W_m2=None):
    """
    Presion de radiacion sobre una vela plana.
    P = (1 + R) * I / c

    Parametros
    ----------
    R : float — reflectividad [0-1]
    I_W_m2 : float — intensidad [W/m2]. Default: Starshot (10 GW/m2)

    Retorna
    -------
    dict con presion [Pa], fuerza [N], aceleracion [m/s2, g]
    """
    if I_W_m2 is None:
        I_W_m2 = I_STARSHOT

    P = (1 + R) * I_W_m2 / C
    F = P * A_SAIL
    a_ms2 = F / (M_SAIL + M_PAYLOAD)
    a_g = a_ms2 / 9.81

    return {
        'presion_Pa': P,
        'fuerza_N': F,
        'aceleracion_m_s2': a_ms2,
        'aceleracion_g': a_g,
        'intensidad_W_m2': I_W_m2,
        'reflectividad': R
    }


def temperatura_equilibrio(R, I_W_m2=None, epsilon=0.1):
    """
    Temperatura de equilibrio radiativo: T = (P_abs / (sigma * epsilon))^(1/4)

    Parametros
    ----------
    R : float — reflectividad [0-1]
    I_W_m2 : float — intensidad [W/m2]
    epsilon : float — emisividad infrarroja [0-1]

    Retorna
    -------
    float — temperatura [K]
    """
    if I_W_m2 is None:
        I_W_m2 = I_STARSHOT

    P_abs = I_W_m2 * (1 - R)
    return (P_abs / (SIGMA_SB * epsilon))**0.25


def brecha_experimental():
    """Calcula la brecha entre experimentos de laboratorio y Starshot."""
    brechas = {
        'area': A_SAIL / EXP_AREA_MAX_M2,
        'intensidad': I_STARSHOT / EXP_INTENSIDAD_MAX_W_M2,
        'fuerza': F_RAD_IDEAL / EXP_FUERZA_MAX_N,
        'reflectividad_requerida': 0.9999,
        'reflectividad_demostrada': EXP_REFLECTIVIDAD,
    }
    return brechas


def tabla_materiales():
    """Tabla comparativa de materiales candidatos para velas Starshot."""
    materiales = [
        {
            'nombre': 'SiN (50nm)', 'n': 2.0, 'k': 1.6e-4,
            'rho_kg_m3': 3100, 'T_limite_K': 1600,
            'R_1550nm': reflectividad_tmm([1.0, N_SIN_1550, 1.0], [float('inf'), 50, float('inf')], 1550)['R_avg'],
            'ref': 'Zwickl 2008, Michaeli 2025'
        },
        {
            'nombre': 'SiN (200nm)', 'n': 2.0, 'k': 1.6e-4,
            'rho_kg_m3': 3100, 'T_limite_K': 1600,
            'R_1550nm': reflectividad_tmm([1.0, N_SIN_1550, 1.0], [float('inf'), 200, float('inf')], 1550)['R_avg'],
            'ref': 'Moura 2018'
        },
        {
            'nombre': 'Si (43nm)', 'n': 3.48, 'k': 1e-7,
            'rho_kg_m3': 2330, 'T_limite_K': 1687,
            'R_1550nm': reflectividad_tmm([1.0, N_SI_1550, 1.0], [float('inf'), 43, float('inf')], 1550)['R_avg'],
            'ref': 'Ilic 2018, Atwater 2024'
        },
        {
            'nombre': 'SiC (200nm)', 'n': 2.6, 'k': 1e-7,
            'rho_kg_m3': 3210, 'T_limite_K': 2000,
            'R_1550nm': reflectividad_tmm([1.0, N_SIC_1064, 1.0], [float('inf'), 200, float('inf')], 1550)['R_avg'],
            'ref': 'Choyke 1997 (datos bulk)'
        },
        {
            'nombre': 'Si-SiO2 N=4', 'n': 'multi', 'k': 'multi',
            'rho_kg_m3': '~2500', 'T_limite_K': 1374,
            'R_1550nm': 0.75,  # Valor aproximado de Ilic 2018
            'ref': 'Ilic 2018 (RAAD=0.014)'
        },
    ]
    return materiales


if __name__ == "__main__":
    print("=== OPTICA DE MEMBRANAS ===")
    # Test membrana SiN 200nm
    r = reflectividad_tmm([1.0, N_SIN_1550, 1.0], [float('inf'), 200, float('inf')], 1550)
    print(f"SiN 200nm @ 1550nm: R_avg = {r['R_avg']*100:.1f}%")

    # Test presion radiacion
    p = presion_radiacion(0.9999)
    print(f"Presion (R=99.99%): {p['presion_Pa']:.1f} Pa, F = {p['fuerza_N']:.1f} N, a = {p['aceleracion_g']:.0f} g")

    # Test temperatura
    T = temperatura_equilibrio(0.9999, I_STARSHOT, 0.1)
    print(f"T_eq (R=99.99%, eps=0.1): {T:.0f} K")

    # Brecha experimental
    b = brecha_experimental()
    print(f"\nBrecha experimental: area {b['area']:.2e}x, intensidad {b['intensidad']:.2e}x, fuerza {b['fuerza']:.2e}x")

    print("\n✅ optica.py listo")
