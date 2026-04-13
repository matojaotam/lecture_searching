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

# def binary_search(num_list, num_search):
#     return num_index

def binary_search(num_list, num_search):
    leva = 0
    prava= len(num_list) - 1

    while leva <= prava:
        mid = (leva + prava) // 2
        if num_list[mid] == num_search:
            return mid
        elif num_list[mid] < num_search:
            leva = mid + 1
        else:
            prava = mid - 1
    return None



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

    ordered_data = read_data("sequential.json", "ordered_numbers")
    index = binary_search(ordered_data, num_search)
    print(index)
if __name__ == "__main__":
    main()


