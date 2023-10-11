# test_main.py

import unittest
from main import reverse_string

class TestMain(unittest.TestCase):
    """
    A test case for the `reverse_string` function.

    This test case checks the functionality of the `reverse_string` function by
    testing it with a sample input string "hello world". The expected output
    for this input is "dlrow olleh".
    """
    def test_reverse_string(self):
        """
        Test the reverse_string function
        by passing in a string and checking if the output is the reverse of the input.
        """
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    # generate a set of inputs to test the function with
    def test_reverse_string_with_set(self):
        """
        Test the reverse_string function
        by passing in a set of strings and checking if the output is the reverse of the input.
        """
        test_strings = {"hello world", "racecar", "python", "madam", "a", ""}
        for test_string in test_strings:
            self.assertEqual(reverse_string(test_string), test_string[::-1])


if __name__ == '__main__':
    unittest.main()
