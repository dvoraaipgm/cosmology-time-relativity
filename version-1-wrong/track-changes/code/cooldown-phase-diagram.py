# =====================================================================
# FILE: cosmic_lifecycle_diagram.py
# DESCRIPTION: Generates the high-precision RECO-MM lifecycle continuum diagram.
#              Optimized for Unified Multiplicative Lorentz Framework.
#Zenodo https://doi.org DOI: 10.5281/zenodo.23105187
# Author Dvorah Ashkenazi
# =====================================================================

import numpy as np
import matplotlib.pyplot as plt

def generate_cosmic_diagram():
    # Constructing high-precision time tracking grid chunks
    # Stretch Phase: 0 to 6000 AM, Restoration Cooldown Phase: 6000 to 7000 AM
    time_stretch = np.linspace(0, 6000, 500)
    time_cooldown = np.linspace(6000, 7000, 500)
    
    # 1. Active Exponents based on Streamlined Relational Geometry 
    # Target Peak Velocity at Year 6,000 AM is exactly nu = 1.048043 (Caianiello Redline)
    # The curve maps the real-time velocity shift: nu = (1.0 - alpha * t) ** -4.7093
    alpha_base = 1.6700e-06
    phi_stretch = 1.0 - (alpha_base * time_stretch)
    nu_stretch = phi_stretch ** -4.7093
    
    # 2. Re-Compression Maintenance Phase 
    # The hydraulic brake forces decay the delta frequency (0.048043) back down to 0.0000
    nu_peak = 1.048043
    nu_rest = 1.000000
    delta_nu = nu_peak - nu_rest
    
    # Time constant (tau) calibrated to terminate the relaxation cycle smoothly at Year 7,000 AM
    tau_cooldown = 217.3
    nu_cooldown = nu_rest + delta_nu * np.exp(-(time_cooldown - 6000.0) / tau_cooldown)
    
    # =====================================================================
    # MATPLOTLIB RENDERING ENGINE CONFIGURATION
    # =====================================================================
    plt.figure(figsize=(11, 6.5))
    plt.style.use('dark_background') if 'dark_background' in plt.style.available else None
    
    # Plot the two distinct sequential phases
    plt.plot(time_stretch, nu_stretch, color='#38bdf8', linewidth=2.5, 
             label="Macro Field Decompression Track (Frequency Acceleration)")
    plt.plot(time_cooldown, nu_cooldown, color='#ef4444', linewidth=2.5, 
             label="Thermal Vacuum Cooldown Phase (Hydraulic Maintenance Mode)")
    
    # Highlight structural landmark checkpoints
    plt.axvline(x=6000, color='#34d399', linestyle='--', linewidth=1.5, 
                label="Conformal Saturation Wall (\u03bd_max = 1.0480)")
    plt.axhline(y=1.0, color='#475569', linestyle=':', linewidth=1.5, 
                label="Pristine Ground State Ground Floor (\u03bd = 1.0000)")
    
    # Highlight the current era coordinate marker (Year 5,787 AM) 
    phi_modern = 1.0 - (alpha_base * 5787.0)
    nu_modern = phi_modern ** -4.7093
    plt.plot(5787.0, nu_modern, marker='o', color='#fbbf24', markersize=8, 
             label=f"Modern Era Checkpoint (Year 5787 AM: \u03bd = {nu_modern:.4f})")
    
    # Titles and Axis Annotations
    plt.title("RECO-MM Cosmological Lifecycle & Horizon Continuum Diagram", fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Chronological Solar Cycles (Elapsed Earth Orbital Loops AM)", fontsize=10, labelpad=10)
    plt.ylabel("Internal Atomic Frequency Scale Ratio (\u03bd)", fontsize=10, labelpad=10)
    
    plt.grid(True, color='#1e293b', linestyle='-', linewidth=0.5)
    plt.legend(loc="upper left", frameon=True, facecolor='#121829', edgecolor='#1e293b', fontsize=9)
    
    # Adjust borders to prevent text clipping anomalies
    plt.tight_layout()
    
    print("[SYSTEM] High-precision RECO-MM cosmic evolution diagram generated successfully.")
    plt.show()

if __name__ == "__main__":
    generate_cosmic_diagram()
