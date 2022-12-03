# -*- coding: utf-8 -*-
"""
Tempo app.
"""
import typer
from rich import print as rprint

from tempo_random.functions import Tempo, TempoList, tempo_generate

app = typer.Typer(
    name="Tempo",
    help="Quick function to generate random numbers",
    add_completion=False,
)


@app.command()
def tempo(
    start: int = typer.Argument(50, help="Start number"),
    stop: int = typer.Argument(100, help="Stop number"),
    tempo: TempoList = typer.Option(
        TempoList.ANDANTE.value,
        help="Choose common music tempo",
        rich_help_panel="Setting Tempos",
    ),
):
    """
    Enter start number and stop number to randomly select a tempo time.
    """
    if tempo:
        beat = tempo_generate(*Tempo[tempo].value)
        rprint(f"[bold green]Set tempo at:[/] [bold blue]{beat}[/]")
    beat = tempo_generate(start, stop)
    rprint(f"[bold green]Set tempo at:[/] [bold blue]{beat}[/]")


if __name__ == "__main__":
    app()