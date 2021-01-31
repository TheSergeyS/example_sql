import datastorage
import userinterface

def main():

    conn = datastorage.init()

    while True:
        action = userinterface.promt_for_operations_with_db()

        if action == "QUIT":
            break
        elif action == "ADD":
            new_task = userinterface.promt_for_new_task()
            if new_task != None:
                duedate_task = userinterface.promt_duedate_for_task()
                if duedate_task != None:
                    datastorage.add_task(conn, new_task, duedate_task)
        elif action == "SELECT":
            datastorage.read_all_tasks(conn)
        elif action == "COMPLETE":
            datastorage.read_all_tasks(conn)
            id_task = userinterface.promt_complete_task()
            if id_task != None:
                datastorage.mark_task_complete(conn, id_task)

if __name__ == '__main__':
    main()