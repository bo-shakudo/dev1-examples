"""
Comprehensive unit tests for the calculator module.
"""

import pytest
import math
from calculator import Calculator, quick_add, quick_multiply, is_prime


class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition functionality."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 3.7) == 6.2
        assert self.calc.add(-5, -3) == -8
    
    def test_subtract(self):
        """Test subtraction functionality."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(-3, -5) == 2
        assert self.calc.subtract(10.5, 2.3) == 8.2
        assert self.calc.subtract(0, 0) == 0
    
    def test_multiply(self):
        """Test multiplication functionality."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 5) == -10
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(2.5, 4) == 10.0
        assert self.calc.multiply(-3, -4) == 12
    
    def test_divide(self):
        """Test division functionality."""
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-10, 2) == -5.0
        assert self.calc.divide(0, 5) == 0.0
        assert self.calc.divide(15.6, 3) == 5.2
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(-3, 0)
    
    def test_power(self):
        """Test power functionality."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(2, -2) == 0.25
        assert self.calc.power(9, 0.5) == 3.0
        assert self.calc.power(-2, 3) == -8
    
    def test_square_root(self):
        """Test square root functionality."""
        assert self.calc.square_root(9) == 3.0
        assert self.calc.square_root(0) == 0.0
        assert self.calc.square_root(2) == pytest.approx(1.414213562373095)
        assert self.calc.square_root(16) == 4.0
        assert self.calc.square_root(0.25) == 0.5
    
    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)
        
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-10)
    
    def test_factorial(self):
        """Test factorial functionality."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(3) == 6
        assert self.calc.factorial(10) == 3628800
    
    def test_factorial_negative(self):
        """Test factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-1)
        
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-5)
    
    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Factorial requires an integer"):
            self.calc.factorial(3.5)
        
        with pytest.raises(TypeError, match="Factorial requires an integer"):
            self.calc.factorial("5")
    
    def test_percentage(self):
        """Test percentage functionality."""
        assert self.calc.percentage(100, 50) == 50.0
        assert self.calc.percentage(200, 25) == 50.0
        assert self.calc.percentage(80, 0) == 0.0
        assert self.calc.percentage(150, 20) == 30.0
        assert self.calc.percentage(50, 110) == 55.0
    
    def test_average(self):
        """Test average functionality."""
        assert self.calc.average([1, 2, 3, 4, 5]) == 3.0
        assert self.calc.average([10]) == 10.0
        assert self.calc.average([2, 4]) == 3.0
        assert self.calc.average([-1, 0, 1]) == 0.0
        assert self.calc.average([1.5, 2.5, 3.5]) == 2.5
    
    def test_average_empty_list(self):
        """Test average of empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            self.calc.average([])
    
    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        self.calc.divide(10, 2)
        
        history = self.calc.get_history()
        assert len(history) == 3
        assert "2 + 3 = 5" in history
        assert "4 * 5 = 20" in history
        assert "10 / 2 = 5.0" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 1)
        self.calc.subtract(5, 3)
        assert len(self.calc.get_history()) == 2
        
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0
    
    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not the original list."""
        self.calc.add(1, 1)
        history = self.calc.get_history()
        history.append("Modified")
        
        # Original history should be unchanged
        assert "Modified" not in self.calc.get_history()


class TestQuickFunctions:
    """Test cases for quick utility functions."""
    
    def test_quick_add(self):
        """Test quick_add function."""
        assert quick_add(2, 3) == 5
        assert quick_add(-1, 1) == 0
        assert quick_add(0, 0) == 0
        assert quick_add(2.5, 3.7) == 6.2
    
    def test_quick_multiply(self):
        """Test quick_multiply function."""
        assert quick_multiply(3, 4) == 12
        assert quick_multiply(-2, 5) == -10
        assert quick_multiply(0, 100) == 0
        assert quick_multiply(2.5, 4) == 10.0


class TestIsPrime:
    """Test cases for the is_prime function."""
    
    def test_prime_numbers(self):
        """Test that prime numbers are correctly identified."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            assert is_prime(prime) is True, f"{prime} should be prime"
    
    def test_non_prime_numbers(self):
        """Test that non-prime numbers are correctly identified."""
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
        for non_prime in non_primes:
            assert is_prime(non_prime) is False, f"{non_prime} should not be prime"
    
    def test_negative_numbers(self):
        """Test that negative numbers are not prime."""
        assert is_prime(-1) is False
        assert is_prime(-2) is False
        assert is_prime(-7) is False
    
    def test_large_prime(self):
        """Test with a larger prime number."""
        assert is_prime(97) is True
        assert is_prime(101) is True
    
    def test_large_non_prime(self):
        """Test with a larger non-prime number."""
        assert is_prime(100) is False
        assert is_prime(99) is False
    
    def test_non_integer_input(self):
        """Test that non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Prime check requires an integer"):
            is_prime(3.5)
        
        with pytest.raises(TypeError, match="Prime check requires an integer"):
            is_prime("7")
        
        with pytest.raises(TypeError, match="Prime check requires an integer"):
            is_prime([7])


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**10
        assert self.calc.add(large_num, 1) == large_num + 1
        assert self.calc.multiply(large_num, 2) == large_num * 2
    
    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 1e-10
        assert self.calc.add(small_num, small_num) == 2 * small_num
        assert self.calc.multiply(small_num, 2) == 2 * small_num
    
    def test_floating_point_precision(self):
        """Test floating point precision issues."""
        # Use pytest.approx for floating point comparisons
        result = self.calc.add(0.1, 0.2)
        assert result == pytest.approx(0.3)
        
        result = self.calc.multiply(0.1, 3)
        assert result == pytest.approx(0.3)
    
    def test_mixed_integer_float_operations(self):
        """Test operations mixing integers and floats."""
        assert self.calc.add(5, 2.5) == 7.5
        assert self.calc.subtract(10, 3.3) == pytest.approx(6.7)
        assert self.calc.multiply(4, 2.5) == 10.0
        assert self.calc.divide(7, 2.0) == 3.5