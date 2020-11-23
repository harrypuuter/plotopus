import logging
import os.path
from rich.traceback import install

install()
logger = logging.getLogger(__name__)


def get_absolute_path(filepath):
    return os.path.abspath(filepath)


def save_create_folder(path):
    folder = get_absolute_path(path)
    if check_folder_exists(folder):
        return folder
    else:
        try:
            os.makedirs(folder)
        except OSError:
            print("Creation of the directory %s failed" % (folder))
        else:
            print("Successfully created the directory %s" % (folder))
    return folder


def check_file_exists(file):
    if not os.path.isfile(get_absolute_path(file)):
        print("File {} not found ")
        return False
    return True


def check_folder_exists(folder):
    if not os.path.isdir(get_absolute_path(folder)):
        print("File {} not found ")
        return False
    return True
