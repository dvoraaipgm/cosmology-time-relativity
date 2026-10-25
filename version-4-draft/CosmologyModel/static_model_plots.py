import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. SETUP & CONSTANTS
# ==========================================
c_kms = 299792.458       # Speed of light in km/s
R_EDGE = 134.1           # Cavity radius in Gly
S_MAX = 365250.0         # Maximum proper metric scaling factor at edge
N_EXP = 1.02             # Non-linear gradient exponent
R_SOLAR_OFFSET = 3.82    # Milky Way offset in Gly

# Set dark mode style for scientific presentation
plt.style.use('dark_background')
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# ==========================================
# 2. PLOT 1: MACRO-COSMOLOGICAL SCALING PROFILE S(r)
# ==========================================
r_vals = np.linspace(0, R_EDGE, 500)
S_vals = 1.0 + (S_MAX - 1.0) * (r_vals / R_EDGE)**N_EXP

axes[0].plot(r_vals, S_vals, color='#3b82f6', linewidth=2.5, label='Master Scaling $S(r)$')
axes[0].axvline(R_SOLAR_OFFSET, color='#10b981', linestyle='--', linewidth=1.5, 
                label=f'Milky Way Position ($r_\\odot = {R_SOLAR_OFFSET}$ Gly)')
axes[0].set_title('Macro-Cavity Master Metric Profile $S(r)$', fontsize=12, fontweight='bold', color='white')
axes[0].set_xlabel('Coordinate Radius $r$ (Gly)', fontsize=10)
axes[0].set_ylabel('Metric Scaling Factor $S(r)$', fontsize=10)
axes[0].grid(True, linestyle=':', alpha=0.4)
axes[0].legend(frameon=True, facecolor='#111827', edgecolor='none')

# ==========================================
# 3. PLOT 2: GALACTIC ORBIT IN S_MW POTENTIAL
# ==========================================
R_0 = 8.2        # Solar reference radius in kpc
q_z = 0.75       # Disk flattening factor
alpha = 0.15     # Non-linear gradient exponent
R_cut = 30.0     # Outer disk cutoff in kpc

def milky_way_metric(R, z):
    r_ell = np.maximum(np.sqrt(R**2 + (z / q_z)**2), 1e-4)
    return 1.0 + (15.0 - 1.0) * (r_ell / R_0)**alpha * np.exp(-r_ell / R_cut)

# Symplectic orbital integration in galactic units (R in kpc, z in kpc)
dt_myr = 0.02
steps = 3000
R_orb = np.zeros(steps)
z_orb = np.zeros(steps)
R_orb[0], z_orb[0] = 8.2, 0.05
v_R = 0.0
v_z = 15.0 / 977.8      # converted to kpc/Myr
v_phi = 220.0 / 977.8   # converted to kpc/Myr

for i in range(1, steps):
    eps = 1e-3
    S = milky_way_metric(R_orb[i-1], z_orb[i-1])
    ds_dr = (milky_way_metric(R_orb[i-1] + eps, z_orb[i-1]) - milky_way_metric(R_orb[i-1] - eps, z_orb[i-1])) / (2 * eps)
    ds_dz = (milky_way_metric(R_orb[i-1], z_orb[i-1] + eps) - milky_way_metric(R_orb[i-1], z_orb[i-1] - eps)) / (2 * eps)
    
    acc_conv = 1.022e-6  # unit conversion factor
    a_R = (- (c_kms**2 / S) * ds_dr + ((v_phi * 977.8)**2 / R_orb[i-1])) * acc_conv
    a_z = (- (c_kms**2 / S) * ds_dz) * acc_conv
    
    v_R += a_R * dt_myr
    v_z += a_z * dt_myr
    R_orb[i] = R_orb[i-1] + v_R * dt_myr
    z_orb[i] = z_orb[i-1] + v_z * dt_myr

axes[1].plot(R_orb, z_orb, color='#8b5cf6', linewidth=1.5, label='Stellar Epicyclic Orbit ($S_{MW}$)')
axes[1].set_title('Local Galactic Orbit in $S_{MW}(R,z)$ Potential', fontsize=12, fontweight='bold', color='white')
axes[1].set_xlabel('Galactocentric Radius $R$ (kpc)', fontsize=10)
axes[1].set_ylabel('Vertical Height $z$ (kpc)', fontsize=10)
axes[1].grid(True, linestyle=':', alpha=0.4)
axes[1].legend(frameon=True, facecolor='#111827', edgecolor='none')

# ==========================================
# 4. FINALIZE & SAVE PLOT
# ==========================================
plt.tight_layout()
output_filename = 'static_gravitational_well_analysis.png'
plt.savefig(output_filename, dpi=300)
print(f"Successfully generated and saved visualization as '{output_filename}'")
plt.show()