"""
Unit tests for DTQEM v5.0
Run with: python -m unittest test_dtqem_v5.py
"""

import unittest
import numpy as np
from dtqem_v5 import DTQEM_v5, QuantumState

class TestDTQEMv5(unittest.TestCase):
    def setUp(self):
        self.model = DTQEM_v5(t_obs=1e-6, gamma0=1000, omega_eV=0.025)

    def test_visibility_range(self):
        V = self.model.visibility(180, 0)
        self.assertAlmostEqual(V, 1.0, places=4)
        V0 = self.model.visibility(0, 300)
        self.assertAlmostEqual(V0, 0.0, places=4)

    def test_complementarity(self):
        comp = self.model.complementarity(180, 0)
        self.assertLessEqual(comp, 1.0 + 1e-10)
        comp = self.model.complementarity(90, 300)
        self.assertLessEqual(comp, 1.0 + 1e-10)

    def test_distinguishability_orthogonal(self):
        D = self.model.distinguishability(180, 0)
        self.assertAlmostEqual(D, 0.0, places=4)  # pure Bell: D=0

    def test_bloch_vector_norm(self):
        x,y,z = self.model.bloch(90, 0)
        self.assertLessEqual(x*x + y*y + z*z, 1.0 + 1e-10)

if __name__ == '__main__':
    unittest.main()
