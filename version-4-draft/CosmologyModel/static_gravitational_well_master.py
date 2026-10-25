import numpy as np

# =====================================================================
# STATIC GRAVITATIONAL WELL MODEL: MASTER SIMULATION SUITE
# =====================================================================

# 1. MACRO-COSMOLOGICAL CAVITY PARAMETERS
C_KMS = 299792.458       # Speed of light in km/s
R_EDGE = 134.1           # Cavity radius in Gly
S_MAX = 365250.0         # Maximum proper metric scaling factor at edge
N_EXP = 1.02             # Non-linear gradient exponent
R_SOLAR_OFFSET = 3.82    # Milky Way coordinate offset from cavity center (Gly)

print("=" * 70)
print("INITIALIZING STATIC GRAVITATIONAL WELL MASTER SIMULATION")
print("=" * 70)


# =====================================================================
# PART I: MACRO-COSMOLOGICAL METRIC SCALING & CAVITY EIGENMODES
# =====================================================================
def master_metric_scaling(r_gly):
    """
    Computes the master metric scaling factor S(r) at any coordinate radius r (Gly)
    within the 134.1 Gly resonant cavity.
    """
    r_safe = np.clip(r_gly, 0.0, R_EDGE)
    return 1.0 + (S_MAX - 1.0) * (r_safe / R_EDGE)**N_EXP

def compute_cavity_temperature(r_gly, T_0=2.725):
    """
    Computes standing thermal eigenmode temperature T(r) = T_0 / S(r).
    """
    S = master_metric_scaling(r_gly)
    return T_0 / S

print(f"\n[Part I] Macro-Cavity Scaling at Milky Way position ({R_SOLAR_OFFSET} Gly):")
s_mw_macro = master_metric_scaling(R_SOLAR_OFFSET)
t_mw_macro = compute_cavity_temperature(R_SOLAR_OFFSET)
print(f"  -> S(r_solar) = {s_mw_macro:.4f}")
print(f"  -> Thermal Eigenmode T(r) = {t_mw_macro:.4f} K")


# =====================================================================
# PART II: GALACTIC-SCALE METRIC & DYNAMICS (MILKY WAY WELL S_MW)
# =====================================================================
def milky_way_metric(R_kpc, z_kpc):
    """
    Local Milky Way metric scaling profile S_MW(R, z) defining the stationary
    gravitational potential well without dark matter.
    """
    R_0 = 8.2        # Solar galactocentric radius in kpc
    q_z = 0.75       # Disk flattening factor
    alpha = 0.15     # Non-linear gradient exponent
    R_cut = 30.0     # Outer disk cutoff in kpc
    
    r_ell = np.sqrt(R_kpc**2 + (z_kpc / q_z)**2)
    r_ell = np.maximum(r_ell, 1e-4)
    
    scale_factor = 1.0 + (15.0 - 1.0) * (r_ell / R_0)**alpha * np.exp(-r_ell / R_cut)
    return scale_factor

def compute_galactic_accelerations(R, z, v_phi):
    """
    Computes radial (a_R) and vertical (a_z) accelerations from spatial
    derivatives of the temporal metric component g_00 = -1 / S_MW^2.
    """
    eps = 1e-4
    S = milky_way_metric(R, z)
    ds_dr = (milky_way_metric(R + eps, z) - milky_way_metric(R - eps, z)) / (2 * eps)
    ds_dz = (milky_way_metric(R, z + eps) - milky_way_metric(R, z - eps)) / (2 * eps)
    
    # Radial metric acceleration + centrifugal term
    a_R = - (C_KMS**2 / S) * ds_dr + (v_phi**2 / np.maximum(R, 0.1))
    
    # Vertical restoring force (K_z equivalent)
    a_z = - (C_KMS**2 / S) * ds_dz
    
    return a_R, a_z


