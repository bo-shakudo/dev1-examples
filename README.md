# dev1-examples

A Python calculator module with comprehensive unit tests.

## Features

The calculator module provides:

- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, factorial)
- Utility functions (percentage, average)
- Prime number checking
- Operation history tracking
- Quick utility functions for simple operations

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import Calculator, quick_add, is_prime

# Create a calculator instance
calc = Calculator()

# Perform operations
result = calc.add(5, 3)  # Returns 8
result = calc.divide(10, 2)  # Returns 5.0
result = calc.factorial(5)  # Returns 120

# Check calculation history
history = calc.get_history()

# Use quick functions
result = quick_add(2, 3)  # Returns 5

# Check if a number is prime
is_prime(17)  # Returns True
```

## Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=calculator --cov-report=term-missing
```

## Test Coverage

The project maintains 100% test coverage with comprehensive unit tests covering:

- All calculator operations
- Error handling and edge cases
- History tracking functionality
- Prime number checking
- Floating point precision
- Large and small number handling