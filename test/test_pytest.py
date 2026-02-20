import pytest
import math
import sys
import os

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98


def test_profit_loss():
    assert calculator.profit_loss(100, 130) == 30
    assert calculator.profit_loss(100, 70) == -30
    assert calculator.profit_loss(100, 100) == 0


def test_simple_interest():
    assert calculator.simple_interest(1000, 10, 2) == 200
    assert calculator.simple_interest(5000, 5, 1) == 250
    assert calculator.simple_interest(1200, 7.5, 2) == 180


def test_compound_interest():
    assert math.isclose(calculator.compound_interest(1000, 10, 2), 210.0)
    assert math.isclose(
        calculator.compound_interest(1000, 12, 2, 4),
        266.7700813876163,
        rel_tol=1e-9,
    )
    assert math.isclose(calculator.compound_interest(1500, 7, 3), 337.5645000000002, rel_tol=1e-9)
