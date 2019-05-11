from helpers import read_file_to_list, list_median_calculator

tested_files_dict = {
    "data/input00.txt": "data/output00.txt",
    "data/input01.txt": "data/output01.txt",
    "data/input02.txt": "data/output02.txt",
    "data/input03.txt": "data/output03.txt"
}

for key in tested_files_dict:

    input_data = read_file_to_list(key)
    output_data = read_file_to_list(tested_files_dict[key], 'float')
    count = input_data.pop(0)
    tmp_list = []
    for i in range(0, count):
        tmp_list.append(input_data[i])
        result = list_median_calculator(sorted(tmp_list))
        assert result == output_data[i], "Inconsistency in line {0} of output file {1}." .format(i, tested_files_dict[key])