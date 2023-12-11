import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    # Test add function
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(0, 0), 0)

    # Test subtract function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(0, 5), -5)

    # Test multiply function
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(-2, 4), -8)

    # Test divide function
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 0), "Division by zero is not allowed.")
        self.assertAlmostEqual(divide(5, 3), 1.6666666666666667, places=6)

    # Test square function
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-3), 9)

    # Test square_root function
    def test_square_root(self):
        self.assertAlmostEqual(square_root(16), 4.0, places=6)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(-9), "Cannot calculate square root of a negative number.")

    # Test is_even function
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

    # Test is_odd function
    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))

    # Test factorial function
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    # Test find_max function
    def test_find_max(self):
        self.assertEqual(find_max(3, 5), 5)
        self.assertEqual(find_max(-2, 2), 2)
        self.assertEqual(find_max(0, 0), 0)

    # Test find_min function
    def test_find_min(self):
        self.assertEqual(find_min(3, 5), 3)
        self.assertEqual(find_min(-2, 2), -2)
        self.assertEqual(find_min(0, 0), 0)

    # Test sum_list function
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(sum_list([]), 0)

    # Test average_list function
    def test_average_list(self):
        self.assertEqual(average_list([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(average_list([-1, -2, -3, -4, -5]), -3.0)
        self.assertEqual(average_list([]), "List is empty.")

    # Test is_palindrome function
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))

    # Test count_vowels function
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels(""), 0)

    # Test is_prime function
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    # Test fibonacci function
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    # Test binary_to_decimal function
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("1010"), 10)
        self.assertEqual(binary_to_decimal("1101"), 13)
        self.assertEqual(binary_to_decimal("0"), 0)

    # Test decimal_to_binary function
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(13), "1101")
        self.assertEqual(decimal_to_binary(0), "0")

    # Test rectangle_area function
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(3, 0), 0)

    # Test circle_area function
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(5), 78.539816, places=6)
        self.assertAlmostEqual(circle_area(0), 0, places=6)
        self.assertAlmostEqual(circle_area(10), 314.159265, places=6)

    # Test triangle_area function
    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 5), 10)
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(3, 0), 0)

    # Test even_numbers_in_range function
    def test_even_numbers_in_range(self):
        # Test case 1: Range includes both even and odd numbers
        result = even_numbers_in_range(11, 15)
        self.assertListEqual(result, [12, 14])

        # Test case 2: Range starts with an odd number
        result = even_numbers_in_range(1, 5)
        self.assertListEqual(result, [2, 4])

        # Test case 3: Range starts and ends with even numbers
        result = even_numbers_in_range(4, 10)
        self.assertListEqual(result, [4, 6, 8, 10])


    # Test odd_numbers_in_range function
    def test_odd_numbers_in_range(self):
        self.assertEqual(odd_numbers_in_range(1, 10), [1, 3, 5, 7, 9])
        self.assertEqual(odd_numbers_in_range(-5, 5), [-5, -3, -1, 1, 3, 5])
        self.assertEqual(odd_numbers_in_range(11, 15), [11, 13, 15])

    # Test reverse_list function
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list(["apple", "banana", "cherry"]), ["cherry", "banana", "apple"])
        self.assertEqual(reverse_list([]), [])

    # Test string_length function
    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)
        self.assertEqual(string_length("python"), 6)

    # Test concatenate_strings function
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "World"), "HelloWorld")
        self.assertEqual(concatenate_strings("Open", "AI"), "OpenAI")
        self.assertEqual(concatenate_strings("", "Python"), "Python")

    # Test count_char_occurrences function
    def test_count_char_occurrences(self):
        self.assertEqual(count_char_occurrences("hello", "l"), 2)
        self.assertEqual(count_char_occurrences("programming", "g"), 2)
        self.assertEqual(count_char_occurrences("apple", "z"), 0)

    # Test int_list_to_str_list function
    def test_int_list_to_str_list(self):
        self.assertEqual(int_list_to_str_list([1, 2, 3]), ["1", "2", "3"])
        self.assertEqual(int_list_to_str_list([]), [])
        self.assertEqual(int_list_to_str_list([-1, 0, 1]), ["-1", "0", "1"])

    # Test sum_of_digits function
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(-12345), 15)

    # Test find_index function
    def test_find_index(self):
        self.assertEqual(find_index([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(find_index(["apple", "banana", "cherry"], "banana"), 1)
        self.assertEqual(find_index([], 42), -1)
        self.assertEqual(find_index([1, 2, 3], 5), -1)

    # Test prime_numbers_in_range function
    def test_prime_numbers_in_range(self):
        self.assertEqual(prime_numbers_in_range(1, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers_in_range(-5, 5), [2, 3, 5])
        self.assertEqual(prime_numbers_in_range(11, 15), [11, 13])

    # Test power function
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(4, -1), 0.25)

    # Test median function
    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([5, 4, 3, 2, 1]), 3)
        self.assertEqual(median([1, 2, 3]), 2)

    # Test mode function
    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3, 4, 4, 5]), [2, 4])
        self.assertEqual(mode([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(mode(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"])

    # Test gcd function
    def test_gcd(self):
        self.assertEqual(gcd(24, 18), 6)
        self.assertEqual(gcd(7, 5), 1)
        self.assertEqual(gcd(0, 5), 5)

    # Test uppercase_strings function
    def test_uppercase_strings(self):
        self.assertEqual(uppercase_strings(["hello", "world"]), ["HELLO", "WORLD"])
        self.assertEqual(uppercase_strings([]), [])
        self.assertEqual(uppercase_strings(["Python"]), ["PYTHON"])

    # Test lowercase_strings function
    def test_lowercase_strings(self):
        self.assertEqual(lowercase_strings(["Hello", "WORLD"]), ["hello", "world"])
        self.assertEqual(lowercase_strings([]), [])
        self.assertEqual(lowercase_strings(["PyThOn"]), ["python"])


if __name__ == '__main__':
    unittest.main()
