import sys
from pathlib import Path
import os

from utils.config import *


def init_fs(called_path: str) -> None:
    fs_path = os.path.join(called_path, FS_OBJECTS)
    db_path = os.path.join(called_path, DATABASE_PATH)

    os.makedirs(fs_path, exist_ok=True)
    print("FS success initialized!")

    Path(db_path).touch(exist_ok=True)
    print("Database success created!")


def init_fs_helper(*args) -> bool:
    if len(args) != 0:
        print("Command 'init' doesn't take any arguments!")
        return False

    called_path = os.getcwd()
    init_path = os.path.join(called_path, BASE_FS_PATH)

    if Path(init_path).is_dir():
        print("FS already initialized!")
        return False

    init_fs(called_path)


if __name__ == '__main__':
    _, *args = sys.argv
    init_fs_helper(*args)
