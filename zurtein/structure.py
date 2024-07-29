"""
Work in progress
This package can only read PDB files from this source:
- AlphaFold prediction (including AFDB)
- ESMFold prediction (including ESM Atlas)
- **A lot of PDB files from RCSB might not work**
"""

from .sequence import Sequence

import numpy as np


class Structure:
    def __init__(self, sequence: str, coordinates: np.array):
        # coordinate: (N, 3) array
        assert len(sequence) == coordinates.shape[0], "Sequence and coordinates must have the same length"
        self.sequence = sequence
        self.coordinates = coordinates


class Topology:
    def __init__(self, topology: str):
        pass


class Coordinates:
    def __init__(self, coordinates: str):
        pass



