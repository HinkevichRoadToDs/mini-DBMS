from csv_module import fieldnames
def get_mode():
    mode = int(input('Введите действие, которое вы хотите совершить:\n'
                     '0 - завершить работу\n'
                     '1 - найти запись в БД\n'
                     '2 - посмотреть структуру БД\n'
                     '3 - добавить запись в БД\n'
                     '4 - удалить запись из БД\n'
                     '5 - изменить существующую запись : '))
    return mode
def get_parameter():
    param_dict = {}
    print('по каким атрибутам вы будете фильтровать?\n'
          '1 - id\n'
          '2 - name\n'
          '3 - surname\n'
          '4 - email\n'
          '5 - salary : ')
    for i in range(4):
        param = input('Введите номер атрибута или точку, чтобы закончить: ')
        if param != '.':
            param_dict[fieldnames[int(param)-1]] = input('Введите значение для поиска: ')
        else:
            break
    return param_dict

def display_filtered_data(data):
    print('Результат поиска:\n', data)

def get_newdata():
    dict_new = {}
    for item in fieldnames[1:]:
        dict_new[item] = input(f'Введите {item}: ')
    return dict_new


def get_row_number():
    row_number = input("Введите id записи, которую нужно изменить: ")
    return int(row_number)
def get_changes():
    changes_dict = {}
    print('Какие атрибуты вы будете менять?\n'
          '1 - name\n'
          '2 - surname\n'
          '3 - email\n'
          '4 - salary : ')
    for i in range(4):
        choise = input('Введите номер атрибута или точку, чтобы закончить: ')
        if choise != '.':
            changes_dict[fieldnames[int(choise)]] = input('Введите новое значение: ')
        else:
            break
    return changes_dict


def get_del_id():
    row_number = input("Введите id записи, которую нужно удалить: ")
    return int(row_number)