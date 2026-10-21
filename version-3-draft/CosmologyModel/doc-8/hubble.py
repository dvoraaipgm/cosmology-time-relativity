import numpy as np
import pandas as pd

# Apex coordinates of our container off-center vector
l_apex_deg = 264.02
b_apex_deg = 48.25

def angular_separation(l1_deg, b1_deg, l2_deg, b2_deg):
    """Calculates great-circle distance theta between two points in galactic coordinates."""
    l1, b1 = np.radians(l1_deg), np.radians(b1_deg)
    l2, b2 = np.radians(l2_deg), np.radians(b2_deg)
    
    cos_theta = np.sin(b1)*np.sin(b2) + np.cos(b1)*np.cos(b2)*np.cos(l1 - l2)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    return np.degrees(np.arccos(cos_theta))

# Hubble tension anchors
anchors = [
    {"Name": "Large Magellanic Cloud (LMC)", "l": 280.47, "b": -32.89, "Dist_Mpc": 0.05},
    {"Name": "Andromeda Galaxy (M31)", "l": 121.17, "b": -21.57, "Dist_Mpc": 0.78},
    {"Name": "NGC 4258 (M106 Anchor)", "l": 141.81, "b": 67.01, "Dist_Mpc": 7.20}
]

alpha = 4200.0 # Mpc
local_amplitude_kms = 420.0 # Amplitude of velocity dipole anomaly

results = []
for anchor in anchors:
    theta = angular_separation(anchor['l'], anchor['b'], l_apex_deg, b_apex_deg)
    # CCM velocity anomaly projection based on angle theta from apex
    vel_anomaly = local_amplitude_kms * np.cos(np.radians(theta))
    
    results.append({
        'Anchor_Object': anchor['Name'],
        'Distance_Mpc': anchor['Dist_Mpc'],
        'Galactic_l': anchor['l'],
        'Galactic_b': anchor['b'],
        'Apex_Angle_Theta_deg': round(theta, 2),
        'CCM_Velocity_Anomaly_kms': round(vel_anomaly, 2)
    })

df_anchors = pd.DataFrame(results)
print(df_anchors.to_string(index=False))