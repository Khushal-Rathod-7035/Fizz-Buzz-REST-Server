"""Tests the 'json' method of the 'FizzBuzzStats' model by creating an instance with specified
parameters, calling the 'json' method."""
from src.fizzbuzz.models.fizz_buzz_stats import FizzBuzzStats


def test_fizz_buzz_stats_model_json():
    """Tests the 'json' method of the 'FizzBuzzStats' model by creating an instance with specified
    parameters, calling the 'json' method, and asserting that the returned JSON representation
    matches the expected result."""
    fizzbuzz_stats = FizzBuzzStats(int1=3, int2=5, limit=15, str1='fizz', str2='buzz', hits=1)
    json_data = fizzbuzz_stats.json()
    expected_result = {'id': None, 'int1': 3, 'int2': 5, 'limit': 15, 'str1': 'fizz',
                       'str2': 'buzz', 'hits': 1}
    assert json_data == expected_result
