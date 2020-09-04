#!/usr/bin/env python3 -m pytest
"""[summary]
"""
import pytest
import os
import fibonacci
import filecmp
import freezegun


def test_check_non_numeric(mocker):
    """With this function we test che check related to
    non-numeric value passed to our script
    """
    # We mock the input to simulate a wrong input
    mocker.patch('builtins.input', lambda *args: 'a')
    with pytest.raises((ValueError, SystemExit)):
        fibonacci.main()


def test_check_positive(mocker):
    """With this function we test che check related to
    negative number passed to our script
    """
    mocker.patch('builtins.input', lambda *args: '-3')
    with pytest.raises(SystemExit):
        fibonacci.main()


def test_fibonacci_generator_0_to_0():
    """This function test fibonacci for 0 value
    """
    generated = fibonacci.fibonacci(0)
    expected = [0]
    for i in expected:
        # We use next to be sure the function is a generator
        assert next(generated) == i


def test_fibonacci_generator_0_to_1():
    """This function test fibonacci for 1 value
    """
    generated = fibonacci.fibonacci(1)
    expected = [0, 1]
    for i in expected:
        assert next(generated) == i


def test_fibonacci_generator_0_to_6():
    """This function test fibonacci for 6 value
    """
    generated = fibonacci.fibonacci(6)
    expected = [0, 1, 1, 2, 3, 5]
    for i in expected:
        assert next(generated) == i


@freezegun.freeze_time("Jan 8th, 2020 10:22:17")
def test_check_and_rename(tmpdir):
    """This function test renaming function we use tmpdir from pytest
    we use also freezegun to mock datetime
    """
    start_file = tmpdir.join('test_rename')
    renamed_file = tmpdir.join('test_rename_08-01-2020-10-22-17')
    open(start_file, 'a').close()
    fibonacci.check_and_rename(str(start_file))
    # Check if the file renamed has correct name
    assert os.path.isfile(renamed_file)


def test_to_file(tmpdir):
    """This function test to_file function that write results
    on file we use tmpdir from pytest
    We use also freezegun to mock datetime
    """
    expected_file = tmpdir.join('expected')
    with open(expected_file, 'a') as out:
        out.write('0' + '\n')
        out.write('1' + '\n')
    fib_file = tmpdir.join('fibonacci_1')
    g = fibonacci.fibonacci(1)
    fibonacci.to_file(fib_file, g)
    # Compare our expected file with the generated one by the function
    assert filecmp.cmp(expected_file, fib_file, shallow=False)
