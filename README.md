# Robust Calculator

A modular calculator application built in Python using Object-Oriented Programming principles, automated testing, and Continuous Integration.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero error handling
- Command-line interface
- Modular design using classes and packages
- Automated unit testing with Pytest
- 100% test coverage
- Continuous Integration with GitHub Actions

## Project Structure

```
robust_calculator/
│
├── app/
│   ├── calculation/
│   ├── calculator/
│   └── operation/
│
├── tests/
│   ├── test_calculations.py
│   └── test_operations.py
│
├── .github/workflows/
│   └── python-tests.yml
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Swathi-V4/robust_calculator.git
cd robust_calculator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Program

Run the calculator:

```bash
python main.py
```

## Running Tests

Execute all tests:

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=app tests/
```

Generate coverage report:

```bash
coverage report -m
```

## Continuous Integration

This project uses GitHub Actions to automatically:

- Install dependencies
- Run unit tests
- Generate coverage reports
- Verify 100% test coverage

Every push to the repository automatically triggers the workflow.

## Technologies Used

- Python 3.11
- Pytest
- Pytest-Cov
- Git
- GitHub
- GitHub Actions

## Author

Swathi Veerapalli