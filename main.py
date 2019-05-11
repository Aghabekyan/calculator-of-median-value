import math

data = []

def list_median_calculator(data):
    length = len(data)
    if length % 2 != 0:
        pos = int(math.floor(length/2))
        return float(data[pos])
    else:
        max_pos = length/2
        min_pos = max_pos - 1
        return float(data[min_pos] + data[max_pos])/2

print(list_median_calculator(data))