import numpy as np

R_edge = 134.1e9 # 134.1 billion light-years
z_edge = 365249.0
z_earendel = 6.2
n = 1.02

d_earendel = R_edge * (z_earendel / z_edge)**(1/n)
print(f"Recalculated Earendel Distance: {d_earendel/1e9:.3f} billion light-years")
print(f"Percentage of edge radius: {(d_earendel / R_edge)*100:.3f}%")

R_edge = 134.1e9 # 134.1 billion light-years
z_edge = 365249.0
z_earendel = 6.2
n = 1.02

ratio = z_earendel / z_edge
exponent = 1.0 / n
factor = ratio ** exponent
d_earendel = R_edge * factor

print(f"Ratio: {ratio}")
print(f"Factor: {factor}")
print(f"Distance in light years: {d_earendel:,.2f}")
print(f"Distance in millions of light years: {d_earendel / 1e6:.3f} million ly")
print(f"Distance in billion light years: {d_earendel / 1e9:.6f} billion ly")