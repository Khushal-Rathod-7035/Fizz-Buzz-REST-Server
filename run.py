"""
Entry point script for the REST server management.

This script initializes a Flask-Script Manager,
allowing the execution of various commands essential
for managing the REST server, including database
migration and upgrade tasks. It serves as a central
point for coordinating multiple services associated
with the application.
"""


def create_manager():
    """Creates a Flask-Script Manager for command-line tasks.

    The manager facilitates the execution of commands such as
    creating migration scripts ('db migrate') and upgrading the
    database to the latest migration version ('db upgrade').
    It serves as a command-line interface for managing various
    aspects of the REST server.
    """
    from src import manager
    return manager


if __name__ == "__main__":
    create_manager().run()
