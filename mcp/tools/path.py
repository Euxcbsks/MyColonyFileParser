import os
import inspect

__all__ = ["run_here", "rela_chdir"]


def run_here(func):
    # Get orig_path, func_path
    orig_path = os.getcwd()
    func_frame = inspect.currentframe().f_back
    func_frame_info = inspect.getframeinfo(func_frame)
    func_path = os.path.split(func_frame_info.filename)[0]
    del func_frame, func_frame_info

    def run_here_func(*args):
        # Move to the location of the function
        os.chdir(func_path)
        # Get function return value
        func_return = func(*args)
        # Restore work directory
        os.chdir(orig_path)
        return func_return

    return run_here_func


def rela_chdir(path):
    """
    path:
            Type: PathLike
    """
    # For '../path' or '..'
    if path.startswith(".."):
        # For '../path'
        if "/" in path:
            path = path.split("/", 1)

            while len(path[0]) - 1:
                path[0] = path[0][1:]
                os.chdir("..")

            os.chdir(path[1])
        # For '..'
        else:
            while len(path) - 1:
                os.chdir("..")
                path = path[1:]
    # Normal path
    else:
        os.chdir(path)
