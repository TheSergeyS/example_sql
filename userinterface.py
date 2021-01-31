import  datastorage
import datetime as dt

def promt_for_operations_with_db():

    while True:
        print()
        print("What would you like to do?")
        print()
        print(" A = add a task.")
        print(" C = complete a task.")
        print(" S = select all tasks.")
        print(" Q = quit.")
        print()
        action = input(">").strip().upper()
        if action == "A":
            return "ADD"
        elif action == "C":
            return "COMPLETE"
        elif action == "S":
            return "SELECT"
        elif action == "Q":
            return "QUIT"
        else:
            print("Unknown action!")

def promt_for_new_task():

    description_task = input("input the Descripition a new task:")
    return description_task

def promt_duedate_for_task():

    while True:

        duedate_task_str = input("input the DueDate a new task (format:DD.MM.YEAR):")

        try:
            duedate_task = dt.datetime.strptime(duedate_task_str, "%d.%m.%Y")
            return duedate_task
        except ValueError:
            pass

def promt_complete_task():

    while True:

        id_task_str = input("input ID task to complete:")

        try:
            id_task = int(id_task_str)
            return id_task
        except ValueError:
            pass