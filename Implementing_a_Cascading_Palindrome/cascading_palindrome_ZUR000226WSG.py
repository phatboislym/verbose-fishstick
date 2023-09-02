class Palindrome:
    """
    a class to check and find palindromes within a given string.

    :test_string (str): the input string to search for palindromes.
    """

    def __init__(self, test_string: str) -> None:
        """
        initializes an instance of Palindrome.

        param:
        :test_string (str): the input string to search for palindromes.

        raises:
        :TypeError: if input_string is not a string.
        """
        if isinstance(test_string, str):
            self.test_string = test_string
        else:
            raise TypeError("input parameter must be a string")

    def is_palindrome(self, word: str) -> bool:
        """
        checks if a given word is a palindrome.

        param:
        :word (str): the word to check for palindrome.

        return:
        :bool: True if the word is a palindrome, False otherwise.
        """
        size: int = len(word)
        middle: int = size // 2

        if size == 1:
            return True

        # constant time check for early dismissal
        if size % 2:
            if word[middle - 1] != word[middle + 1]:
                return False
        else:
            if word[middle - 1] != word[middle]:
                return False

        # linear time check for palindrome
        for i in range(middle):
            if word[i] != word[size - i - 1]:
                return False

        return True

    def find_palindromes(self) -> list | None:
        """
        finds and returns a list of palindromes within the input string.

        return:
        :palindromes (list): a list of palindromic words found in the input
            string.
        """
        palindromes: list = []
        for word in self.test_string.split():
            if self.is_palindrome(word):
                palindromes.append(word)

        return palindromes if palindromes else None
