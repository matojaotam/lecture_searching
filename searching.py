from pathlib import Path
import json


def read_data(file_name, field):

    with open(file_name, "r") as file:
        data = json.load(file)
    if field not in data:
        return None

    return data[field]

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def main():



