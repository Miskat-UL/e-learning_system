import json
from utils import student_info

file_name = 'student_json_data.json'


def account_create_data():
    name = input("enter your name: ")
    age = input("enter your age: ")
    class_name = input('enter class')
    student_address = input('enter your address:')
    student_info.login_data()

    context = {
        'name': name,
        'age': age,
        'class_name': class_name,
        'address': student_address
    }

    with open(file_name, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)



