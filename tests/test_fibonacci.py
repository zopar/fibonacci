#!/usr/bin/env python3 -m pytest
"""[summary]
"""
import pytest
import fibonacci

def test_check_non_numeric(mocker):
    """[summary]
    """
    mocker.patch('builtins.input', lambda *args: 'a')
    with pytest.raises((ValueError, SystemExit)):
        fibonacci.main()

def test_check_positive(mocker):
    mocker.patch('builtins.input', lambda *args: '-3')
    """[summary]
    """
    with pytest.raises(SystemExit):
        fibonacci.main()

def test_fibonacci_generator_0_to_6():
    """[summary]
    We use next to be sure the function is a generator
    """
    generated = fibonacci.fibonacci(6)
    expected = [0, 1, 1, 2, 3, 5]
    for i in expected:
        assert next(generated) == i
