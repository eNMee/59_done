import os.path
from os import path
import shutil


def delete_project():
    name_project = input("Введіть назву проекта: ")
    if path.exists(f"{name_project}/{name_project}.txt"):
        shutil.rmtree(name_project)
        print(f"Project {name_project} was deleted!")
    else:
        print("Project doesn`t exist!")