"""Tests the Fizz-Buzz statistics endpoint with recorded requests by sending
a GET request to the endpoint in the 'app' module"""
import json
from src import app


def test_fizz_buzz_stats_endpoint_with_requests():
    """Tests the Fizz-Buzz statistics endpoint with recorded requests by sending
    a GET request to the endpoint in the 'app' module, decoding the response data
    using the 'json' module, and asserting the expected result containing the parameters
    and hits of the most used request."""
    parameters = {'int1': 3, 'int2': 5, 'limit': 15, 'str1': 'fizz', 'str2': 'buzz'}
    app.test_client().get('/rest/api/fizz-buzz-logic', query_string=parameters)

    response = app.test_client().get('/rest/api/fizz-buzz-stats')
    data = json.loads(response.data.decode('utf-8'))
    expected_result = {'id': data['id'], 'int1': data['int1'], 'int2': data['int2'], 'limit': data['limit'],
                       'str1': data['str1'], 'str2': data['str2'], 'hits': data['hits']}
    assert response.status_code == 200
    assert data == expected_result
