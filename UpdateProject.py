import os.path
from os import path


def update_project():
    try:

        name_project = input("Введіть назву проекта: ")
        if path.exists(f"{name_project}/{name_project}.txt"):
            with open(f"{name_project}/{name_project}.txt", "a") as project:
                updating_of_project = input("Введіть оновлення: ") + "\n"
                project.write(updating_of_project)
                print(f"Project {name_project} was updated")
        else:
            print("Project doesn`t exist")

    except KeyboardInterrupt as e:
        print("\nError: keyboard interrupt!")
