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


def test_common_tempo():
    """Testing default common-tempo which is
    between 73 and 77"""
    result = runner.invoke(app, ["common-tempo"])
    assert result.exit_code == 0
