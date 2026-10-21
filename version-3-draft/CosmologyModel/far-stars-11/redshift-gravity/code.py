import numpy as np

def calculate_redshift_gravity_distance(d_mainstream, redshift):
    """
    Calculates true distance where the gravitational deceleration 
    factor is directly derived from observed astronomical redshift (z).
    """
    # Using the redshift-dependent gravitational damping factor
    d_true = d_mainstream / (1.0 + redshift)
    return d_true

# Landmarks with mainstream distances and observed redshifts (z)
cosmic_data = {
    "Proxima Centauri": {"d": 4.2, "z": 0.0},
    "Orion Nebula": {"d": 1344.0, "z": 0.0},
    "Andromeda Galaxy": {"d": 2500000.0, "z": -0.001},
    "Earendel (Furthest Star)": {"d": 28000000000.0, "z": 6.2}
}

print("--- REDSHIFT-COUPLED GRAVITY DISTANCE MODEL ---")
for name, data in cosmic_data.items():
    d_true = calculate_redshift_gravity_distance(data["d"], data["z"])
    print(f"Target: {name}")
    print(f"  -> Mainstream Distance: {data['d']:,.1f} ly (Redshift z = {data['z']})")
    print(f"  -> Gravitational Redshift-Adjusted Distance: {d_true:,.2f} light-years\n")