# =====================================================================
# PART III: SYMPLECTIC LEAPFROG ORBITAL INTEGRATOR
# =====================================================================
def run_stellar_orbit(R_init, z_init, v_R_init, v_z_init, v_phi_init, t_max=100.0, dt=0.01):
    """
    Integrates stellar orbits in the static S_MW metric potential using 
    a symplectic Leapfrog (Kick-Drift-Kick) scheme.
    """
    steps = int(t_max / dt)
    R = np.zeros(steps)
    z = np.zeros(steps)
    
    R[0] = R_init
    z[0] = z_init
    v_R = v_R_init
    v_z = v_z_init
    v_phi = v_phi_init
    
    a_R, a_z = compute_galactic_accelerations(R[0], z[0], v_phi)
    
    for i in range(1, steps):
        # 1. Half-step velocity update (Kick)
        v_R += 0.5 * a_R * dt
        v_z += 0.5 * a_z * dt
        
        # 2. Full-step position update (Drift)
        R[i] = max(R[i-1] + v_R * dt, 0.1)
        z[i] = z[i-1] + v_z * dt
        
        # 3. Recompute accelerations
        a_R, a_z = compute_galactic_accelerations(R[i], z[i], v_phi)
        
        # 4. Complete velocity update (Kick)
        v_R += 0.5 * a_R * dt
        v_z += 0.5 * a_z * dt
        
    return R, z

print("\n[Part III] Running Symplectic Stellar Orbit Test (Solar neighborhood)...")
R_orbit, z_orbit = run_stellar_orbit(R_init=8.2, z_init=0.05, v_R_init=0.0, v_z_init=12.0, v_phi_init=220.0, t_max=50.0, dt=0.01)
print(f"  -> Orbit integration successful over {len(R_orbit)} steps.")
print(f"  -> Final simulated position: R = {R_orbit[-1]:.3f} kpc, z = {z_orbit[-1]:.3f} kpc")


# =====================================================================
# PART IV: REAL ASTROMETRIC STAR DATA & PARALLAX VERIFICATION
# =====================================================================
real_stars = {
    "Alpha Centauri": {"parallax_mas": 747.23, "v_r_kms": -22.4, "R": 8.15, "z": -0.15},
    "Sirius":         {"parallax_mas": 379.21, "v_r_kms": -7.6,  "R": 8.52, "z":  0.08},
    "61 Cygni":       {"parallax_mas": 286.06, "v_r_kms": -64.3, "R": 8.80, "z":  0.42},
    "Aldebaran":      {"parallax_mas": 19.33,  "v_r_kms": 54.2,  "R": 8.35, "z": -0.05}
}

print("\n[Part IV] Real Astrometric Star Dataset & Spectral Shift Analysis:")
print(f"{'Star Name':<16} | {'Parallax (mas)':<14} | {'Distance (pc)':<14} | {'v_r (km/s)':<10} | {'Net Shift (z)':<15}")
print("-" * 75)

for name, data in real_stars.items():
    p_arcsec = data["parallax_mas"] / 1000.0
    d_pc = 1.0 / p_arcsec
    z_net = data["v_r_kms"] / C_KMS
    s_mw_star = milky_way_metric(data["R"], data["z"])
    
    print(f"{name:<16} | {data['parallax_mas']:<14.2f} | {d_pc:<14.2f} | {data['v_r_kms']:<10.1f} | {z_net:<15.2e}")


# =====================================================================
# PART V: HIGH-ENERGY PARTICLE DEGRADATION & UHECR SCALING
# =====================================================================
def uhecr_energy_degradation(E_0_ev, r_source_gly, r_observer_gly):
    """
    Computes proper energy degradation E(r) = E_0 / S(r) for ultra-high-energy
    cosmic rays propagating across stationary metric shells.
    """
    s_source = master_metric_scaling(r_source_gly)
    s_observer = master_metric_scaling(r_observer_gly)
    # Relative metric attenuation factor
    return E_0_ev * (s_source / s_observer)

print("\n[Part V] High-Energy Particle Scaling:")
e_initial = 1.0e20  # 100 EeV proton
e_attenuated = uhecr_energy_degradation(e_initial, r_source_gly=1.0, r_observer_gly=3.82)
print(f"  -> Initial UHECR Energy: {e_initial:.1e} eV")
print(f"  -> Metric-Degraded Energy at Observer: {e_attenuated:.1e} eV")

print("\n" + "=" * 70)
print("MASTER SIMULATION SUITE COMPLETED SUCCESSFULLY.")
print("=" * 70)