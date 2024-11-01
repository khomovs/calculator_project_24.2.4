import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_add_calculate_correctly(self):
        assert self.calc.add(2, 3) == 5

    def test_subtract_calculate_correctly(self):
        assert self.calc.subtract(5, 3) == 2

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 3) == 6

    def test_divide_calculate_correctly(self):
        assert self.calc.divide(6, 2) == 3

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(1, 0)