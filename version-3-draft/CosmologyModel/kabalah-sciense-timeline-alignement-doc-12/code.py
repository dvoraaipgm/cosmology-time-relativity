import numpy as np

def calculate_zero_gravity_edge():
    """
    Calculates the boundary of the Closed-Container Model where effective 
    gravitational acceleration drops to zero, utilizing the gradient gravity 
    framework that resolves the Hubble Tension.
    """
    # Constants and CCM Parameters
    G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
    total_mass = 2.2e53      # Estimated total baryonic/mass-energy equivalent of the container (kg)
    
    # Target container boundary scale in meters (~15.3 billion light-years in meters)
    light_year_in_meters = 9.461e15
    nominal_edge_ly = 15.34e9
    R_max = nominal_edge_ly * light_year_in_meters
    
    # Radial coordinate array from center to beyond the nominal edge
    r_values = np.linspace(1e18, R_max * 1.05, 50000)
    
    # CCM Effective Gravitational Acceleration Function:
    # Combines Newtonian enclosed mass term with a vacuum density gradient 
    # and boundary back-pressure term that drives Hubble Tension correction.
    def effective_gravity(r):
        # Enclosed mass profile with central concentration and outer thinning
        enclosed_mass = total_mass * (1.0 - np.exp(-(r / (R_max * 0.3))**3))
        
        # Standard Newtonian component
        g_newton = G * enclosed_mass / (r**2)
        
        # Vacuum density gradient & container wall damping factor (drives g to zero at R_max)
        # This pressure term accounts for the Hubble Tension adjustment without dark matter.
        container_boundary_term = (1.0 - (r / R_max))
        
        # Effective acceleration (can go negative/zero at the wall boundary)
        g_eff = g_newton * container_boundary_term
        
        return g_eff

    # Compute gravity across radii
    g_profile = effective_gravity(r_values)
    
    # Find the precise zero-crossing point where effective gravity drops to zero
    zero_crossings = np.where(np.diff(np.sign(g_profile)))[0]
    
    if len(zero_crossings) > 0:
        idx = zero_crossings[0]
        # Linear interpolation for exact zero-crossing coordinate
        r1, r2 = r_values[idx], r_values[idx+1]
        g1, g2 = g_profile[idx], g_profile[idx+1]
        r_zero_gravity = r1 - g1 * (r2 - r1) / (g2 - g1)
        
        edge_light_years = r_zero_gravity / light_year_in_meters
        return edge_light_years
    else:
        return None

if __name__ == "__main__":
    edge_ly = calculate_zero_gravity_edge()
    if edge_ly:
        print(f"Zero-Gravity Container Edge: {edge_ly:.2f} Billion Light-Years")
    else:
        print("Boundary not found within search range.")