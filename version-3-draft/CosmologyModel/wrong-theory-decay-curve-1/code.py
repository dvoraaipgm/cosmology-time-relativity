import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def analyze_sdss_residuals(fits_file_path):
    # Open the SDSS/APOGEE spectrum FITS file
    with fits.open(fits_file_path) as hdul:
        # Extract flux, model template, wavelength grid, and metadata
        flux = hdul[1].data['FLUX']
        model = hdul[1].data['MODEL']
        wavelength = hdul[1].data['WAVELENGTH']
        
        # 1. Isolate raw pre-calibration residuals (the scrubbed "noise/jitter")
        raw_residuals = flux - model
        
        # 2. Strip standard Doppler/radial velocity shifts
        # (Remove standard kinematic baseline adjustments)
        v_helio = hdul[0].header.get('VHELIO', 0.0)
        corrected_wavelength = wavelength * (1.0 - (v_helio / 299792.458))
        
        # 3. Calculate lookback distance / tier grouping
        # (Grouping stars by distance brackets corresponding to our historical window)
        distance_ly = hdul[0].header.get('DIST_LY', 1000.0) # Estimated distance in light-years
        
        return corrected_wavelength, raw_residuals, distance_ly

# Example execution loop for a sample of intermediate-distance stars
# results = [analyze_sdss_residuals(f) for f in stellar_file_list]