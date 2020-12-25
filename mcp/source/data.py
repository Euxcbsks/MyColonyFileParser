import json

from ..classes import SourceFile
from ..tools.path import run_here
from ..tools.data import format_source_data

__all__ = ["game", "strings"]


@run_here
def get_source_data(file):
    with open(f"{file}.js", "r", encoding="UTF-8") as game_file:
        data = format_source_data(game_file.read())
        data = json.loads(data, encoding="UTF-8")
        return data


game = SourceFile("game", get_source_data("game"))
strings = SourceFile("strings", get_source_data("strings"))
