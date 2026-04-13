from pathlib import Path
import json


def read_data(file_name, field):

    with open(file_name, "r") as file:
        data = json.load(file)
    if field not in data:
        return None

    return data[field]

# def linear_search(sequence, num_search):
#     return positions, count

# positions = []
# for i, hodnota in enumerate(sequence):
#     if hodnota == num_search:
#         positions.append(i)


def linear_search(sequence, num_search):
    positions = []
    for i, hodnota in enumerate(sequence):
        if hodnota == num_search:
            positions.append(i)

    return {"positions": positions, "count": len(positions)}
# # get current working directory path
    # cwd_path = Path.cwd()
    #
    # file_path = cwd_path / file_name


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    num_search = sequential_data[0]

    result = linear_search(sequential_data, num_search)
    print(result)

if __name__ == "__main__":
    main()


