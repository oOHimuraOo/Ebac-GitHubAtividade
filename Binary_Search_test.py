import unittest
from array import array

from binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        array = [12,23,34,45,56,67,78,89,90]
        find = 45

        result = binary_search(array,find,0,len(array)-1)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
