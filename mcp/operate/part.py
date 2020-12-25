from ..source import data
from .exceptions import InvalidFileError

__all__ = ["get_part", "get_parts"]


def get_part(file, part_name, **options):
    """
    If part_name is invalid, return None
    Else, return Part

    options:
            check_file(Type: bool, Default: True): If True, will check file_name before try to get part
            check_part(Type: bool, Default: True): If True, will check part_name before try to get part
    """
    valid_option = {"check_file": True, "check_part": True}

    # Basic check
    if not check.option_check(options, valid_option):
        return

    # Filling options
    options = fill_dic(valid_option, options)

    # Optional check
    if options["check_file"] and not check.file_check(file_name):
        return

    part_list = get_part_list(file_name)  # move for avoid use get_part_list twice

    if options["check_part"] and not check.part_check(
        file_name, part_name, check_file=False, part_list=part_list
    ):
        return

    # Support use int instead part's name
    if type(part_name) == int:
        part_name = part_list[part_name - 1]

    # Try get file
    try:
        file = getattr(data, file_name)
    # AttributeError -> invalid file_name -> check file_name for print error message
    except AttributeError:
        check.file_check(file_name)
        return

    # Try get part_data
    try:
        part_data = file.data[part_name]
    # KeyError -> invalid part_name -> check part_name for print error message
    except KeyError:
        check.part_check(file_name, part_name, check_file=False)
        return

    # Create Part
    part = Part(file_name, part_name, part_data)

    return part


def get_parts(file, part_names: list, **options):
    """
    get_part's advance version, can return mulit part at once
    """
    part_list = []

    for part_name in part_names:
        part = get_part(file, part_name, options)

        if part is None:
            return

        part_list.append(part)

    if len(part_list) == 1:
        return part_list[0]
    return part_list
