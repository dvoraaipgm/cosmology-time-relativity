import numpy as np
import pandas as pd

R_core_mpc = 52965.56 # Absolute container radius from center (Mpc)
d_earth_mpc = 150.0 # Mpc off-center displacement along apex
mpc_to_ly = 3.26156e6

angles_deg = [0, 45, 90, 135, 180, 225, 270, 315]

results = []
for theta_deg in angles_deg:
    theta = np.radians(theta_deg)
    b_coef = 2.0 * d_earth_mpc * np.cos(theta)
    c_coef = d_earth_mpc**2 - R_core_mpc**2
    discriminant = b_coef**2 - 4 * c_coef
    r_edge = (-b_coef + np.sqrt(discriminant)) / 2.0
    r_edge_ly = r_edge * mpc_to_ly
    
    results.append({
        'Apex_Angle_deg': theta_deg,
        'Distance_to_Edge_Mpc': round(r_edge, 2),
        'Distance_to_Edge_Ly': f"{r_edge_ly:,.2f} ly"
    })

df_45 = pd.DataFrame(results)
print(df_45.to_string(index=False))