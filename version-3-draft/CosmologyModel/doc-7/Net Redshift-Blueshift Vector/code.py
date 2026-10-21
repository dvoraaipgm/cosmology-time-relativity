import numpy as np
import pandas as pd

print("=== CLOSED-CONTAINER MODEL: CORRECTED REDSHIFT-BLUESHIFT VECTOR ENGINE ===")

c = 299792.458 # km/s (Baseline speed of light)
alpha = 4200.0 # Mpc container decay scale length

def calculate_container_shift(r_mpc, theta_deg, local_amplitude=0.0020):
    """
    Calculates net spectroscopic shift by taking the global exponential 
    distance redshift and subtracting the local directional vector component 
    based on the observer's off-center position in the growing gravitational gradient.
    """
    rad = np.radians(theta_deg)
    
    # 1. Global structural redshift from exponential light speed decay
    z_global = np.exp(r_mpc / alpha) - 1.0
    
    # 2. Local directional gradient vector projected by viewing angle theta
    z_local_vector = local_amplitude * np.cos(rad)
    
    # 3. Net Shift: Global redshift minus the local vector component
    z_net = z_global - z_local_vector
    
    # Corresponding apparent velocity
    v_apparent = z_net * c
    
    return z_global, z_local_vector, z_net, v_apparent

# Test across key viewing angles at a standard test distance (r = 50 Mpc)
test_distance = 50.0 # Mpc
angles = [0.0, 60.0, 90.0, 120.0, 180.0]

results = []
for th in angles:
    zg, zl, zn, va = calculate_container_shift(test_distance, th)
    results.append({
        'Viewing_Angle_deg': th,
        'Global_Redshift (zg)': round(zg, 5),
        'Local_Vector (zl)': round(zl, 5),
        'Net_Shift (zn)': round(zn, 5),
        'Apparent_Velocity_kms': round(va, 2)
    })

df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))