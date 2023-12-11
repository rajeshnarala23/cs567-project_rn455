# Function 1: Add two numbers
def add(a, b):
    return a + b

# Function 2: Subtract two numbers
def subtract(a, b):
    return a - b

# Function 3: Multiply two numbers
def multiply(a, b):
    return a * b

# Function 4: Divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

# Function 5: Calculate the square of a number
def square(x):
    return x ** 2

# Function 6: Calculate the square root of a number
def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Cannot calculate square root of a negative number."

# Function 7: Check if a number is even
def is_even(x):
    return x % 2 == 0

# Function 8: Check if a number is odd
def is_odd(x):
    return x % 2 != 0

# Function 9: Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function 10: Find the maximum of two numbers
def find_max(a, b):
    return max(a, b)

# Function 11: Find the minimum of two numbers
def find_min(a, b):
    return min(a, b)

# Function 12: Calculate the sum of a list of numbers
def sum_list(numbers):
    return sum(numbers)

# Function 13: Calculate the average of a list of numbers
def average_list(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return "List is empty."

# Function 14: Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Function 15: Count the number of vowels in a string
def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Function 16: Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function 17: Generate Fibonacci sequence up to n terms
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        return sequence

# Function 18: Convert a binary number to decimal
def binary_to_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        return "Invalid binary input."

# Function 19: Convert a decimal number to binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

# Function 20: Calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function 21: Calculate the area of a circle
def circle_area(radius):
    import math
    return math.pi * (radius ** 2)

# Function 22: Calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Function 23: Generate a list of even numbers in a range
def even_numbers_in_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

# Function 24: Generate a list of odd numbers in a range
def odd_numbers_in_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 != 0]

# Function 25: Reverse a list
def reverse_list(lst):
    return lst[::-1]

# Function 26: Find the length of a string
def string_length(string):
    return len(string)

# Function 27: Concatenate two strings
def concatenate_strings(str1, str2):
    return str1 + str2

# Function 28: Count the occurrences of a character in a string
def count_char_occurrences(string, char):
    return string.count(char)

# Function 29: Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Function 30: Check if a list is sorted
def is_sorted(lst):
    return lst == sorted(lst)

# Function 31: Convert a list of integers to a list of strings
def int_list_to_str_list(int_list):
    return [str(x) for x in int_list]

# Function 32: Calculate the sum of digits in a number
def sum_of_digits(number):
    if number < 0:
        number = -number  # Convert negative number to positive
    return sum(int(digit) for digit in str(number))

# Function 33: Find the index of the first occurrence of an element in a list
def find_index(lst, element):
    if element in lst:
        return lst.index(element)
    else:
        return -1

# Function 34: Generate a list of prime numbers in a range
def prime_numbers_in_range(start, end):
    return [x for x in range(start, end + 1) if is_prime(x)]

# Function 35: Calculate the power of a number
def power(base, exponent):
    return base ** exponent

# Function 36: Calculate the median of a list of numbers
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_numbers[n // 2]

# Function 37: Calculate the mode of a list of numbers
def mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode

# Function 38: Find the GCD (Greatest Common Divisor) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 39: Convert a list of strings to uppercase
def uppercase_strings(strings):
    return [s.upper() for s in strings]

# Function 40: Convert a list of strings to lowercase
def lowercase_strings(strings):
    return [s.lower() for s in strings]
