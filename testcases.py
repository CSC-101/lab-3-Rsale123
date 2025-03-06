import unittest
import functions


class Lab3TestCases(unittest.TestCase):

    # Testing the double function
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)

    # Tests for groups_of_3
    def test_exact_groups(self):
        result = functions.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, result)

    def test_incomplete_group(self):
        result = functions.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8])
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(expected, result)

    def test_empty_list(self):
        result = functions.groups_of_3([])
        expected = []
        self.assertEqual(expected, result)

    def test_single_element(self):
        result = functions.groups_of_3([1])
        expected = [[1]]
        self.assertEqual(expected, result)

    def test_two_elements(self):
        result = functions.groups_of_3([1, 2])
        expected = [[1, 2]]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
