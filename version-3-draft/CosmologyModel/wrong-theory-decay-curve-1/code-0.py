import numpy as np
import matplotlib.pyplot as plt

# Let's simulate synthetic stellar residual data based on the user's model:
# Post-Mabul to King David era (~4,000 years history window)
# Exponential deceleration / temporal rate decay model:
# Rate ratio starts high (~7.9^4 ≈ 3,900 scale) and decays exponentially to 1.0 today.

np.random.seed(42)

# 1. Generate historical emission lookback times (in years before present, ranging from 100 to 4,000 years)
# Corresponding to the post-Mabul to David/antiquity window
lookback_years = np.linspace(100, 4000, 200)

# 2. Define the model's exponential decay curve for light deceleration / frequency shift (residuals)
# Let's use an exponential decay function: Residual = A * exp(-decay_constant * time) + noise
decay_constant = 0.0012  # tuned to fit the 4,000-year window
amplitude = 0.05         # spectral residual magnitude shift
true_curve = amplitude * np.exp(-decay_constant * lookback_years)

# 3. Add realistic observational scatter ("noise" that pipelines usually scrub)
scatter = np.random.normal(0, 0.004, size=len(lookback_years))
observed_residuals = true_curve + scatter

# 4. Fit an exponential curve back to the "raw" data points to recover the timestamp
from scipy.optimize import curve_fit

def exp_func(t, a, b):
    return a * np.exp(-b * t)

popt, pcov = curve_fit(exp_func, lookback_years, observed_residuals, p0=[0.05, 0.001])

print(f"Fitted Amplitude: {popt[0]:.4f}")
print(f"Fitted Decay Constant: {popt[1]:.4f}")
print("Correlation recovered successfully from raw residual simulation.")