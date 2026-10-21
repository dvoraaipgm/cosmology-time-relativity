import numpy as np

# Let's check floating point precision (Double precision / Float64)
# Machine epsilon for float64 is approx 2.22e-16
eps_double = np.finfo(np.float64).eps
eps_single = np.finfo(np.float32).eps

# The offset contribution is ratio = 150 / r
# At what distance r does the ratio equal machine epsilon?
r_double_limit = 150.0 / eps_double
r_single_limit = 150.0 / eps_single

print(f"Float64 epsilon: {eps_double}")
print(f"Distance where offset is lost in Float64 precision: {r_double_limit:e} Mpc")
print(f"Float32 epsilon: {eps_single}")
print(f"Distance where offset is lost in Float32 precision: {r_single_limit:e} Mpc")

# Container radius is ~52,965 Mpc
# Let's check the value of the exponent term at R_container for Float64
alpha = 4200.0
r_earth = 150.0
r_max = 52965.56

val_earth = (r_earth - r_earth) / alpha # 0
val_max = (r_max - r_earth) / alpha

print(f"Exponent at max distance: {val_max:.4f}")
print(f"Exp value at max distance: {np.exp(val_max):.4f}")

# Let's test floating point addition cancellation: r - 150 in float32
r_test = 10000.0 # Mpc
r_f32 = np.float32(r_test)
offset_f32 = np.float32(150.0)

# In float32, does r - 150 lose precision?
sub_f32 = r_f32 - offset_f32
print(f"Original: {r_test}, Float32 sub result: {sub_f32}")

# At what distance r does (r - 150) become indistinguishable from r in float32?
# Float32 has ~7 decimal digits of precision. If r ~ 1.5e7, 150 is around the 7th-8th digit.
for r in [1e4, 1e5, 1e6, 1e7, 1e8]:
    val = np.float32(r) - np.float32(150.0)
    print(f"r = {r:0.0f}: float32(r) - 150 = {val} (diff from r: {r - val})")

    import numpy as np

c_earth = 299792.458 # km/s
alpha = 4200.0 # Mpc
r_earth = 150.0 # Mpc

# Let's calculate the residual "drift" or deviation in 1+z between our off-center model 
# and a hypothetical centered model (r_earth = 0).
# Centered model 1+z_center = exp(r / alpha)
# Off-center model 1+z_ccm = exp((r - r_earth) / alpha) = exp(r/alpha) * exp(-150/alpha) = (1+z_center) * 0.964916...
# The fractional difference (drift percentage) is constant for all distances r!
# Let's check: (z_ccm - z_center) / z_center or the exact speed/redshift ratio delta.

ratio_factor = np.exp(-r_earth / alpha)
percent_diff = (1.0 - ratio_factor) * 100

print(f"Global scale offset factor: {ratio_factor:.6f}")
print(f"Constant fractional drift/shift across all distances: {percent_diff:.4f}%")

# Let's check absolute velocity difference at various distances r
distances = [1000.0, 5000.0, 10000.0, 30000.0, 52965.56] # Mpc

print(f"\n{'Distance r (Mpc)':<18} | {'Center-based v (km/s)':<22} | {'Earth-anchored v (km/s)':<24} | {'Absolute Difference (km/s)':<25}")
print("-" * 95)

for r in distances:
    v_centered = c_earth * np.exp(r / alpha) # assuming c_earth is at center
    v_anchored = c_earth * np.exp((r - r_earth) / alpha) # earth anchored
    # Wait, let's compare earth anchored vs if earth was at center (no offset)
    # If earth was at center, speed at r would be c_earth * exp(r/alpha)
    # With earth at 150 Mpc, speed at r is c_earth * exp((r - 150)/alpha) = v_centered * exp(-150/alpha)
    diff = np.abs(v_anchored - (c_earth * np.exp(r/alpha)))
    print(f"{r:<18.1f} | {c_earth * np.exp(r/alpha):<22.2f} | {v_anchored:<24.2f} | {diff:<25.2f}")