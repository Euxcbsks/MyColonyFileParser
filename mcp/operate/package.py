import os

from ..tools.path import run_here
from ..source.data import game

__all__ = ["get_package_source_version"]


@run_here
def get_package_source_version():
    os.chdir("..")
    return game.data["meta"]["buildVersion"]
