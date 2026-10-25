import numpy as np

# Let's test standard LambdaCDM luminosity distance roughly at z = 0.5 and z = 1.0
# and see what power-law n in r(z) = R_edge * (z / 365249)**(1/n) or similar matches the curve.
# Actually, let's look at the mapping: z = (365250 - 1) * (r / R_edge)**n
# Solving for r: r = R_edge * (z / 365249)**(1/n)

# In standard cosmology, distance-redshift relation for flat LambdaCDM (Omega_m = 0.3, Omega_lambda = 0.7):
# d_L(0.5) approx 2.9 Gpc, d_L(1.0) approx 6.8 Gpc.
# In the user's model, effective luminosity distance driving the flux attenuation is proportional to r (or r * (1+z)).
# Let's find n such that the predicted dimming matches the Pantheon supernova magnitude residuals.

R_edge = 5.205e15 # light years
z_test = np.array([0.1, 0.3, 0.5, 0.7, 1.0])

# If n = 0.5 (square-root-like potential distribution):
# r = R_edge * (z / 365249)**(1/n) -> r(0.5) will be calculated.
for n in [0.5, 0.75, 1.0, 1.5, 2.0]:
    r_vals = R_edge * (z_test / 365249)**(1/n)
    print(f"For n = {n}: r at z=0.5 is {r_vals[2]:.2e} light years")