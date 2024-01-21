# Fizz-Buzz REST Server

## Overview

The Fizz-Buzz REST Server is a Flask-based web application that implements the classic Fizz-Buzz logic through a REST API. It provides the capability to generate Fizz-Buzz sequences based on user-defined parameters and offers a statistical endpoint to retrieve information about the most used request.

## Features
- **Fizz-Buzz Logic:** Replace multiples of specified integers with corresponding strings.
- **Fizz-Buzz Endpoint:** Generate Fizz-Buzz sequences with customizable parameters.
- **Statistical Endpoint:** Retrieve information about the most used Fizz-Buzz request.

## Getting Started

### Prerequisites
- Python 3.6.8 (download from https://www.python.org/downloads/release/python-368/)
- python -m venv venv (to create virtual environment)
- pip (Python package installer)

## Table of Contents

- [Installation](#installation)
- [Configuring Environment Variables](#configuring-environment-variables)
- [Usage](#usage)
- [Local Database Migration](#local-database-migration)
- [Code Linters](#code-linters)
- [Automated Unit Testing with pytest](#automated-unit-testing-with-pytest)


### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd fizz-buzz-rest-server
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows
    ```
4. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```
5. Install ansible:
    ```bash
    pip install ansible
    ```

### Configuring Environment Variables
To configure environment variables from environments/{development or production}-env.yml file and export them to a .env file, follow these steps:
1. Install Required Packages: Make sure you have the required packages installed. If not, install them using -
    ```bash
    pip install PyYAML
    ```
2. Run the Script: Arguments - i) yaml_file (str): Path to the YAML file. ii) env_file (str): Path to the .env file.
    ```bash
    python export_yaml_to_env.py ./environments/development-env.yml ./.env
    ```
3. Check the Output:
The script will print a message indicating whether the conversion was successful. Check the generated .env file to ensure that the environment variables are correctly exported.
   
   ```Successfully exported data from .\environments\development-env.yml to .\.env```
4. Review and Adjust: Open the generated .env file to review the exported environment variables. You can adjust the values if needed.

### Usage
Run the server:
```bash
python run.py runserver
```
The server will be accessible at http://localhost:5000


### Local Database Migration
To manage local database migrations for the Fizz-Buzz REST Server, follow these steps:
1. Create a migration script by running the following command in your terminal:
    ```bash
    python run.py db revision -m "CREATE TABLE fizz_buzz_stats"
    ```
2. Update the generated migration script located in the `migrations/versions` directory.
3. Apply the migration to your local database by executing:
    ```bash
    python run.py db upgrade
    ```
4. If needed, you can revert the migration by running:
    ```bash
    python run.py db downgrade
    ```
Make sure to review and customize the migration script as necessary before applying it to database.

### Code Linters
Pylint and Flake8 are configured for this codebase. It is recommended to run these linters after any future changes. Follow the commands below:
1. To check for linter errors in specific files, execute:
    ```bash
    pylint ./run.py
    ```
2. To check for style errors, execute:
    ```bash
    flake8 --statistics -qq --ignore=F,S,CCR
    ```
   For specific files, run:
    ```bash
    flake8 --statistics -qq --ignore=F,S,CCR --filename=./run.py
    ```
3. To check for logical errors, execute:
    ```bash
    flake8 --statistics -qq --ignore=E,S,W,CCR
    ```
   For specific files, run:
    ```bash
    flake8 --statistics -qq --ignore=E,S,W,CCR --filename=./run.py
    ```
4. To check for security errors, execute:
    ```bash
    flake8 --statistics -qq --ignore=E,F,W,CCR
    ```
   For specific files, run:
    ```bash
    flake8 --statistics -qq --ignore=E,F,W,CCR --filename=./run.py
    ```

### Automated Unit Testing with pytest

The `pytest` testing framework is installed and configured for this repository. To run the test cases, use the following command in the command-line interface:

```bash
pytest
```
