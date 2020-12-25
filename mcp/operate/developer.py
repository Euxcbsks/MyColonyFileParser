import os

from ..tools.path import run_here, rela_chdir

__all__ = ["del_pycache"]


def deep_file_finder(path, targets):
    """
    path:
            Type: PathLike
            Description: Path for start search
    targets:
            Type: File name, folder name or a list of both
            Description: Names ending with slash(/) will be judged as folder names.
                    Else will be judged as file names
    """
    listdir = os.listdir(path)
    target_list = []

    if type(targets) != list:
        targets = list(targets)

    for target in targets:
        # For folder
        if target.endswith("/"):
            target = target[:-1]

            for folder in listdir:
                if folder == target:
                    target_list.append(os.path.abspath(folder))

                if os.path.isdir(folder):
                    target_list.append(deep_file_finder(folder, f"{target}/"))
        # For file
        else:
            pass
    return target_list


@run_here
def del_pycache():
    os.chdir("..")
    target_list = deep_file_finder(os.getcwd(), "__pycache__/")

    for target in target_list:
        pass
