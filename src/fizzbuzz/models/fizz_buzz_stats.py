"""Defines a SQLAlchemy model 'FizzBuzzStats' within the 'src' module
to store FizzBuzz request statistics data in the connected database."""
from sqlalchemy import Column, Integer, String
from src import db


class FizzBuzzStats(db.Model):
    """This Model stores the FizzBuzz request stats data"""
    __tablename__ = 'fizz_buzz_stats'

    id = Column(Integer, primary_key=True)
    int1 = Column(Integer, nullable=False)
    int2 = Column(Integer, nullable=False)
    limit = Column(Integer, nullable=False)
    str1 = Column(String(50), nullable=False)
    str2 = Column(String(50), nullable=False)
    hits = Column(Integer, default=1)

    def __init__(self, int1: int, int2: int, limit: int,
                 str1: str, str2: str, hits: int = 1):
        self.int1 = int1
        self.int2 = int2
        self.limit = limit
        self.str1 = str1
        self.str2 = str2
        self.hits = hits

    def json(self):
        """Formats the model data into a JSON serializable dictionary."""
        return {
            'id': self.id,
            'int1': self.int1,
            'int2': self.int2,
            'limit': self.limit,
            'str1': self.str1,
            'str2': self.str2,
            'hits': self.hits
        }
