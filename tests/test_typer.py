# -*- coding: utf-8 -*-
"""
Typer testing.
"""
from typer.testing import CliRunner

from src.tempo_random.main import app

runner = CliRunner()


def test_tempo_defualts():
    """
    Testing defaults.
    """
    result = runner.invoke(app, ["tempo"])
    assert result.exit_code == 0
    assert "Set tempo" in result.stdout
