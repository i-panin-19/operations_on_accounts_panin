import json


def sort_in_date():
    data_sort = []
    with open('operations.json', 'r', encoding="utf8") as json_file:
        data = json.load(json_file)
        for p in data:
            if 'date' is not None:
                data_sort.append(str(p.get('date')))
        data_sort.sort()
        # for i in range(len(data_sort)):
        #     print(data_sort[i])

    return data_sort


def last_5_executed_data(data_sort):
    data_sort.reverse()
    last_5_data = []
    k = 0
    with open('operations.json', 'r', encoding="utf8") as json_file:
        data = json.load(json_file)
        for i in range(len(data_sort)):
            for p in data:
                if str(p.get('state')) == 'EXECUTED' and str(p.get('date')) == data_sort[i]:
                    k += 1
                    last_5_data.append(p)
                    pass
            if k == 5:
                break
        # for i in range(len(last_5_data)):
        #     print(last_5_data[i])

    return last_5_data

