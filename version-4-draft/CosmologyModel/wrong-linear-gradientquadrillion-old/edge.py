import numpy as np
from scipy.integrate import quad

R_edge = 5.205e15 # light years
r_star = 1.0e15   # 1 quadrillion light years
n = 1.02
S_target = 365250.0

def S_func(r):
    return 1.0 + (S_target - 1.0) * (r / R_edge)**n

# Travel time in years (since c = 1 ly/yr, t = int S(r) dr from 0 to r_star)
travel_time, _ = quad(S_func, 0, r_star)

print(f"Euclidean distance: {r_star:.2e} light years")
print(f"Coordinate travel time: {travel_time:.3e} years")
print(f"Ratio (travel time / distance): {travel_time / r_star:.2f}")