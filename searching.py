from pathlib import Path
import json
import time
from generators import unordered_sequence, ordered_sequence

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
#
import matplotlib.pyplot as plt         #zkusebni graf
#
# sizes = [100, 500, 1000, 5000, 10000]
# times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]
#
# plt.plot(sizes, times)
#
# plt.xlabel("Velikost vstupu")
# plt.ylabel("Čas [s]")
# plt.title("Ukázkový graf měření")
# plt.show()

def compare_search():
    velikosti = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []

    for velikost in velikosti:

        unordered = unordered_sequence(velikost)
        ordered = ordered_sequence(velikost)

        target = unordered[-1]

        start = time.time()
        linear_search(unordered, target)
        end = time.time()
        linear_times.append(end - start)


        start = time.time()
        binary_search(ordered, target)
        end = time.time()
        binary_times.append(end - start)

        #graf zobrazeni
    plt.figure()
    plt.plot(velikosti, linear_times, label='Linear Search')
    plt.plot(velikosti, binary_times, label='Binary Search')

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání lineárního a binárního vyhledávání")
    plt.legend()
    plt.show()



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

    compare_search()
if __name__ == "__main__":
    main()


