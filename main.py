import math

data = [1, 2, 3]

def read_file_to_list(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        return [int(item) for item in lines]

def list_median_calculator(data):
    length = len(data)
    if length % 2 != 0:
        pos = int(math.floor(length/2))
        return float(data[pos])
    else:
        max_pos = length/2
        min_pos = max_pos - 1
        return float(data[min_pos] + data[max_pos])/2

print(read_file_to_list("data/input00.txt"))
print(list_median_calculator(data))