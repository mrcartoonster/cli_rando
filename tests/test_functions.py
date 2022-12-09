# -*- coding: utf-8 -*-
"""
Will have the tests for functions here.
"""
import pytest

from src.tempo_random.functions import tempo_generate

set_tempos = [(50, 60), (60, 70), (70, 80)]
tempo_ids = [str(_) for _ in set_tempos]


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


@pytest.mark.smoke
@pytest.mark.parametrize("numbers", set_tempos, ids=tempo_ids)
def test_multiples(numbers):
    """
    Testing multiples.
    """
    sample = tempo_generate(*numbers)
    assert sample >= numbers[0] and sample <= numbers[1]
