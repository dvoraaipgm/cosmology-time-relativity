import numpy as np
import pandas as pd

print("=== CLOSED-CONTAINER MODEL: PARALLAX GRADIENT & OFFSET ENGINE ===")

# Constants
AU_pc = 1.0 / 206265.0  # 1 AU in parsecs
alpha_local = 4200.0 * 1000.0  # Converted to parsecs (4.2 Gpc)
gaia_offset_uas = 29.0  # Micro-arcseconds baseline zero-point offset seen in Gaia DR3

def calculate_container_parallax(distance_pc, theta_deg):
    """
    Calculates the container-corrected parallax incorporating light-speed 
    decay scaling and the off-center observer's directional dipole offset.
    """
    rad = np.radians(theta_deg)
    
    # 1. Standard trigonometric parallax (arcseconds)
    pi_standard = (1.0 / distance_pc) if distance_pc > 0 else 0.0
    pi_standard_mas = pi_standard * 1000.0 # milli-arcseconds
    
    # 2. Gravitational gradient compression multiplier over parsec scales
    compression_factor = np.exp(distance_pc / alpha_local)
    
    # 3. Off-center directional astrometric shift (in micro-arcseconds, converted to mas)
    # Cosine projection models looking toward/away from the container core axis
    vector_shift_mas = (gaia_offset_uas * np.cos(rad)) / 1000.0
    
    # 4. Net Container Parallax
    pi_net_mas = (pi_standard_mas * compression_factor) - vector_shift_mas
    
    # Corresponding container-corrected distance
    d_net = 1.0 / (pi_net_mas / 1000.0) if pi_net_mas > 0 else np.nan
    
    return pi_standard_mas, pi_net_mas, d_net

# Test across different stellar distances and viewing angles
test_cases = [
    {"Name": "Nearby Star (Alpha Centauri)", "Dist_pc": 1.34, "Theta": 0.0},
    {"Name": "Intermediate Disk Star", "Dist_pc": 100.0, "Theta": 90.0},
    {"Name": "Outer Arm Star (Toward Core)", "Dist_pc": 1000.0, "Theta": 0.0},
    {"Name": "Outer Arm Star (Toward Anticenter)", "Dist_pc": 1000.0, "Theta": 180.0}
]

results = []
for case in test_cases:
    std, net, d_calc = calculate_container_parallax(case["Dist_pc"], case["Theta"])
    results.append({
        'Target': case['Name'],
        'Distance_pc': case['Dist_pc'],
        'Viewing_Angle_deg': case['Theta'],
        'Standard_Parallax_mas': round(std, 4),
        'Container_Net_Parallax_mas': round(net, 4),
        'Implied_Container_Dist_pc': round(d_calc, 2)
    })

df_parallax = pd.DataFrame(results)
print(df_parallax.to_string(index=False))