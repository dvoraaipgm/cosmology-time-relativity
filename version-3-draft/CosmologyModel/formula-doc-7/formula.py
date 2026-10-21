import numpy as np
import pandas as pd

# Constants
c = 299792.458 # km/s (Speed of light baseline)
alpha = 4200.0 # Characteristic container decay length in Mpc

# 1. The Core Mechanical Engine: v(r) = c * exp(-r / alpha)
def light_speed_propagation(r_mpc):
    return c * np.exp(-r_mpc / alpha)

# 2. Derive redshift from velocity decay: 1 + z = c / v(r) = exp(r / alpha)
def derived_redshift(r_mpc):
    return np.exp(r_mpc / alpha) - 1.0

# Test real empirical distance benchmarks against our core engine
benchmarks = pd.DataFrame({
    'Scale': ['Local (Milky Way Disk)', 'Intermediate (Megamasers)', 'Global (Planck CMB Horizon)'],
    'Distance_Mpc': [10.0, 130.0, 10000.0]
})

benchmarks['Propagation_Speed_kms'] = light_speed_propagation(benchmarks['Distance_Mpc'])
benchmarks['Speed_Deficit_Percent'] = (1.0 - (benchmarks['Propagation_Speed_kms'] / c)) * 100
benchmarks['Derived_Redshift_z'] = derived_redshift(benchmarks['Distance_Mpc'])

print("=== CLOSED-CONTAINER ENGINE TEST: v(r) = c * exp(-r / alpha) ===")
print(benchmarks.to_string(index=False))