# -*- coding: utf-8 -*-
"""
pytest fixtures.
"""

import pytest

set_tempos = [(50, 60), (60, 70), (70, 80)]
tempo_ids = [str(_) for _ in set_tempos]

tempo_names = ["Andante", "Moderato", "Allegretto", "Allegro"]


@pytest.fixture(name="numbers", params=set_tempos, ids=tempo_ids)
def return_tempos(request):
    """
    Returning a list of tempos.
    """
    return request.param


@pytest.fixture(name="random", params=tempo_names)
def random_tempo_names(request):
    """
    Fixture for random tempo names.
    """
    return request.param
