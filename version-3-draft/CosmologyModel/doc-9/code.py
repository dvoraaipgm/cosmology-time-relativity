import numpy as np

c = 299792.458 # km/s
alpha = 4200.0 # Mpc
mpc_to_km = 3.085677581e19
seconds_per_year = 31557600.0

# If v(r) = c * exp(r / alpha) [speed increases outward]
# Let's calculate lookback time for an object at distance R from Earth, 
# or integrated from edge to center.
# For v(r) = c * exp(r/alpha), let's check the integral t = int dr / v(r)
# t = int (1 / (c * exp(r/alpha))) dr = (alpha / c) * (1 - exp(-R/alpha))
# Notice that as R -> infinity, lookback time saturates at alpha / c! 
# Let's calculate what that means for our container radius.

R_core_mpc = 52965.56 # Mpc
alpha_km = alpha * mpc_to_km
R_core_km = R_core_mpc * mpc_to_km

# Total transit time with v(r) = c * exp(r/alpha):
# t = (alpha / c) * (1 - exp(-R_core / alpha)) in natural units (where alpha is in light-years or converted properly)
# Let's do it precisely in seconds:
# t_seconds = (alpha_km / c) * (1.0 - np.exp(-R_core_mpc / alpha))
# Wait, let's check dimensions: alpha is in Mpc, R_core is in Mpc. R_core / alpha is dimensionless.
# alpha_km / c has units of seconds (since alpha_km is km, c is km/s).
t_seconds = (alpha_km / c) * (1.0 - np.exp(-R_core_mpc / alpha))
t_years = t_seconds / seconds_per_year

print(f"Saturated lookback time for inverted profile: {t_years:,.2f} years")