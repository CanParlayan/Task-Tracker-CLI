# Task Tracker CLI

[Project Roadmap](https://roadmap.sh/projects/task-tracker)

The application runs from the command line, accepts user actions and inputs as arguments, and stores the tasks in a JSON file.

## Features

The user can:
- **Add**, **Update**, and **Delete** tasks
- Mark a task as **in progress** or **done**
- List all tasks
- List tasks by status: **todo**, **in-progress**, **done**

## Commands and Usage

### Adding a New Task

```bash
task-cli add "Buy groceries"
```

### Updating and Deleting Tasks

```bash
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

### Marking a Task as In Progress or Done

```bash
task-cli mark-in-progress 1
task-cli mark-done 1
```

### Listing All Tasks

```bash
task-cli list
```

### Listing Tasks by Status

```bash
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Installation

To run the script using `task-cli` instead of `.\taskcli.py`, you need to make the script executable and create a command alias or symbolic link.

### 1. Rename the script to `task-cli` (optional)

You can rename `taskcli.py` to `task-cli` for consistency, but this step is optional.

### 2. Add a shebang to the script

At the top of your `taskcli.py` file, add the following line to specify the Python interpreter:

```python
#!/usr/bin/env python3
```

### 3. Make the script executable

Run the following command in your terminal to make the script executable:

```bash
chmod +x TaskCLI.py
```

### 4. Move the script to a directory in your PATH

Move the script to a directory that is included in your system's `PATH`, such as `/usr/local/bin`:

```bash
mv TaskCLI.py /usr/local/bin/task-cli
```

### 5. Run the script

Now you can run the script using:

```bash
task-cli add "Read the book"
```