import os.path
from os import path


def create_task():
    name_project = input("Введіть назву проекта: ")
    if path.exists(f"{name_project}/{name_project}.txt"):
        if not path.exists(f"{name_project}/ {name_project}_Task.txt"):
            with open(f"{name_project}/ {name_project}_Task_Info.txt", "w") as task:
                text_task = "Task: " + input("Введіть завдання для проекту: ")
                deadline = "Deadline: " + input("Введіть deadline: ")
                status = "Status: " + input("Статус завдання: ")
                res_person = "Res_person: " + input("Введіть відповідальну особу: ")
                task.writelines([res_person + "\n", deadline + "\n", status + "\n", text_task])
                print(f"Task for project {name_project} was created")
        else:
            print(f"Task for project {name_project} already exists")
    else:
        print("Created project before created task for project!")