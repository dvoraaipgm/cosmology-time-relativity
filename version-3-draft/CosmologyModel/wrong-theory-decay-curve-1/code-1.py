# Let's list and detail the best specific spectral absorption lines / element triplets used in high-res stellar spectroscopy
# for fine-structure constant and atomic clock testing (e.g., Fe I, Mg I/II, Na I, Ca II).
elements = [
    {"Element": "Magnesium (Mg I / Mg II)", "Lines": "Mg I b triplet (~5167, 5173, 5184 Å), Mg II (~2796, 2803 Å)", "Why it's ideal": "Extremely strong resonance lines with high signal-to-noise in solar-type stars; sensitive to electron pressure and fine-structure splitting."},
    {"Element": "Iron (Fe I / Fe II)", "Lines": "Hundreds of lines across optical and infrared (e.g., APOGEE H-band Fe I lines)", "Why it's ideal": "Fe I multi-plets have diverse excitation potentials and Landé g-factors, making them supreme anchors for differential wavelength shifts and 'barcode' consistency."},
    {"Element": "Sodium (Na I D-lines)", "Lines": "Sodium D doublet (~5890, 5896 Å)", "Why it's ideal": "Very sharp doublet spacing that tests fine-structure alpha sensitivity directly in local/intermediate stellar gas."}
]
for el in elements:
    print(f"- **{el['Element']}**: {el['Lines']} -> {el['Why it''s ideal']}")
                                                        
