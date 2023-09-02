from cascading_palindrome_ZUR000226WSG import Palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_is_palindrome_true(self):
        # test cases where words are palindromes
        self.assertTrue(Palindrome.is_palindrome(self, "racecar"))
        self.assertTrue(Palindrome.is_palindrome(self, "madam"))
        self.assertTrue(Palindrome.is_palindrome(self, "deed"))
        self.assertTrue(Palindrome.is_palindrome(self, "civic"))
        self.assertTrue(Palindrome.is_palindrome(self, "level"))

    def test_is_palindrome_false(self):
        # test cases where words are not palindromes
        self.assertFalse(Palindrome.is_palindrome(self, "python"))
        self.assertFalse(Palindrome.is_palindrome(self, "language"))
        self.assertFalse(Palindrome.is_palindrome(self, "hello"))
        self.assertFalse(Palindrome.is_palindrome(self, "world"))
        self.assertFalse(Palindrome.is_palindrome(self, "programming"))

    def test_find_palindromes(self):
        # test case where for a string with substring of palindromes
        input_str: str = "racecar radar hello world level deed civic"
        palindrome_finder: Palindrome = Palindrome(input_str)
        palindromes: list | None = palindrome_finder.find_palindromes()

        # check if the correct palindromic words are found
        self.assertEqual(
            palindromes, ["racecar", "radar", "level", "deed", "civic"])

    def test_invalid_input(self):
        # test case for invalid input type
        with self.assertRaises(TypeError):
            Palindrome(12345)

    def test_empty_string(self):
        # test case for an empty string
        input_str: str = ""
        palindrome_finder: Palindrome = Palindrome(input_str)
        palindromes: list | None = palindrome_finder.find_palindromes()
        self.assertEqual(palindromes, None)

    def test_single_character(self):
        # test case for a single character input
        input_str: str = "a"
        palindrome_finder: Palindrome = Palindrome(input_str)
        palindromes: list | None = palindrome_finder.find_palindromes()
        self.assertEqual(palindromes, ["a"])

        input_str: str = "b"
        palindrome_finder: Palindrome = Palindrome(input_str)
        palindromes: list | None = palindrome_finder.find_palindromes()
        self.assertEqual(palindromes, ["b"])

        input_str: str = "z"
        palindrome_finder: Palindrome = Palindrome(input_str)
        palindromes: list | None = palindrome_finder.find_palindromes()
        self.assertEqual(palindromes, ["z"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
