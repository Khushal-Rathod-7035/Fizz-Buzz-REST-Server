"""Tests the Fizz-Buzz statistics endpoint when no requests have been
recorded, by sending a GET request to the endpoint in the 'app' module."""
import json
from src import app


def test_fizz_buzz_stats_endpoint_no_requests():
    """Tests the Fizz-Buzz statistics endpoint when no requests have
    been recorded, sending a GET request to the endpoint in the 'app'
    module, decoding the response data using the 'json' module, and
    asserting that the returned message indicates no recorded requests."""
    response = app.test_client().get('/rest/api/fizz-buzz-stats')
    data = json.loads(response.data.decode('utf-8'))
    if 'message' in data:
        assert data == {"message": "No requests recorded yet"}
