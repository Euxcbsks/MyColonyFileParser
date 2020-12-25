from .self_check import get_latest_version_number, download_source

from ..operate.package import get_package_source_version
from ..operate.config import load_config

__all__ = ["check_update"]

config_data = load_config()


def check_update(auto_update=False):
    def update():
        download_source("game")
        download_source("strings")

    latest_version_number = get_latest_version_number()
    package_source_version = get_package_source_version()

    if latest_version_number != package_source_version:
        if auto_update == False:
            do_update = input(
                "The package source files have been updated. Do you want to update?(Y/N)\n> "
            )
            true_like = ["Y", "y"]
            false_like = ["N", "n"]

            while True:
                if do_update in true_like:
                    update()
                    break
                if do_update in false_like:
                    break
                do_update = input(
                    f'Invalid input "{do_update}", please enter again.(Y/N)\n> '
                )
        else:
            update()
    else:
        pass
