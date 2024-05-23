import shutil
import unittest
import os.path
from os import path


class TestingModuls(unittest.TestCase):

    def test_create_project_true(self):

        name_project = "TestProject"
        if path.exists(name_project):
            pass
        else:
            os.mkdir(name_project)
            with open(f"{name_project}/{name_project}.txt", "w"):
                pass
        if path.exists(f"{name_project}/{name_project}.txt"):
            res = True

        self.assertEqual(res,True)

    def test_update_project(self):
        name_project = "TestProject"
        if path.exists(f"{name_project}/{name_project}.txt"):
            with open(f"{name_project}/{name_project}.txt", "a") as project:
                updating_of_project = "Test text" + "\n"
                project.write(updating_of_project)
            with open(f"{name_project}/{name_project}.txt", "r") as project:
                list = [i for i in project.readlines()]

                self.assertEqual(["Test text" + "\n"], list)

    def test_create_task_true(self):
        name_project = "TestProject"
        if path.exists(f"{name_project}/{name_project}.txt"):
            if not path.exists(f"{name_project}/{name_project}_Task.txt"):
                with open(f"{name_project}/{name_project}_Task_Info.txt", "w") as task:
                    text_task = "Task: " + "Buy a car"
                    deadline = "Deadline: " + "12.12.2024"
                    status = "Status: " + "Active"
                    res_person = "Res_person: " + "Den"
                    task.writelines([res_person + "\n", deadline + "\n", status + "\n", text_task])

        with open(f"{name_project}/{name_project}_Task_Info.txt", "r") as f:
            list = [i for i in f.readlines()]

        self.assertEqual([res_person + "\n", deadline + "\n", status + "\n", text_task], list)

    def test_change_task_and_info_true(self):
        name_project = "TestProject"
        if path.exists(f"{name_project}/{name_project}.txt"):
            if path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
                new_info = []
                choice = "1"
                with open(f"{name_project}/{name_project}_Task_Info.txt", "r") as info_task:
                    info = info_task.readlines()
                    if choice == "1":
                        info[0] = "Res_person: " + "Alex" + "\n"
                        new_info = info
                        info[1] = "Deadline: " + "11.11.2024" + "\n"
                        new_info = info
                        info[2] = "Status: " + "Inactive" + "\n"
                        new_info = info
                        info[3] = "Task: " + "Buy a bike"
                        new_info = info
                    with open(f"{name_project}/{name_project}_Task_Info.txt", "w") as f:
                        f.writelines(new_info)

                with open(f"{name_project}/{name_project}_Task_Info.txt", "r") as info_task:
                    info = [i for i in info_task.readlines()]

                    self.assertEqual(["Res_person: " + "Alex" + "\n",
                                      "Deadline: " + "11.11.2024" + "\n",
                                      "Status: " + "Inactive" + "\n",
                                      "Task: " + "Buy a bike"
                                      ],info)

    def test_delete_task_and_info_true(self):

        name_project = "TestProject"
        if path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
            os.remove(f"{name_project}/{name_project}_Task_Info.txt")
        if not path.exists(f"{name_project}/{name_project}_Task_Info.txt"):
            res = True

        self.assertEqual(res, True)

    def test_delete_project_true(self):
        name_project = "TestProject"
        if path.exists(f"{name_project}/{name_project}.txt"):
            shutil.rmtree(name_project)
        else:
            pass

        if not path.exists(f"{name_project}/{name_project}.txt"):
            res = True

        self.assertEqual(res, True)






