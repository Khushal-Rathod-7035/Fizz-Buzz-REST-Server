"""Implements a Flask RESTful API endpoint at '/rest/api/fizz-buzz-logic' to handle GET requests,
generating a Fizz-Buzz sequence based on specified parameters with error handling using
the 'fizzbuzz_case_handler' decorator."""
import flask_restful as restful
from flask_restful import reqparse
from src import db
from src.fizzbuzz.models.fizz_buzz_stats import FizzBuzzStats
from src.handler.case_handler import fizzbuzz_case_handler


class FizzBuzzLogicAPI(restful.Resource):
    """Handles a GET request to the '/rest/api/fizz-buzz-logic' endpoint.
    Returns:
        str: representation of the Fizz-Buzz sequence based on the provided parameters.
    """

    @fizzbuzz_case_handler
    def get(self):
        """Generates a list of strings based on the Fizz-Buzz logic.
        Args:
            int1 (int): The first integer for Fizz-Buzz logic.
            int2 (int): The second integer for Fizz-Buzz logic.
            limit (int): The upper limit for generating the Fizz-Buzz list.
            str1 (str): The string replacement for multiples of int1.
            str2 (str): The string replacement for multiples of int2.
        Returns:
            str: A list of strings representing the Fizz-Buzz sequence.
        """
        req_parser = reqparse.RequestParser()
        req_parser.add_argument('int1', type=int, required=True)
        req_parser.add_argument('int2', type=int, required=True)
        req_parser.add_argument('limit', type=int, required=True)
        req_parser.add_argument('str1', type=str, required=True)
        req_parser.add_argument('str2', type=str, required=True)
        args = req_parser.parse_args()
        int1 = args['int1']
        int2 = args['int2']
        limit = args['limit']
        str1 = args['str1']
        str2 = args['str2']
        result = []
        for num in range(1, limit + 1):
            output = ""
            if num % int1 == 0:
                output += str1
            if num % int2 == 0:
                output += str2
            if not output:
                output = str(num)
            result.append(output)
        result = ','.join(result)

        request_entry = FizzBuzzStats.query.filter_by(int1=int1, int2=int2,
                                                      limit=limit, str1=str1, str2=str2).first()
        if request_entry:
            request_entry.hits += 1
        else:
            request_entry = FizzBuzzStats(int1=int1, int2=int2, limit=limit, str1=str1, str2=str2)
        db.session.add(request_entry)
        db.session.commit()
        return result, 200
