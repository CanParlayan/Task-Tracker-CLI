import json
import os


def file_exists(file_path):
    return os.path.exists(file_path)


def json_read(file_path):
    if not file_exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return None
    try:
        with open(file_path, 'r') as file:
            return json.load(file)

    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None


def json_write(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
        return False
    return True


def append_to_json(file_path, new_data):
    if not file_exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False

    try:

        data = json_read(file_path)
        if data is None:
            return False

        if isinstance(data, list):
            data.append(new_data)
        elif isinstance(data, dict):
            data.update(new_data)
        else:
            print("Error: Unsupported JSON structure.")
            return False

        return json_write(file_path, data)
    except Exception as e:
        print(f"Error appending to file '{file_path}': {e}")
        return False
