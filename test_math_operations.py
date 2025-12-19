import pytest
from math_operations import (
    add_numbers, 
    multiply_numbers, 
    Calculator
)


class TestAddNumbers:
    """Тесты для функции add_numbers()"""
    
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        result = add_numbers(2, 3)
        assert result == 5.0
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        result = add_numbers(-2, -3)
        assert result == -5.0
    
    def test_add_mixed_numbers(self):
        """Тест сложения чисел с разными знаками"""
        result = add_numbers(10, -5)
        assert result == 5.0
    
    def test_add_floats(self):
        """Тест сложения дробных чисел"""
        result = add_numbers(3.5, 2.5)
        assert result == 6.0
    
    def test_add_zero(self):
        """Тест сложения с нулем"""
        result = add_numbers(10, 0)
        assert result == 10.0
        
    def test_add_large_numbers(self):
        """Тест сложения больших чисел"""
        result = add_numbers(1_000_000, 2_000_000)
        assert result == 3_000_000.0


class TestMultiplyNumbers:
    """Тесты для функции multiply_numbers()"""
    
    def test_multiply_positive_numbers(self):
        """Тест умножения положительных чисел"""
        result = multiply_numbers(3, 4)
        assert result == 12.0
    
    def test_multiply_negative_numbers(self):
        """Тест умножения отрицательных чисел"""
        result = multiply_numbers(-3, -4)
        assert result == 12.0
    
    def test_multiply_mixed_signs(self):
        """Тест умножения чисел с разными знаками"""
        result = multiply_numbers(3, -4)
        assert result == -12.0
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        result = multiply_numbers(10, 0)
        assert result == 0.0
    
    def test_multiply_fractions(self):
        """Тест умножения дробных чисел"""
        result = multiply_numbers(2.5, 4.0)
        assert result == 10.0
        
    def test_multiply_by_one(self):
        """Тест умножения на единицу"""
        result = multiply_numbers(7, 1)
        assert result == 7.0


class TestCalculatorClass:
    """Тесты для класса Calculator"""
    
    def test_calculator_default_name(self):
        """Тест создания калькулятора с именем по умолчанию"""
        calc = Calculator()
        assert calc.name == "Калькулятор"
    
    def test_calculator_custom_name(self):
        """Тест создания калькулятора с пользовательским именем"""
        calc = Calculator("Мой калькулятор")
        assert calc.name == "Мой калькулятор"
    
    def test_power_positive(self):
        """Тест возведения в положительную степень"""
        calc = Calculator()
        result = calc.power(2, 3)
        assert result == 8.0
    
    def test_power_zero_exponent(self):
        """Тест возведения в нулевую степень"""
        calc = Calculator()
        result = calc.power(5, 0)
        assert result == 1.0
    
    def test_power_one_exponent(self):
        """Тест возведения в первую степень"""
        calc = Calculator()
        result = calc.power(7, 1)
        assert result == 7.0
    
    def test_power_negative_exponent(self):
        """Тест возведения в отрицательную степень"""
        calc = Calculator()
        result = calc.power(2, -2)
        assert result == 0.25
    
    def test_power_fractional_exponent(self):
        """Тест возведения в дробную степень"""
        calc = Calculator()
        result = calc.power(4, 0.5)
        assert result == 2.0
    
    def test_power_zero_base(self):
        """Тест возведения нуля в степень"""
        calc = Calculator()
        result = calc.power(0, 5)
        assert result == 0.0


class TestEdgeCases:
    """Тесты крайних случаев"""
    
    def test_add_very_small_numbers(self):
        """Тест сложения очень маленьких чисел"""
        result = add_numbers(0.000001, 0.000002)
        assert result == 0.000003
    
    def test_multiply_very_large_numbers(self):
        """Тест умножения очень больших чисел"""
        result = multiply_numbers(1e10, 2e10)
        assert result == 2e20
    
    def test_power_large_numbers(self):
        """Тест возведения в очень большую степень"""
        calc = Calculator()
        result = calc.power(10, 10)
        assert result == 10_000_000_000.0


class TestParameterized:
    """Параметризованные тесты"""
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0.0),
        (1, 1, 2.0),
        (-1, 1, 0.0),
        (100, -100, 0.0),
        (0.1, 0.2, 0.3),
    ])
    def test_add_numbers_parametrized(self, a, b, expected):
        """Параметризованный тест сложения"""
        result = add_numbers(a, b)
        # Используем приблизительное сравнение для чисел с плавающей точкой
        if isinstance(expected, float):
            assert result == pytest.approx(expected)
        else:
            assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 5, 1.0),
        (2, 3, 8.0),
        (5, 0, 1.0),
        (10, -1, 0.1),
    ])
    def test_power_parametrized(self, a, b, expected):
        """Параметризованный тест возведения в степень"""
        calc = Calculator()
        result = calc.power(a, b)
        assert result == pytest.approx(expected)


if __name__ == "__main__":
    # Запуск тестов напрямую
    pytest.main([__file__, "-v"])