from data_print_results import print_result, anon_card, anon_check


"""
- тестирование с pytest
- результат тестирования в файле pytests.txt
"""
def test_print_result():
    assert print_result(
        [
            {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
             'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
             'to': 'Счет 46765464282437878125'}
        ]
    ) == None

def test_anon_card():
    assert anon_card(['MasterCard', '1796816785869527']) == 'MasterCard 1796 81** **** 9527'
    assert anon_card(['Счет', '1796816785869527']) == 'Счет 1796 81** **** 9527'

def test_anon_check():
    assert anon_check(['Счет', '38611439522855669794']) == 'Счет **9794'
