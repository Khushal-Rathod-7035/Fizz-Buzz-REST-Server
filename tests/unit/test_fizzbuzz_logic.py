"""Tests the functionality of the Fizz-Buzz logic endpoint in the 'app' module,
utilizing the assertions and validations."""
import json
from src import app


def test_fizz_buzz_logic():
    """Tests the Fizz-Buzz logic endpoint by sending a GET request with specified
    parameters, decoding the response data using the 'json' module, and asserting
    that the returned result matches the expected Fizz-Buzz sequence."""
    parameters = {'int1': 3, 'int2': 5, 'limit': 15, 'str1': 'fizz', 'str2': 'buzz'}
    response = app.test_client().get('/rest/api/fizz-buzz-logic', query_string=parameters)
    data = json.loads(response.data.decode('utf-8'))
    expected_result = "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz"
    assert response.status_code == 200
    assert data == expected_result
