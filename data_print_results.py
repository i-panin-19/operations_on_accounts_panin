def print_result(last_5_data):
    for data in last_5_data:
        date = (str(data.get('date')))[0:10].split('-')
        date.reverse()
        print('.'.join(date), data.get('description'))

        if 'from' in data:
            from_ = data.get('from').split(' ')
            if not ('Счет' in from_):
                num_from = anon_card(from_)
            else:
                num_from = anon_check(from_)
        else:
            num_from = '-'

        to_ = data.get('to').split(' ')
        if not ('Счет' in to_):
            num_to = anon_card(to_)
        else:
            num_to = anon_check(to_)
        print(f'{num_from} -> {num_to}')

        operation_amount = data.get('operationAmount')
        print(operation_amount.get('amount'), operation_amount.get('currency').get('name'), '\n')


def anon_card(count):
    new_num = ''
    num = count[len(count) - 1][::-1]
    num = num[0:4] + '******' + num[10:]
    num = num[::-1]
    for i in range(len(num)):
        if (i + 1) % 4 == 0:
            new_num += num[i] + ' '
        else:
            new_num += num[i]
    num = ''
    for i in range(len(count)-1):
        num += count[i] + ' '

    return num + new_num[:-1]

def anon_check(count):
    num = count[len(count) - 1][::-1]
    num = num[0:4] + '**'
    new_num = num[::-1]
    num = ''
    for i in range(len(count)-1):
        num += count[i] + ' '

    return num + new_num
