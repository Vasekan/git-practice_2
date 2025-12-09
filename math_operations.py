# math_operations.py

def add_numbers(a: float, b: float) -> float:
    """
    Складывает два числа.
    
    Args:
        a: Первое число
        b: Второе число
        
    Returns:
        Сумма a и b
        
    Examples:
        >>> add_numbers(2, 3)
        5.0
        >>> add_numbers(10.5, 5.5)
        16.0
    """
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """
    Умножает два числа.
    
    Args:
        a: Первый множитель
        b: Второй множитель
        
    Returns:
        Произведение a и b
    """
    return a * b

class Calculator:
    """Класс для математических операций."""
    
    def __init__(self, name="Калькулятор"):
        self.name = name
        
    def power(self, base: float, exponent: float) -> float:
        """
        Возводит число в степень.
        
        Args:
            base: Основание
            exponent: Показатель степени
            
        Returns:
            base ** exponent
        """
        return base ** exponent