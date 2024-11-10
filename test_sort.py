import unittest
from sort import quicksort  # Import the quicksort function from the sort module

class TestQuicksort(unittest.TestCase):

    def test_unsorted_array(self):
        self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])

if __name__ == "__main__":
    unittest.main()
