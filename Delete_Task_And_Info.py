import os.path
from os import path
import shutil


def delete_task_and_info():
    try:

        name_project = input("Введіть назву проекта: ")
        if path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
            os.remove(f"{name_project}/{name_project}_Task_Info.txt")
            print(f"Task and info about {name_project} was deleted!")
        else:
            print("Project Task and info doesn`t exist!")

    except KeyboardInterrupt as e:
        print("\nError: keyboard interrupt!")
