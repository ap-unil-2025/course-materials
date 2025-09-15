"""
Automated tests for Problem Set 3
Do not modify this file!
"""

import pytest
import sys
import os

# Add current directory to path to import student modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Exercise 1: Temperature Tests
def test_celsius_to_fahrenheit():
    from temperature import celsius_to_fahrenheit
    
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0
    assert round(celsius_to_fahrenheit(37), 1) == 98.6

def test_fahrenheit_to_celsius():
    from temperature import fahrenheit_to_celsius
    
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(-40) == -40.0

def test_classify_temperature():
    from temperature import classify_temperature
    
    assert classify_temperature(-5) == "freezing"
    assert classify_temperature(10) == "cold"
    assert classify_temperature(20) == "moderate"
    assert classify_temperature(30) == "warm"
    assert classify_temperature(40) == "hot"

# Exercise 2: List Operations Tests
def test_find_max_min():
    from list_operations import find_max_min
    
    assert find_max_min([3, 1, 4, 1, 5, 9]) == (9, 1)
    assert find_max_min([42]) == (42, 42)
    assert find_max_min([-5, -1, -10]) == (-1, -10)

def test_remove_duplicates():
    from list_operations import remove_duplicates
    
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 1, 1]) == [1]

def test_calculate_average():
    from list_operations import calculate_average
    
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) is None
    assert calculate_average([42]) == 42.0

# Exercise 3: Word Counter Tests
def test_count_words():
    from word_counter import count_words
    
    result = count_words("Hello world hello Python")
    assert result['hello'] == 2
    assert result['world'] == 1
    assert result['python'] == 1

def test_most_common_words():
    from word_counter import most_common_words
    
    text = "the quick brown fox jumps over the lazy dog the fox"
    result = most_common_words(text, 3)
    assert len(result) == 3
    assert result[0][0] == 'the'
    assert result[0][1] == 3

# Exercise 4: Calculator Tests
def test_calculate():
    from calculator import calculate
    
    assert calculate("2 + 3") == 5.0
    assert calculate("2 + 3 * 4") == 14.0
    assert calculate("(2 + 3) * 4") == 20.0
    assert calculate("10 / 2") == 5.0

def test_is_valid_expression():
    from calculator import is_valid_expression
    
    assert is_valid_expression("2 + 3") == True
    assert is_valid_expression("(2 + 3) * 4") == True
    assert is_valid_expression("2 + x") == False
    assert is_valid_expression("import os") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])