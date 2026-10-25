import numpy as np

# Physical constants
c = 2.99792458e8      # m/s
G = 6.67430e-11       # m^3 kg^-1 s^-2
S_max = 365250.0
ln_S = np.log(S_max)

# Cosmic densities (kg/m^3)
# 1. Critical density of the universe
rho_crit = 8.53e-27   
# 2. Total matter density (Omega_m ~ 0.3 * rho_crit)
rho_matter = 0.3 * rho_crit
# 3. Approximate uniform density used earlier (approx 1 atom/m^3 -> ~1.67e-27 kg/m^3)
rho_baryon = 1.67e-27

def calculate_edge(rho):
    # R_edge^2 = (3 * ln(S_max) * c^2) / (4 * pi * G * rho)
    R_edge_squared = (3.0 * ln_S * c**2) / (4.0 * np.PI * G * rho)
    R_edge_meters = np.sqrt(R_edge_squared)
    # Convert meters to light years (1 light year = 9.461e15 meters)
    ly_per_meter = 1.0 / 9.46073e15
    R_edge_ly = R_edge_meters * ly_per_meter
    return R_edge_ly

print(f"Edge using Critical Density ({rho_crit:.2e} kg/m^3): {calculate_edge(rho_crit):.3e} light-years")
print(f"Edge using Matter Density ({rho_matter:.2e} kg/m^3): {calculate_edge(rho_matter):.3e} light-years")
print(f"Edge using Baryon Density ({rho_baryon:.2e} kg/m^3): {calculate_edge(rho_baryon):.3e} light-years")


c = 2.99792458e8      # m/s
G = 6.67430e-11       # m^3 kg^-1 s^-2
S_max = 365250.0
ln_S = np.log(S_max)

rho_crit = 8.53e-27   
rho_matter = 0.3 * rho_crit
rho_baryon = 1.67e-27

def calculate_edge(rho):
    R_edge_squared = (3.0 * ln_S * c**2) / (4.0 * np.pi * G * rho)
    R_edge_meters = np.sqrt(R_edge_squared)
    ly_per_meter = 1.0 / 9.46073e15
    return R_edge_meters * ly_per_meter

print(f"Edge using Critical Density ({rho_crit:.2e} kg/m^3): {calculate_edge(rho_crit):.3e} light-years")
print(f"Edge using Matter Density ({rho_matter:.2e} kg/m^3): {calculate_edge(rho_matter):.3e} light-years")
print(f"Edge using Baryon Density ({rho_baryon:.2e} kg/m^3): {calculate_edge(rho_baryon):.3e} light-years")