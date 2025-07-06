import argparse

from task_functions import *


def main():
    parser = argparse.ArgumentParser("Simple Task Tracker CLI App")
    parser.description = "A CLI app to track your tasks and manage your to-do list."
    parser.add_argument("command", choices=["add", "list", "update", "delete", "mark-in-progress", "mark-done"],
                        help="Command to execute")
    parser.add_argument("args", nargs="*", help="Additional arguments for the command")

    args = parser.parse_args()

    if args.command == "add":
        if len(args.args) < 1:
            print("Error: Description is required for adding a task.")
            return
        description = " ".join(args.args)
        add_task("tasks.json", description)
    elif args.command == "list":
        if len(args.args) < 1:
            list_tasks("tasks.json")
        else:
            status = " ".join(args.args)
            list_tasks("tasks.json", status)
    elif args.command == "update":
        if len(args.args) < 2:
            print("Error: Task ID and description are required for updating a task.")
            return
        task_id = args.args[0]
        description = " ".join(args.args[1:])
        update_task("tasks.json", task_id, description)
    elif args.command == "delete":
        if len(args.args) < 1:
            print("Error: Task ID is required for deleting a task.")
            return
        task_id = args.args[0]
        delete_task("tasks.json", task_id)
    elif args.command == "mark-in-progress":
        if len(args.args) < 1:
            print("Error: Task ID is required for marking a task as in-progress.")
            return
        task_id = args.args[0]
        mark_in_progress("tasks.json", task_id)

    elif args.command == "mark-done":
        if len(args.args) < 1:
            print("Error: Task ID is required for marking a task as done.")
            return
        task_id = args.args[0]
        mark_done("tasks.json", task_id)
    else:
        print(f"Error: Unknown command '{args.command}'.")


if __name__ == "__main__":
    main()
