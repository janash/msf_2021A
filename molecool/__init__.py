"""
molecool
A python package for analyzing and visualizing xyz and pdb files
"""

# Add imports here
from .functions import *
from .measure import calculate_distance, calculate_angle
from .io import open_pdb, open_xyz, write_xyz
from .molecule import build_bond_list
from .visualize import draw_molecule, bond_histogram

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
