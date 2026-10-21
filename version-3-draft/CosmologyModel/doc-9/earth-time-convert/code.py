import numpy as np
import pandas as pd

print("=== EARTH LOCAL LOOKBACK TIME & GRAVITATIONAL DELAY ENGINE ===")

c = 299792.458 # km/s
alpha = 4200.0 # Mpc

# Conversion factors
mpc_to_km = 3.085677581e19 # km per Mpc
seconds_per_year = 31557600.0 # seconds in a standard Julian year

def calculate_earth_lookback_time(z_list):
    results = []
    for z in z_list:
        # Radial distance in Mpc: r = alpha * ln(1 + z)
        r_mpc = alpha * np.log(1.0 + z)
        
        # Earth lookback time formula: t = (alpha * z) / c
        # Convert alpha from Mpc to km: alpha_km = alpha * mpc_to_km
        alpha_km = alpha * mpc_to_km
        time_seconds = (alpha_km * z) / c
        time_years = time_seconds / seconds_per_year
        
        results.append({
            'Redshift (z)': z,
            'Distance_Mpc': round(r_mpc, 2),
            'Earth_Lookback_Time_Years': f"{time_years:,.2f}"
        })
    return pd.DataFrame(results)

# Test across key cosmic milestones
milestones_z = [0.05, 0.5, 1.0, 2.0, 7.5, 15.0]
df_time = calculate_earth_lookback_time(milestones_z)

print(df_time.to_string(index=False))