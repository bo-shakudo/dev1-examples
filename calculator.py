"""
A simple calculator module with basic mathematical operations.
"""

import math
from typing import Union, List


class Calculator:
    """A calculator class with various mathematical operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, n: Union[int, float]) -> float:
        """Calculate the square root of n."""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(n)
        self.history.append(f"√{n} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate the factorial of n."""
        if not isinstance(n, int):
            raise TypeError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def percentage(self, value: Union[int, float], percent: Union[int, float]) -> float:
        """Calculate percentage of a value."""
        result = (value * percent) / 100
        self.history.append(f"{percent}% of {value} = {result}")
        return result
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        result = sum(numbers) / len(numbers)
        self.history.append(f"Average of {numbers} = {result}")
        return result
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()
    
    def get_history(self) -> List[str]:
        """Get the calculation history."""
        return self.history.copy()


def quick_add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Quick addition function without history tracking."""
    return a + b


def quick_multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Quick multiplication function without history tracking."""
    return a * b


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if not isinstance(n, int):
        raise TypeError("Prime check requires an integer")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True