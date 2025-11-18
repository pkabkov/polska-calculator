"""
Юнит-тесты для функции polska, реализующей калькулятор в постфиксной записи.
"""

import pytest
from main import polska


def test_addition():
    """Тест простого сложения."""
    assert polska("2 3 +") == 5  # (2 + 3)


def test_multiplication_after_addition():
    """Тест умножения после сложения."""
    assert polska("2 3 + 4 *") == 20  # (2 + 3) * 4


def test_addition_after_multiplication():
    """Тест сложения после умножения."""
    assert polska("2 3 4 * +") == 14  # 2 + (3 * 4)


def test_complex_expression():
    """Тест сложного выражения с несколькими операторами."""
    assert polska("100 70 20 5 6 * + - /") == 5  # 100 / (70 - (20 + (5 * 6)))


def test_single_number():
    """Тест выражения с одним числом."""
    assert polska("7") == 7


def test_operators_fallout():
    """
    Тест неверного выражения, состоящего только из операторов,
    выдаёт ValueError.
    """
    with pytest.raises(ValueError):
        polska("- + / *")


def test_division_by_zero():
    """Тест деления на ноль вызывает ValueError."""
    with pytest.raises(ValueError):
        polska("1 0 /")


def test_without_operators():
    """Тест неправильного выражения без операторов вызывает ValueError."""
    with pytest.raises(ValueError):
        polska("1 2 3")


def test_with_wrong_arguments():
    """Тест с неверными символами внутри вызывает ValueError"""
    with pytest.raises(ValueError):
        polska("a b +")


def test_power():
    """Тест возведения в степень."""
    assert polska("2 3 ^") == 8


def test_power_chain():
    """Тест правоассоциативности для степени."""
    assert polska("2 3 2 ^ ^") == 512  # 2 ^ (3^2) = 2^9 = 512


def test_power_with_other_ops():
    """Тест степени вместе с другими операциями."""
    assert polska("2 3 + 2 ^") == 25  # (2+3)^2
