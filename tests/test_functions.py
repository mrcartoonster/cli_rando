# -*- coding: utf-8 -*-
"""
Will have the tests for functions here.
"""
from src.tempo_random.functions import tempo_generate


def test_generate():
    """
    Testing tempo_generate the numbers are random.
    """
    first = tempo_generate(50, 100)
    second = tempo_generate(50, 100)

    assert first != second


def test_default():
    """
    Test the defualt which is 50 and 100.
    """
    sample = tempo_generate(50, 100)
    assert sample >= 50 and sample <= 100


def test_multiples(numbers):
    """
    Testing multiples.
    """
    sample = tempo_generate(*numbers)
    assert sample >= numbers[0] and sample <= numbers[1]
