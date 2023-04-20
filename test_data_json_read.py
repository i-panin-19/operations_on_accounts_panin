from data_json_read import sort_in_date, last_5_executed_data

"""
- тестирование с pytest
- результат тестирования в файле pytests.txt
"""
def test_sort_in_date():
    assert sort_in_date() != list

def test_last_5_executed_data():
    assert last_5_executed_data([]) == []
