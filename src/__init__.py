"""
Configures and initializes a Flask application with various extensions
and middleware for a Fizz-Buzz REST server.

Key Components:
    - Flask: Main web application framework.
    - SQLAlchemy: Database ORM for interacting with the database.
    - Marshmallow: Object serialization and deserialization library.
    - Flask-RESTful: Extension for building REST APIs with Flask.
    - Flask-Migrate: Handles database migrations.
    - Flask-Script: Adds command-line functionality to manage the application.
    - Flask-CORS: Handles Cross-Origin Resource Sharing.
    - ProxyFix: Middleware to handle proxy headers for correct IP information.
    - Flask-Session: Manages user sessions.
    - Flask-Script Server: Runs the development server.
    - Prometheus Flask Exporter: Exports Prometheus-compatible metrics.
    - Logging: Configures basic logging with INFO level.
    - Dotenv: Loads environment variables from a .env file.

Usage:
    - Run the application with 'manager.run()' to start the server.
    - Use Flask commands for database migrations ('db migrate', 'db upgrade').
    - Configure routes in the 'src.fizzbuzz.fizzbuzz_router' module.
    - Access Prometheus metrics at the '/metrics' endpoint.

Note: Ensure proper configuration in the 'config' module for database and other settings.
"""
import logging
from flask import Flask
import flask_restful as restful
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS
from flask_script import Server, Manager
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from prometheus_flask_exporter import PrometheusMetrics
from flask_session import Session

load_dotenv()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0'))

db = SQLAlchemy(app)
ma = Marshmallow(app)
rest_api = restful.Api(app)

import src.fizzbuzz.fizzbuzz_router

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, Promotheus Metrics Start", version="1.0.0")
