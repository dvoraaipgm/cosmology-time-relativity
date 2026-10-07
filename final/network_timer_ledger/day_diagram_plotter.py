# =====================================================================
# FILE: day_diagram_plotter.py
# DESCRIPTION: Plots the 3 day-length curves across the universal continuum.
# CITATION ID: DOI: 10.5281/zenodo.23105187
# =====================================================================

import numpy as np
import matplotlib.pyplot as plt

def generate_rotational_diagram():
    # Constructing time tracking grid from Year 0 AM up to the 6,000 AM ceiling
    time_spectrum = np.linspace(0, 6000, 1000)
    
    h_initial, h_present, beta_hubble = 67.40, 73.50, 8.9093
    phi_present = (h_initial / h_present) ** (1.0 / beta_hubble)
    alpha = (1.0 - phi_present) / 5787.0

    day_terrestrial_curve = []
    day_space_curve = []
    spin_velocity_curve = []

    for t in time_spectrum:
        phi_t = 1.0 - (alpha * t)
        
        # Calculate the 3 metrics across the continuum [Vavryčuk (2025)]
        dt = 24.0 * (phi_t ** -8.9593) * (phi_present ** 8.9593)
        ds = 24.0 * (phi_t ** -4.25)
        sv = (1.0 / (phi_t ** 4.20)) - 1.0  # Percentage speed increase
        
        day_terrestrial_curve.append(dt)
        day_space_curve.append(ds)
        spin_velocity_curve.append(sv * 100.0)

    # =====================================================================
    # MATPLOTLIB DARK-MODE RENDERING ENGINE
    # =====================================================================
    plt.figure(figsize=(11, 6.5))
    plt.style.use('dark_background') if 'dark_background' in plt.style.available else None
    
    # Plot day duration metrics on primary axis
    ax1 = plt.gca()
    ax1.plot(time_spectrum, day_terrestrial_curve, color='#34d399', linewidth=2.5, 
             label="1. Local Atomic Clock Day (Standard Hours/Rotation)")
    ax1.plot(time_spectrum, day_space_curve, color='#38bdf8', linewidth=2.5, 
             label="2. Cosmic Space Clock Day (Invariant Hours/Rotation)")
    ax1.set_xlabel("Chronological Universal Timeline Coordinate (AM)", fontsize=10, labelpad=10)
    ax1.set_ylabel("Measured Day Length Duration (Hours)", fontsize=10, labelpad=10)
    ax1.tick_params(axis='y', labelcolor='#38bdf8')
    
    # Create secondary axis to map the raw physical spin acceleration velocity percentage
    ax2 = ax1.twinx()
    ax2.plot(time_spectrum, spin_velocity_curve, color='#ef4444', linewidth=2, linestyle=':',
             label="3. Physical Earth Spin Velocity Increase (%)")
    ax2.set_ylabel("Net Planetary Spin Velocity Increase (%)", color='#ef4444', fontsize=10, labelpad=10)
    ax2.tick_params(axis='y', labelcolor='#ef4444')

    # Mark the current era coordinate snapshot (Year 5,787 AM)
    ax1.plot(5787.0, 24.0, marker='o', color='#fbbf24', markersize=8, 
             label="Modern Era Checkpoint (Year 5787 AM: Locked at 24.00h)")

    plt.title("RECO-MM: Tri-Metric Rotational Day-Length Continuum Diagram", fontsize=12, fontweight='bold', pad=15)
    ax1.grid(True, color='#1e293b', linestyle='-', linewidth=0.5)
    
    # Collect and display unified legends cleanly
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=True, facecolor='#121829', edgecolor='#1e293b', fontsize=9)
    
    plt.tight_layout()
    print("[SYSTEM] Tri-metric rotational timeline diagram generated successfully.")
    plt.show()

if __name__ == "__main__":
    generate_rotational_diagram()
