from cascading_palindrome_ZUR000226WSG import Palindrome


if __name__ == '__main__':

    def demarcate() -> None:
        print("-" * 60)

    # Example 1:
    # should return [racecar, radar, level, deed, civic]
    input_str1: str = "racecar radar hello world level deed civic"
    palindrome_finder1: Palindrome = Palindrome(input_str1)
    palindromes1: list | None = palindrome_finder1.find_palindromes()
    print("expected:    ['racecar', 'radar', 'level', 'deed', 'civic']")
    print("palindromes:", palindromes1)
    demarcate()

    # Example 2:
    input_str2: str = "python language radar"  # should return [radar]
    palindrome_finder2: Palindrome = Palindrome(input_str2)
    palindromes2: list | None = palindrome_finder2.find_palindromes()
    print("expected:    ['radar']")
    print("palindromes:", palindromes2)
    demarcate()

    # Example 3:
    input_str3: str = "madam anna kayak"  # should return [madam, anna, kayak]
    palindrome_finder3: Palindrome = Palindrome(input_str3)
    palindromes3: list | None = palindrome_finder3.find_palindromes()
    print("expected:    ['madam', 'anna', 'kayak']")
    print("palindromes:", palindromes3)
    demarcate()

    # Example 4:
    input_str4: str = "programming code class"  # should return None
    palindrome_finder4: Palindrome = Palindrome(input_str4)
    palindromes4: list | None = palindrome_finder4.find_palindromes()
    print("expected:    None")
    print("palindromes:", palindromes4)
    demarcate()

    # Example 5:
    input_str5: str = "able was I ere I saw elba"  # should return [I, ere, I]
    palindrome_finder5: Palindrome = Palindrome(input_str5)
    palindromes5: list | None = palindrome_finder5.find_palindromes()
    print("expected:    ['I', 'ere', 'I']")
    print("palindromes:", palindromes5)
    demarcate()

    # Example 6:
    input_str6: str = "deify repaper civic"  # should return [repaper, civic]
    palindrome_finder6: Palindrome = Palindrome(input_str6)
    palindromes6: list | None = palindrome_finder6.find_palindromes()
    print("expected:    ['repaper', 'civic']")
    print("palindromes:", palindromes6)
    demarcate()

    # Example 7:
    # should return [racecar, madam, kayak, civic]
    input_str7: str = "racecar madam kayak civic"
    palindrome_finder7: Palindrome = Palindrome(input_str7)
    palindromes7: list | None = palindrome_finder7.find_palindromes()
    print("expected:    ['racecar', 'madam', 'kayak', 'civic']")
    print("palindromes:", palindromes7)
    demarcate()

    # Example 8:
    input_str8: str = "python language is fun"  # should return None
    palindrome_finder8: Palindrome = Palindrome(input_str8)
    palindromes8: list | None = palindrome_finder8.find_palindromes()
    print("expected:    None")
    print("palindromes:", palindromes8)
    demarcate()

    # Example 9:
    input_str9: str = "hello world"  # should return None
    palindrome_finder9: Palindrome = Palindrome(input_str9)
    palindromes9: list | None = palindrome_finder9.find_palindromes()
    print("expected:    None")
    print("palindromes:", palindromes9)
    demarcate()

    # Example 10:
    input_str10: str = "level deed civic"  # should return [level, deed, civic]
    palindrome_finder10: Palindrome = Palindrome(input_str10)
    palindromes10: list | None = palindrome_finder10.find_palindromes()
    print("expected:    ['level', 'deed', 'civic']")
    print("palindromes:", palindromes10)
    demarcate()

    # Example 11:
    input_str11: str = '1230321'  # should return [1230321]
    palindrome_finder11: Palindrome = Palindrome(input_str11)
    palindromes11: list | None = palindrome_finder11.find_palindromes()
    print("expected:    ['1230321']")
    print("palindromes:", palindromes11)
    demarcate()

    # Example 12:
    # should return [1230321, 0124210]
    input_str12: str = '1230321 09234 0124210'
    palindrome_finder12: Palindrome = Palindrome(input_str12)
    palindromes12: list | None = palindrome_finder12.find_palindromes()
    print("expected:    ['1230321', '0124210']")
    print("palindromes:", palindromes12)
    demarcate()

    # Example 13:
    # should return [abcd5dcba, 1230321, 0124210]
    input_str13: str = 'abcd5dcba 1230321 09234 0124210'
    palindrome_finder13: Palindrome = Palindrome(input_str13)
    palindromes13: list | None = palindrome_finder13.find_palindromes()
    print("expected:    ['abcd5dcba', '1230321', '0124210']")
    print("palindromes:", palindromes13)
    demarcate()

    # Example 14:
    # should return [abcddcba, 123321, 012210]
    input_str14: str = 'abcddcba 123321 09234 012210'
    palindrome_finder14: Palindrome = Palindrome(input_str14)
    palindromes14: list | None = palindrome_finder14.find_palindromes()
    print("expected:    ['abcddcba', '123321', '012210']")
    print("palindromes:", palindromes14)
    demarcate()

    # Example 15:
    input_str15: str = "aaaa"  # should return [aaaa]
    palindrome_finder15 = Palindrome(input_str15)
    palindromes15: list | None = palindrome_finder15.find_palindromes()
    print("expected:    ['aaaa']")
    print("palindromes:", palindromes15)
    demarcate()

    # Example 16:
    input_str16: str = "aaaa, bbbb"  # should return [bbbb]
    palindrome_finder16 = Palindrome(input_str16)
    palindromes16: list | None = palindrome_finder16.find_palindromes()
    print("expected:    ['bbbb']")
    print("palindromes:", palindromes16)
    demarcate()
