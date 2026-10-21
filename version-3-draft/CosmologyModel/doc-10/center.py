import numpy as np

c_center = 299792.458 # km/s (Center reference)
alpha = 4200.0 # Mpc
r_earth = 150.0 # Mpc

v_earth = c_center * np.exp(r_earth / alpha)
print(f"If Center = c ({c_center:,.3f} km/s), then Earth Speed = {v_earth:,.3f} km/s")
print(f"Difference: {v_earth - c_center:,.3f} km/s faster at Earth")