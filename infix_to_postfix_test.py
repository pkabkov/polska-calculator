"""
Юнит-тесты для функции init_to_postfix, реализующей калькулятор в постфиксной записи.
"""

import pytest
from main import infix_to_postfix


def test_with_bad_brackets():
    """Тест с неверным расположением скобок вызывает ValueError."""
    with pytest.raises(ValueError):
        infix_to_postfix("( 1 + 2 ( )")


def test_priority_with_brackets():
    """Тест на верное распределение приоритетов со скобками"""
    assert infix_to_postfix("3 * ( 1 + 2 )") == "3 1 2 + *"


def test_priority_multiply():
    """Тест на верное распределение приоритетов у умножения"""
    assert infix_to_postfix("1 + 2 * 3") == "1 2 3 * +"

def test_priority_division():
    """Тест на верное распределение приоритетов у деления"""
    assert infix_to_postfix("1 + 2 / 3") == "1 2 3 / +"

def test_with_one_digit():
    """Тест на одну цифру в выражении"""
    assert infix_to_postfix("1") == "1"

def test_power_priority():
    """Степень имеет самый высокий приоритет"""
    assert infix_to_postfix("2 + 3 * 4 ^ 5") == "2 3 4 5 ^ * +"

def test_power_right_associativity():
    """^ должен быть правоассоциативным"""
    assert infix_to_postfix("2 ^ 3 ^ 2") == "2 3 2 ^ ^"
