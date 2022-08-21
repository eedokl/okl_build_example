# Python Build Example

## What is this project about?

It's a very basic project that shows how to set up a python package.

It uses GitHub actions to fire a CI build that run the tests and generate the package

The package has been created following this [tutorial](https://packaging.python.org/tutorials/packaging-projects/)

## Python version:
**3.8**

## Folder structure

1. __/.github/workflows__
    This folder will contain the GitHub workflows template

2. __/src__
    This folder will contain the source code

## Unit Tests

This project uses [unittest](https://docs.python.org/3/library/unittest.html) as the testing framework, and [coverage.py](https://coverage.readthedocs.io/en/coverage-5.4/) for generating code coverage reports. In addition flake8 linter is used.

### How to run the tests with coverage report

Inside the __/src__ folder, just run this command:

````bash
pytest --cov=calculator --cov-report term --cov-report html tests
````
### How to view the linter report

Inside the __/src__ folder, just run this command:

````bash
flake8 .
````
