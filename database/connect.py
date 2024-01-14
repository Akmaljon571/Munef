import json
import os


def path():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, 'workshops.json')


def get_all():
    with open(path(), 'r') as file:
        return json.load(file)


def get_one(id: int):
    with open(path(), 'r') as file:
        all = json.load(file)
        for a in all:
            if a['id'] == id:
                return a


def create(data):
    all_data = get_all()
    all_data.append(data)
    with open(path(), 'w') as file:
        json.dump(all_data, file, indent=2)


def create_vacancy(id, data):
    one_data = get_one(id)
    if one_data:
        one_data['vacancy'].append(data)
        all_data = get_all()
        new_data = list(map(lambda x: one_data if x['id'] == id else x, all_data))
        with open(path(), 'w') as file:
            json.dump(new_data, file, indent=2)


def delete(id):
    all_data = get_all()
    new_data = list(filter(lambda x: x['id'] != id, all_data))
    with open(path(), 'w') as file:
        json.dump(new_data, file, indent=2)


def delete_vacancy(id, text):
    one_data = get_one(id)
    if one_data:
        one_data['vacancy'] = list(filter(lambda x: x != text, one_data['vacancy']))
        all_data = get_all()
        new_data = list(map(lambda x: one_data if x['id'] == id else x, all_data))
        with open(path(), 'w') as file:
            json.dump(new_data, file, indent=2)
