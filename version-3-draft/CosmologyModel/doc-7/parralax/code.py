import numpy as np
import pandas as pd

print("=== CLOSE MILKY WAY STARS PARALLAX VERIFICATION ===")

def close_star_parallax(name, dist_pc, l_deg, b_deg, uas_offset=29.0):
    """
    Evaluates parallax for stars very close to the Sun within the Milky Way disk.
    """
    l_rad = np.radians(l_deg)
    b_rad = np.radians(b_deg)
    
    # Standard trigonometric parallax (mas)
    pi_std = (1.0 / dist_pc) * 1000.0
    
    # Local container vector shift for nearby scales (in micro-arcseconds converted to mas)
    vector_shift_mas = (uas_offset * np.cos(l_rad) * np.cos(b_rad)) / 1000.0
    
    pi_net = pi_std - vector_shift_mas
    diff_uas = (pi_std - pi_net) * 1000.0
    
    return pi_std, pi_net, diff_uas

# Benchmark nearby stars (Distance in parsecs, Galactic Longitude l, Latitude b)
nearby_stars = [
    {"Name": "Alpha Centauri", "Dist": 1.34, "l": 315.74, "b": -0.72},
    {"Name": "Barnard's Star", "Dist": 1.82, "l": 32.79, "b": 14.04},
    {"Name": "Sirius", "Dist": 2.64, "l": 227.23, "b": -8.89},
    {"Name": "Wolf 359", "Dist": 2.39, "l": 233.17, "b": 69.34},
    {"Name": "Lalande 21185", "Dist": 2.54, "l": 174.85, "b": 56.81}
]

results = []
for star in nearby_stars:
    std, net, diff = close_star_parallax(star['Name'], star['Dist'], star['l'], star['b'])
    results.append({
        'Star': star['Name'],
        'Distance_pc': star['Dist'],
        'Standard_Parallax_mas': round(std, 4),
        'Container_Parallax_mas': round(net, 4),
        'Vector_Shift_uas': round(diff, 2)
    })

df_close = pd.DataFrame(results)
print(df_close.to_string(index=False))