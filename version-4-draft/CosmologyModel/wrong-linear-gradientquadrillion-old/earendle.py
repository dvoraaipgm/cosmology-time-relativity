import numpy as np

R_edge = 5.205e15 # light years
z_edge = 365249.0
z_earendel = 6.2
n = 1.02

d_earendel_model = R_edge * (z_earendel / z_edge)**(1/n)
print(f"Distance of z = 6.2 in model: {d_earendel_model:.3e} light years ({d_earendel_model/1e9:.2f} billion light years)")