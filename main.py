from CreateProject import create_project
import os.path
from os import path
def main():
    while True:
        print("1.Створити проект.\n"
              "2.Змінити проект.\n"
              "3.Видалити проект.\n"
              "4.Створити завдання для проекту.\n"
              "5.Змінити завдання для проекту.\n"
              "6.Видалити завдання для проекту.\n"
              "7.Призначити відповідальних проекту.\n"
              "8.Встановити дедлайн проекту.")

        choice = input("Введіть ваш вибір: ")
        if choice == "1":
            create_project()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass


main()