import unittest
from more_math.algebra import Algebra


class TestAlgebra(unittest.TestCase):
    def test_comb(self):
        combination = Algebra().comb(6, 3)
        self.assertEqual(combination, 20)


if __name__ == '__main__':
    unittest.main()
