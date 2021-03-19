from unittest import TestCase

import numpy as np
from scipy.interpolate import interp1d


class DebugTest(TestCase):

    def test_numpy(self):
        a = np.array([4, 4, 4])
        b = np.ones(3) * 4
        self.assertTrue(np.all(a == b))

    def test_scipy(self):
        x = [1, 3]
        y = [1, 3]
        f = interp1d(x, y)
        v = f(2)
        self.assertEqual(v, 2)
