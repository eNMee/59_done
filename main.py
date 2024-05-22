from Change_Task_And_Info import change_task_and_info
from CreateProject import create_project
import os.path
from os import path

from DeleteProject import delete_project
from Delete_Task_And_Info import delete_task_and_info
from UpdateProject import update_project
from CreateTask import create_task


def main():
    try:

        while True:
            print("1.Створити проект.\n"
                  "2.Оновити проект.\n"
                  "3.Видалити проект.\n"
                  "4.Створити завдання,статус,дедлайн та відповідального для проекту.\n"
                  "5.Змінити завдання,статус,дедлайн та відповідального для проекту.\n"
                  "6.Видалити завдання та інше для проекту.\n"
                  "7.Вихід")

            choice = input("Введіть ваш вибір: ")
            if choice == "1":
                create_project()
            elif choice == "2":
                update_project()
            elif choice == "3":
                delete_project()
            elif choice == "4":
                create_task()
            elif choice == "5":
                change_task_and_info()
            elif choice == "6":
                delete_task_and_info()
            elif choice == "7":
                break

    except KeyboardInterrupt as e:
        print("\nError: keyboard interrupt!")

main()
