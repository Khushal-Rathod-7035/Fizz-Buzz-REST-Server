"""Configures and sets up RESTful API resources for Fizz-Buzz logic and statistics."""
from src import rest_api as api
from src.fizzbuzz import apis as fizzbuzz

api.add_resource(fizzbuzz.FizzBuzzLogicAPI, '/rest/api/fizz-buzz-logic')
api.add_resource(fizzbuzz.FizzBuzzStatsAPI, '/rest/api/fizz-buzz-stats')
