import numpy as np
import pandas as pd

print("=== VERIFYING NET SPECTROSCOPIC SHIFT ENGINE ===")

c = 299792.458 # km/s
alpha = 4200.0 # Mpc

def compute_net_shift(r_mpc, theta_deg, beta_blue=0.0015):
    rad = np.radians(theta_deg)
    # Global structural redshift component (exponential deceleration/energy decay)
    z_red = np.exp(r_mpc / alpha) - 1.0
    # Directional blueshift relief component (subtracted)
    z_blue = beta_blue * np.cos(rad)
    # Net observed shift
    z_net = z_red - z_blue
    return z_red, z_blue, z_net

angles = [0.0, 90.0, 180.0]
r_test = 50.0

df = pd.DataFrame({'Theta_deg': angles})
df['z_red'], df['z_blue'], df['z_net'] = zip(*df['Theta_deg'].apply(lambda th: compute_net_shift(r_test, th)))
df['Apparent_Velocity_kms'] = df['z_net'] * c

print(df.to_string(index=False))