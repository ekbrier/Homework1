#QUESTION 3
def palindrome_searcher():
    word = str(input('Please enter a word:  '))
    if word == word[::-1]:
        print('Congratulations! Your word is a palindrome')
    else:
        print('Your word is not a palindrome')


if __name__ == '__main__':
    palindrome_searcher()

#QUESTION 4
import unittest
from unittest import TestCase,  main
from Assessment_2_Eleanor_Brierley import palindrome_searcher

class Test_Palindrome(unittest.TestCase):

    def test_if_palindrome_is_true(self):
        value = palindrome_searcher().is_palindrome('noon')
        self.assertEquals(value, True)

    def test_if_palindrome_is_false(self):
        value = palindrome_searcher().is_palindrome('banana')
        self.assertEquals(value, False)

    def test_error_reverse(self):
        list_of_bad_value = [123, None]
        for bad_value in list_of_bad_value:
            self.assertRaises(
                TypeError,
                palindrome_searcher().reverse,
                bad_value
            )
   def test_length(self):
    value

if __name__ == '__main__':
    unittest.main()
    
    
# QUESTION 9
def two_numbers(my_numbers, target_sum):
    output = []
    for x in range(0, len(my_numbers) - 1):
        attempt_a = my_numbers[x]
        for y in range(x + 1, len(my_numbers)):
            attempt_b = my_numbers[y]
            sum = attempt_a + attempt_b
            if sum == target_sum:
                output.append([attempt_a, attempt_b])
                print(output)


if __name__ == "__main__":
    two_numbers([6, 5, -4, 8, 11, 1, -1, 6], 10)
