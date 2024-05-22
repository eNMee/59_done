import os.path
from os import path


def create_task():
    name_project = input("Введіть назву проекта: ")
    if path.exists(f"{name_project}/{name_project}.txt"):
        with open(f"{name_project}/ {name_project}_Task.txt", "w") as task:
            text_task = input("Введіть завдання для проекту: ")
            task.write(text_task)
            print(f"Task for project {name_project} was created")
    else:
        print("Created project before created task for project!")