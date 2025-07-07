from typing import List

import argparse

from Task import logger
from TaskManager import TaskManager


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(
        prog='task-cli',
        description='📋 A powerful CLI task tracker',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
task-cli add "Buy groceries"
task-cli list
task-cli list done
task-cli update 1 "Buy groceries and cook dinner"
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli delete 1
        """
    )

    parser.add_argument(
        'command',
        choices=['add', 'list', 'update', 'delete', 'mark-in-progress', 'mark-done'],
        help='Command to execute'
    )

    parser.add_argument(
        'args',
        nargs='*',
        help='Additional arguments for the command'
    )

    return parser


class TaskCLI:
    """Command line interface for task management"""

    def __init__(self):
        self.task_manager = TaskManager()

    def run(self):
        """Run the CLI application"""
        parser = create_parser()
        args = parser.parse_args()

        try:
            if args.command == 'add':
                self._handle_add(args.args)
            elif args.command == 'list':
                self._handle_list(args.args)
            elif args.command == 'update':
                self._handle_update(args.args)
            elif args.command == 'delete':
                self._handle_delete(args.args)
            elif args.command == 'mark-in-progress':
                self._handle_mark_in_progress(args.args)
            elif args.command == 'mark-done':
                self._handle_mark_done(args.args)
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"❌ An error occurred: {e}")

    def _handle_add(self, args: List[str]):
        """Handle add command"""
        if not args:
            print("❌ Error: Description is required for adding a task")
            print("Usage: task-cli add \"Task description\"")
            return

        description = " ".join(args)
        self.task_manager.add_task(description)

    def _handle_list(self, args: List[str]):
        """Handle list command"""
        status_filter = " ".join(args) if args else None
        self.task_manager.list_tasks(status_filter)

    def _handle_update(self, args: List[str]):
        """Handle update command"""
        if len(args) < 2:
            print("❌ Error: Task ID and description are required")
            print("Usage: task-cli update <task_id> \"New description\"")
            return

        try:
            task_id = int(args[0])
            description = " ".join(args[1:])
            self.task_manager.update_task(task_id, description)
        except ValueError:
            print("❌ Error: Task ID must be a number")

    def _handle_delete(self, args: List[str]):
        """Handle delete command"""
        if not args:
            print("❌ Error: Task ID is required for deleting a task")
            print("Usage: task-cli delete <task_id>")
            return

        try:
            task_id = int(args[0])
            self.task_manager.delete_task(task_id)
        except ValueError:
            print("❌ Error: Task ID must be a number")

    def _handle_mark_in_progress(self, args: List[str]):
        """Handle mark-in-progress command"""
        if not args:
            print("❌ Error: Task ID is required")
            print("Usage: task-cli mark-in-progress <task_id>")
            return

        try:
            task_id = int(args[0])
            self.task_manager.mark_in_progress(task_id)
        except ValueError:
            print("❌ Error: Task ID must be a number")

    def _handle_mark_done(self, args: List[str]):
        """Handle mark-done command"""
        if not args:
            print("❌ Error: Task ID is required")
            print("Usage: task-cli mark-done <task_id>")
            return

        try:
            task_id = int(args[0])
            self.task_manager.mark_done(task_id)
        except ValueError:
            print("❌ Error: Task ID must be a number")


def main():
    """Main entry point"""
    cli = TaskCLI()
    cli.run()


if __name__ == "__main__":
    main()
