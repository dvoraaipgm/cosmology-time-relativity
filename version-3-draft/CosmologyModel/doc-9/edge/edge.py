import numpy as np
import pandas as pd

print("=== CLOSED-CONTAINER MODEL: ABSOLUTE PHYSICAL EDGE & GRAVITY ZERO ENGINE ===")

c = 299792.458       # Fundamental baseline speed of light (km/s)
alpha = 4200.0       # Container scale length (Mpc)
mpc_to_ly = 3.26156e6 # Light years per Mpc
mpc_to_km = 3.085677581e19
seconds_per_year = 31557600.0

def calculate_absolute_container_edge():
    """
    Calculates the true physical edge of the container where gravitational 
    potential gradient terminates and light propagation fully stops (v -> 0).
    """
    # Absolute terminal redshift limit where container gravity halts light propagation
    z_wall = c - 1.0 # 299,791.5
    
    # 1. Absolute Wall Radius in Megaparsecs
    r_wall_mpc = alpha * np.log(1.0 + z_wall)
    
    # 2. Absolute Wall Radius in Light Years
    r_wall_ly = r_wall_mpc * mpc_to_ly
    
    # 3. Earth Local Lookback Time to Absolute Wall (Years)
    alpha_km = alpha * mpc_to_km
    t_wall_seconds = (alpha_km * z_wall) / c
    t_wall_years = t_wall_seconds / seconds_per_year
    
    return r_wall_mpc, r_wall_ly, t_wall_years

r_mpc, r_ly, t_years = calculate_absolute_container_edge()

results = pd.DataFrame({
    'Metric': [
        'Absolute Container Wall Radius (Mpc)',
        'Absolute Container Wall Radius (Light Years)',
        'Earth Local Lookback Time to Absolute Wall (Years)'
    ],
    'Calculated Value': [
        f"{r_mpc:,.2f} Mpc",
        f"{r_ly:,.2f} ly",
        f"{t_years:,.2e} years"
    ]
})

print(results.to_string(index=False))