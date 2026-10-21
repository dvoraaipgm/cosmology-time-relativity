# =====================================================================
# FILE: setup.py
# DESCRIPTION: Standard PyPI installation setup script for RECO-MM.
# CITATION ID: DOI: 10.5281/zenodo.23105187
# =====================================================================

from setuptools import setup, find_packages

setup(
    name="recomm-cosmology",
    version="2.0.0",
    author="Your Name",
    description="Un-dampened Relational Cosmology & High-Precision Network Timer Stabilization Engine",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.io",
    packages=find_packages(),
    py_modules=[
        "final/pure_kinematic_resolver",
        "final/native_continuum_solver",
        "final/network_timer_ledger/network_sync_bypass",
        "final/blackhole_threshold_solver",
        "final/network_timer_ledger/day_length_solver",
        "final/network_timer_ledger/day_diagram_plotter",
        "final/cosmic_lifecycle_diagram"
    ],
    install_requires=[
        "numpy>=1.20.0",
        "matplotlib>=3.4.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: System :: Networking :: Time Synchronization"
    ],
    python_requires=">=3.8",
)
