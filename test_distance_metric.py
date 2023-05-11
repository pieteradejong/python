from 'python-algos'.distance_metrics import *
import unittest

class TestEuclidean1D(unittest.TestCase):
    def test_calc_distance_1d(self):
        metric1d = Euclidean1D()
        self.assertEqual(metric1d.calc_distance(1, 10), 9, "Expected distance to equal 9")

if __name__ == '__main__':
    unittest.main()
