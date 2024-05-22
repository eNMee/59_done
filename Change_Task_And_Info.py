import os.path
from os import path


def change_task_and_info():
    try:

        name_project = input("Введіть назву проекта:")
        if path.exists(f"{name_project}/{name_project}.txt"):
            if path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
                new_info = []
                choice = input("1.Змініти відповідального.\n"
                               "2.Змінити deadline.\n"
                               "3.Змінити статус.\n"
                               "4.Змінити завдання.\n"
                               "Введіть ваш вибір: ")

                with open(f"{name_project}/{name_project}_Task_Info.txt", "r") as info_task:
                    info = info_task.readlines()
                    if choice == "1":
                        info[0] = "Res_person: " + input("Введіть відповідальну особу: ") + "\n"
                        new_info = info
                    elif choice == "2":
                        info[1] = "Deadline: " + input("Введіть deadline: ") + "\n"
                        new_info = info
                    elif choice == "3":
                        info[2] = "Status: " + input("Статус завдання: ") + "\n"
                        new_info = info
                    elif choice == "4":
                        info[3] = "Task: " + input("Введіть завдання для проекту: ")
                        new_info = info
                    with open(f"{name_project}/{name_project}_Task_Info.txt", "w") as f:
                        f.writelines(new_info)
                    print(f"Task for project {name_project} was changed")
            else:
                print(f"Task for project {name_project} already exists")
        else:
            print("Created project before created task for project!")

    except KeyboardInterrupt as e:
        print("\nError: keyboard interrupt!")