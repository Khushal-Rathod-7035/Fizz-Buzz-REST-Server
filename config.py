"""
Configuration settings for the REST server.

This module defines environment-specific configurations,
such as database settings, debug mode, and testing mode.
It uses environment variables to adapt to different hosting
environments, distinguishing between production and
development setups.
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = os.getenv('DEBUG', True)
TESTING = os.getenv('TESTING', False)
USE_RELOADER = os.getenv('USE_RELOADER', False)
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)

HOST_ENVIRONMENT = os.getenv("HOST_ENVIRONMENT")

if HOST_ENVIRONMENT == 'production':
    # Database Configuration
    DB_HOST = os.getenv("PROD_DB_HOST")
    DB_NAME = os.getenv('PROD_DB_NAME')
    SQLALCHEMY_DATABASE_URI = DB_HOST + os.path.join(BASE_DIR, DB_NAME)

elif HOST_ENVIRONMENT == 'development':
    # Database Configuration
    DB_HOST = os.getenv("DEV_DB_HOST")
    DB_NAME = os.getenv("DEV_DB_NAME")
    SQLALCHEMY_DATABASE_URI = DB_HOST + os.path.join(BASE_DIR, DB_NAME)
