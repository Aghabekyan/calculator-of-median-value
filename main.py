from helpers import read_file_to_list, list_median_calculator

def main():
    data = read_file_to_list("data/input01.txt")
    count = data.pop(0)
    tmp_list = []
    for i in range(0, count):
        tmp_list.append(data[i])
        print(list_median_calculator(sorted(tmp_list)))

if __name__ == "__main__":
    main()