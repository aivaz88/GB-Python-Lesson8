import csv
import json
import view
global data_base
data_base = []

def init():
    return data_base

def find_persone(last_name):
    data = []
    for i in data_base:
        if i['last_name'] == last_name:
            data.append(i)
    return data

def filter_of_position(position):
    data = []
    for i in data_base:
        if i['position'] == position:
            data.append(i)
    return data

def filter_of_salary(min, max):
    data = []
    for i in data_base:
        if min <= int(i['salary']) <= max:
            data.append(i)
    return data

def add_person(data):
    data_base.append(data)

def del_person(id):
    for i in range(len(data_base)):
        if int(data_base[i]['id']) != id:
            next
        else:
            count = i
            break
    data_base.pop(count)

def change_person(id):
    data = view.add_person(data_base)
    for i in data_base:
        if i['id'] == id:
            
            if data['last_name'] != '':
                i['last_name'] = data['last_name']
            if data['first_name'] != '':
                i['first_name'] = data['first_name']
            if data['position'] != '':
                i['position'] = data['position']
            if data['phone_number'] != '':
                i['phone_number'] = data['phone_number']
            if data['salary'] != '':
                i['salary'] = data['salary']

def import_csv(file_name):
    file = open(f'{file_name}.csv', 'r', encoding='utf-8')
    data = csv.reader(file, delimiter=',')
    count = 0
    for row in data:
        dict_person = {}
        if count != 0:
            dict_person['id'] = row[0]
            dict_person['last_name'] = row[1]
            dict_person['first_name'] = row[2]
            dict_person['position'] = row[3]
            dict_person['phone_number'] = row[4]
            dict_person['salary'] = row[5]
            data_base.append(dict_person)
        count += 1
    file.close()

def export_json(file_name):
    file = open(f'{file_name}.json', 'w', encoding='utf-8')
    for i in data_base:
        file.write(json.dumps(i) + '\n')
    file.close()

def export_csv(file_name):
    file = open(f'{file_name}.csv', 'w', encoding='utf-8')
    file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
    file_writer.writerow(["id", "last_name", "first_name", "position", "phone_number", "salary"])
    for i in data_base:
        file_writer.writerow(i.values()) 
    file.close()
