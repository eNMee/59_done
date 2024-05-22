import os.path
from os import path


def change_task():
    name_project = input("Введіть назву проекта:")
    if path.exists(f"{name_project}/{name_project}.txt"):
        if path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
            new_info = []
            with open(f"{name_project}/{name_project}_Task_Info.txt", "r") as info_task:
                info = info_task.readlines()
                info[3] = "Task: " + input("Введіть завдання для проекту: ")
                new_info = info
                with open(f"{name_project}/{name_project}_Task_Info.txt", "w") as f:
                    f.writelines(new_info)
                print(f"Task for project {name_project} was changed")
        else:
            print(f"Task for project {name_project} already exists")
    else:
        print("Created project before created task for project!")