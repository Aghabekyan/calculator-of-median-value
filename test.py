from helpers import read_file_to_list, list_median_calculator

tested_files_dict = {
    "data/input00.txt": "data/output00.txt",
    "data/input01.txt": "data/output01.txt"
}

for key in tested_files_dict:
    print(key)
    print(tested_files_dict[key])

    input_data = read_file_to_list(key)
    output_data = read_file_to_list(tested_files_dict[key], 'float')
    count = input_data.pop(0)
    tmp_list = []
    for i in range(0, count):
        tmp_list.append(input_data[i])
        result = list_median_calculator(sorted(tmp_list))
        print(result, output_data[i])
        assert result == output_data[i], "Error"