"""Decorator function 'fizzbuzz_case_handler' that handles edge cases and failures
for the decorated function, providing additional functionality to address specific
scenarios in the Fizz-Buzz logic."""
from functools import wraps
from flask_restful import reqparse


def fizzbuzz_case_handler(func):
    """ This decorator functions handle edge cases and failures"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        req_parser = reqparse.RequestParser()
        req_parser.add_argument('int1', type=int, required=True)
        req_parser.add_argument('int2', type=int, required=True)
        req_parser.add_argument('limit', type=int, required=True)

        args_from_request = req_parser.parse_args()
        int1 = args_from_request['int1']
        int2 = args_from_request['int2']
        limit = args_from_request['limit']

        if int1 <= 0 or int2 <= 0 or limit < 0:
            return {"error": "Invalid parameters. int1 and int2 Parameters should "
                    "be positive and non-zero. limit Parameters should be positive."}, 400
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return {"error": "Zero division error. Please provide valid non-zero "
                    "values for int1, int2, and limit."}, 400

    return wrapper
