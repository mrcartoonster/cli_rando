# -*- coding: utf-8 -*-
"""
Functons for typer CLI.
"""
import secrets


def tempo_generate(first: int = 50, second: int = 100) -> int:
    """
    Simple random number function.
    """
    random_tempo = [_ for _ in range(first, second)]
    return secrets.choice(random_tempo)
