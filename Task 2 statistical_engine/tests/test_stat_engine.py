import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    
    def test_mean(self):
        engine = StatEngine([10, 20, 30])
        self.assertEqual(engine.getmean(), 20)

    def test_median_odd(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.getmedian(), 3)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.getmedian(), 2.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_standard_deviation(self):
        engine = StatEngine([1, 2, 3])
        # We don't check exact value, just that it runs without error
        self.assertGreater(engine.getstandarddeviation(), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)