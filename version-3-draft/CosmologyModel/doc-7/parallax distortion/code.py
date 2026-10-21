import numpy as np
import pandas as pd

print("=== MILKY WAY OFF-CENTER PARALLAX DISTORTION ENGINE ===")

def milky_way_parallax_distortion(star_gal_l_deg, star_gal_b_deg, d_sun_pc, offset_magnitude_uas=29.0):
    """
    Calculates parallax distortion for Milky Way stars based on our off-center position.
    l: Galactic longitude (0 deg is toward Galactic Center)
    b: Galactic latitude
    d_sun_pc: Distance from the Sun to the star in parsecs
    """
    l_rad = np.radians(star_gal_l_deg)
    b_rad = np.radians(star_gal_b_deg)
    
    # 1. Standard trigonometric parallax (mas)
    pi_std_mas = (1.0 / d_sun_pc) * 1000.0 if d_sun_pc > 0 else 0.0
    
    # 2. Off-center geometric projection vector inside the Milky Way disk
    # Scaling factor increases with distance across the container gradient
    disk_gradient_factor = 1.0 + (d_sun_pc / 50000.0) 
    
    # Distortion offset in milli-arcseconds (converting micro-arcseconds uas to mas)
    distortion_mas = (offset_magnitude_uas * np.cos(l_rad) * np.cos(b_rad) * disk_gradient_factor) / 1000.0
    
    # 3. Net Distorted Parallax
    pi_distorted_mas = pi_std_mas - distortion_mas
    
    # Apparent distance shift (%)
    apparent_distance_pc = 1.0 / (pi_distorted_mas / 1000.0) if pi_distorted_mas > 0 else np.nan
    distance_error_percent = ((apparent_distance_pc - d_sun_pc) / d_sun_pc) * 100.0
    
    return pi_std_mas, distortion_mas, pi_distorted_mas, distance_error_percent

# Test Milky Way target positions at d = 2000 pc across different Galactic longitudes
test_mw_stars = [
    {"Target": "Toward Galactic Center (Core)", "l": 0.0, "b": 0.0, "dist": 2000.0},
    {"Target": "Perpendicular Disk (l = 90)", "l": 90.0, "b": 0.0, "dist": 2000.0},
    {"Target": "Toward Galactic Anticenter", "l": 180.0, "b": 0.0, "dist": 2000.0},
    {"Target": "Perpendicular Disk (l = 270)", "l": 270.0, "b": 0.0, "dist": 2000.0},
]

results = []
for star in test_mw_stars:
    std, dist_val, net, err = milky_way_parallax_distortion(star['l'], star['b'], star['dist'])
    results.append({
        'Target_Position': star['Target'],
        'Galactic_Long (l)': star['l'],
        'True_Dist_pc': star['dist'],
        'Standard_Parallax_mas': round(std, 4),
        'Distortion_Offset_mas': round(dist_val, 4),
        'Net_Parallax_mas': round(net, 4),
        'Distance_Shift_%': round(err, 3)
    })

df_mw = pd.DataFrame(results)
print(df_mw.to_string(index=False))