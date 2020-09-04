#!/usr/bin/env python3 -m pytest
"""[summary]
"""
import pytest
import io
import fibonacci
import filecmp

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

def test_fibonacci_generator_0_to_0():
    """[summary]
    We use next to be sure the function is a generator
    """
    generated = fibonacci.fibonacci(0)
    expected = [0]
    for i in expected:
        assert next(generated) == i
        
def test_fibonacci_generator_0_to_1():
    """[summary]
    We use next to be sure the function is a generator
    """
    generated = fibonacci.fibonacci(1)
    expected = [0, 1]
    for i in expected:
        assert next(generated) == i

def test_fibonacci_generator_0_to_6():
    """[summary]
    We use next to be sure the function is a generator
    """
    generated = fibonacci.fibonacci(6)
    expected = [0, 1, 1, 2, 3, 5]
    for i in expected:
        assert next(generated) == i

def test_to_file(tmpdir):
    expected_file = tmpdir.join('expected')
    with open(expected_file, 'a') as out:
       out.write('0' + '\n')
       out.write('1' + '\n')
    fib_file = tmpdir.join('fibonacci_1')
    g = fibonacci.fibonacci(1)
    fibonacci.to_file(fib_file, g) 
    assert filecmp.cmp(expected_file, fib_file, shallow=False)

def test_check_and_rename():
    pass