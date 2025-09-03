import unittest

from algorithms.src.array_equilibrium import find_array_equilibrium


class MyTestCase(unittest.TestCase):
    def test_find_array_equilibrium(self):
        index = find_array_equilibrium([1, 2, 3, 2, 1])
        self.assertEqual(index, 2)

    def test_find_array_equilibrium_no_index(self):
        index = find_array_equilibrium([1, 2, 3, 2, 1, 1])
        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()
