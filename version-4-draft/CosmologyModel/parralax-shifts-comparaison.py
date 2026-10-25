import numpy as np

# ==========================================
# REAL ASTROMETRIC & SPECTRAL DATA
# ==========================================
c_kms = 299792.458  # Speed of light in km/s
H_0 = 70.0          # Standard Hubble constant (km/s/Mpc) for comparison

stars = {
    "Alpha Centauri": {"parallax_mas": 747.23, "v_r_kms": -22.4},
    "Sirius":         {"parallax_mas": 379.21, "v_r_kms": -7.6},
    "61 Cygni":       {"parallax_mas": 286.06, "v_r_kms": -64.3},
    "Aldebaran":      {"parallax_mas": 19.33,  "v_r_kms": 54.2}
}

print("=" * 85)
print(f"{'Star Name':<16} | {'Parallax Dist (pc)':<18} | {'Measured z (v_r/c)':<20} | {'Hubble z (Expanding)':<20}")
print("-" * 85)

for name, data in stars.items():
    p_arcsec = data["parallax_mas"] / 1000.0
    d_pc = 1.0 / p_arcsec
    
    # Measured spectral shift (Doppler/Kinematic)
    z_measured = data["v_r_kms"] / c_kms
    
    # Naive Hubble expansion shift for comparison (d in Mpc)
    d_mpc = d_pc / 1e6
    z_hubble = (H_0 * d_mpc) / c_kms
    
    print(f"{name:<16} | {d_pc:<18.2f} | {z_measured:<20.2e} | {z_hubble:<20.2e}")

print("=" * 85)