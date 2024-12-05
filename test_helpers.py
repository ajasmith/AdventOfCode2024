import unittest
import numpy
import helpers

file_empty = "test/test_data_empty.txt"
file_numbers = "test/test_data_ints.txt"
file_numbers_irregular = "test/test_data_ints_irregular.txt"
file_chars = "test/test_data_chars.txt"
file_chars_irregular = "test/test_data_chars_irregular.txt"

class test_open_file(unittest.TestCase):
    def test_empty(self):
        actual = helpers.open_file(file_empty)
        expected = []
        self.assertEqual(actual, expected)

    def test_multiline_1(self):
        actual = helpers.open_file(file_numbers)
        expected = [" 1  2  3  4  5", " 6  7  8  9 10", "11 12 13 14 15"]
        self.assertEqual(actual, expected)

    def test_multiline_2(self):
        actual = helpers.open_file(file_chars_irregular)
        expected = ["abcde", "fg h ij", "klmno", "pq", "r", "stuvwxyz"]
        self.assertEqual(actual, expected)

class test_parse_to_int_lists(unittest.TestCase):
    def test_empty(self):
        actual = helpers.parse_to_int_lists(file_empty)
        expected = []
        self.assertEqual(actual, expected)

    def test_valid_regular(self):
        actual = helpers.parse_to_int_lists(file_numbers)
        expected = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
        self.assertEqual(actual, expected)

    def test_valid_irregular(self):
        actual = helpers.parse_to_int_lists(file_numbers_irregular)
        expected = [[1,2,3], [4,5,6,7,8], [], [9]]
        self.assertEqual(actual, expected)

    def test_invalid1(self):
        x = lambda: helpers.parse_to_int_lists(file_chars_irregular)
        self.assertRaises(ValueError, x)

    def test_invalid2(self):
        x = lambda: helpers.parse_to_int_lists(file_chars)
        self.assertRaises(ValueError, x)

class test_parse_to_char_array(unittest.TestCase):
    def test_empty(self):
        actual, w, h = helpers.parse_to_char_array(file_empty)
        expected = numpy.empty((0,0), dtype='|S1')
        self.assertTrue(numpy.array_equal(actual, expected))
        self.assertEqual(w, 0)
        self.assertEqual(h, 0)

    def test_valid(self):
        actual, w, h = helpers.parse_to_char_array(file_chars)
        self.assertEqual(actual[0,0], b'a')
        self.assertEqual(actual[1,0], b'b')
        self.assertEqual(actual[0,1], b'f')
        self.assertEqual(actual[4,2], b'o')
        self.assertEqual(w, 5)
        self.assertEqual(h, 3)

if __name__ == '__main__':
    unittest.main()