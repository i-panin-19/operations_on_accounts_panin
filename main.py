import data_json_read, data_print_results


"""
- главный файл компиляции кода
- описание программы в файле README.md
- пакеты среды разработки requirements.txt
"""
if __name__ == '__main__':
    data_sort = data_json_read.sort_in_date()
    last_5_data = data_json_read.last_5_executed_data(data_sort)
    # for i in range(len(last_5_data)):
    #     print(last_5_data[i])
    data_print_results.print_result(last_5_data)
