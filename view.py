def show_menu():
    print('\n' + '=' * 20)
    print('Выберите необходимое действие: ')
    print('1. Найти сотрудника')
    print('2. Сделать выборку сотрудников по должности')
    print('3. Сделать выборку сотрудников по зарплате')
    print('4. Добавить сотрудника')
    print('5. Удалить сотрудника')
    print('6. Обновить данные сотрудника')
    print('7. Экспортировать данные в формате json')
    print('8. Экспортировать данные в формате csv')
    print('9. Закончить работу')
    print('10. Импортировать сохраненные данные')
    return int(input('Введите номер необходимого действия: '))

def find_person():
    return input('Введите фамилию сотрудника: ')

def print_person(data):
    if data == []:
        print('Сотрудника нет')
    else:
        print(f'{len(data)} сотрудников по данному критерию.')
        for data_person in data:
            id = data_person['id']
            last_name = data_person['last_name']
            first_name = data_person['first_name']
            position = data_person['position']
            phone_number = data_person['phone_number']
            salary = data_person['salary']
            print(f'id: {id}')
            print(f'Фамилия: {last_name}')
            print(f'Имя: {first_name}')
            print(f'Должность: {position}')
            print(f'Телефон: {phone_number}')
            print(f'Зарплата: {salary}')

def filter_of_position():
    return input('Введите наименование должности: ')

def filter_of_salary():
    salary = []
    salary.append(int(input('Введите нижний порог зарплаты: ')))
    salary.append(int(input('Введите верхний порог зарплаты: ')))
    return salary

def add_person(data_base):
    if data_base == []:
        new_id = 1
    else:
        new_id = int(data_base[-1]['id']) + 1
    last_name = input('Введите фамилию сотрудника: ')
    first_name = input('Введите имя сотрудника: ')
    position = input('Введите должность сотрудника: ')
    phone_number = input('Введите телефон сотрудника: ')
    salary = input('Введите зарплату сотрудника: ')
    data_person = {'id': new_id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'phone_number': phone_number, 'salary': salary}
    return data_person

def del_person():
    return int(input('Введите id сотрудника: '))

def change_person():
    x = input('Введите id сотрудника: ')
    print('Начинаем обновление данных сотрудника! Если параметр не изменился ничего не заполняйте.')
    return x

def export_json():
    return input('Введите название файла: ')

def export_csv():
    return input('Введите название файла: ')

def import_csv():
    return input('Введите название файла: ')

def stop():
    print('Работа программы остановлена!')

def error_command():
    print('Несуществующая команда!')
