"""Implements a Flask RESTful API endpoint at '/rest/api/fizz-buzz-stats' to handle GET requests,
providing a JSON representation of the most used request's parameters and hits based on
the 'FizzBuzzStats' model."""
import flask_restful as restful
from src.fizzbuzz.models.fizz_buzz_stats import FizzBuzzStats


class FizzBuzzStatsAPI(restful.Resource):
    """Handles a GET request to the '/rest/api/fizz-buzz-stats' endpoint.
    Returns:
        str: JSON representation of the most used request's parameters and hits.
    """
    def get(self):
        """Defines a 'get' method within the 'fizzbuzz_case_handler' decorator that
        retrieves and returns the most used Fizz-Buzz request's parameters and hits
        from the 'FizzBuzzStats' model, responding with a JSON representation or a
        message indicating no recorded requests, along with an HTTP status code."""
        most_used_request = FizzBuzzStats.query.order_by(FizzBuzzStats.hits.desc()).first()

        if most_used_request:
            result = most_used_request.json()
        else:
            result = {"message": "No requests recorded yet"}
        return result, 200
