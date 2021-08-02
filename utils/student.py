import json
from utils import student_login_info

se_information_file = 'student_json_data.json'


def account_create_data():
    name = input("enter your name: ")
    age = input("enter your age: ")
    class_name = input('enter class')
    student_address = input('enter your address:')
    student_login_info.login_data(name)

    context = {
        'name': name,
        'age': age,
        'class_name': class_name,
        'address': student_address
    }

    with open(se_information_file, 'r+') as file:
        data = json.load(file)
        data.append(context)
        file.seek(0)
        json.dump(data, file, indent=2)



