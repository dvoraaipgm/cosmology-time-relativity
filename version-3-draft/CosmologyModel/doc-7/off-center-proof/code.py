import numpy as np
import pandas as pd

print("=== 360-DEGREE ALL-SKY DIPOLE ANISOTROPY ENGINE ===")

def simulate_all_sky_dipole(num_points=360, amplitude_kms=420.0):
    """
    Simulates apparent velocity anomalies across 360 degrees of Galactic Longitude (l)
    to prove off-center container positioning.
    """
    # Generate full 360 degree scan (Galactic Longitude l from 0 to 360)
    l_deg = np.linspace(0, 360, num_points)
    l_rad = np.radians(l_deg)
    
    # Assuming Galactic latitude b = 0 for the disk plane
    b_rad = 0.0 
    
    # Dipole vector projection based on off-center position
    # l = 0 deg (Toward Core): Maximum negative vector (resistance/compression)
    # l = 180 deg (Anticenter): Maximum positive vector (easing/expansion relief)
    velocity_anomaly = amplitude_kms * np.cos(l_rad) * np.cos(b_rad)
    
    df = pd.DataFrame({
        'Galactic_Longitude_deg': l_deg,
        'Apparent_Velocity_Anomaly_kms': velocity_anomaly
    })
    
    return df

# Run the simulation
sky_scan = simulate_all_sky_dipole(num_points=9) # Sample every 45 degrees for display
sky_scan['Apparent_Velocity_Anomaly_kms'] = sky_scan['Apparent_Velocity_Anomaly_kms'].round(2)

print(sky_scan.to_string(index=False))