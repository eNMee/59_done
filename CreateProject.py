import os.path
from os import path


def create_project():
    name_project = input("Введіть назву проекта: ")
    if path.exists(name_project):
        print(f"Project {name_project} already exists")
    else:
        os.mkdir(name_project)
        with open(f"{name_project}/{name_project}.txt", "w"):
            print(f"Project {name_project} was created!")



