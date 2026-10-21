import numpy as np
import pandas as pd

# Container parameters
R_core_mpc = 52965.56 # Absolute container radius from center (Mpc)
# Our off-center displacement d_Earth from the center:
# In our model, our position offset creates the velocity anomaly amplitude v_offset ~ 420 km/s.
# Let's derive displacement d_Earth based on the gradient scale alpha = 4200 Mpc and velocity profile.
# If v(r) = c * exp(-r/alpha), our displacement from center r_earth can be estimated where v(r_earth)/c matches our offset factor.
# Or let's define our offset as a fraction of the container radius or scale length alpha.
# For instance, if our displacement is delta_r = alpha * (v_offset / c) or similar geometric offset.
# Let's compute a precise offset: say d_Earth = 120.0 Mpc along the apex vector.
d_earth_mpc = 150.0 # Mpc off-center displacement along the apex vector

# 4 Key Directions from Earth:
# 1. Toward Apex (theta = 0)
# 2. Toward Anti-Apex (theta = 180)
# 3. Perpendicular 1 (theta = 90)
# 4. Perpendicular 2 (theta = 270 / or opposite transverse)

directions = [
    {"Direction": "Toward Apex (Shortest Edge)", "theta_deg": 0.0, "l": 264.02, "b": 48.25},
    {"Direction": "Perpendicular Transverse (East)", "theta_deg": 90.0, "l": 174.02, "b": 0.00},
    {"Direction": "Toward Anti-Apex (Longest Edge)", "theta_deg": 180.0, "l": 84.02, "b": -48.25},
    {"Direction": "Perpendicular Transverse (West)", "theta_deg": 270.0, "l": 354.02, "b": 0.00}
]

mpc_to_ly = 3.26156e6

results = []
for d in directions:
    theta = np.radians(d['theta_deg'])
    # Using law of cosines or vector offset for a sphere of radius R:
    # R^2 = d_earth^2 + r_edge^2 - 2 * d_earth * r_edge * cos(180 - theta)  [if measuring from center]
    # More simply, distance from Earth r_edge(theta) satisfies:
    # r_edge^2 + 2 * d_earth * cos(theta) * r_edge - (R_core^2 - d_earth^2) = 0  (approx for small offset)
    # Exact vector intersection with sphere of radius R_core:
    # Let container center be origin (0,0,0). Earth is at vector E = (d_earth, 0, 0) along apex.
    # Ray from Earth in direction theta: P(r) = E + r * u(theta)
    # Magnitude of P(r) equals R_core: |E + r*u|^2 = R_core^2
    # d_earth^2 + r^2 + 2 * d_earth * r * cos(theta) = R_core^2
    # r^2 + [2 * d_earth * cos(theta)] * r + [d_earth^2 - R_core^2] = 0
    
    b_coef = 2.0 * d_earth_mpc * np.cos(theta)
    c_coef = d_earth_mpc**2 - R_core_mpc**2
    
    # Solve quadratic equation: r^2 + b_coef * r + c_coef = 0
    discriminant = b_coef**2 - 4 * c_coef
    r_edge = (-b_coef + np.sqrt(discriminant)) / 2.0
    
    r_edge_ly = r_edge * mpc_to_ly
    
    results.append({
        'Direction': d['Direction'],
        'Galactic_l': d['l'],
        'Galactic_b': d['b'],
        'Distance_to_Edge_Mpc': round(r_edge, 2),
        'Distance_to_Edge_Ly': f"{r_edge_ly:,.2f} ly"
    })

df_edge = pd.DataFrame(results)
print(df_edge.to_string(index=False))