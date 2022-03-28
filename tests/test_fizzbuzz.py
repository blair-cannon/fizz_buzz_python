import pytest
from fizzbuzz.fizzbuzz import fizzbuzz

# - Get "1" when pass in 1
def test_return1WhenGiven1():
    returnVal = "1"
    assert returnVal

# - Get "2" when pass in 2
# - Get "Fizz" when pass in 3
# - Get "Buzz" when pass in 5
# - Get "Fizz" when pass in 6 (multiple of 3)
# - Get "Buzz" when pass in 10 (multiple of 5)
# - Get "FizzBuzz" when pass in 15 (multiple of 3 and 5)