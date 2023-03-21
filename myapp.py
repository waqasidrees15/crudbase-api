import requests
import json

URL = 'http://127.0.0.1:8000/employeeapi/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(int(input("Enter your Employee ID:  ")))


def post_data():
    data = {
        'name': input("Enter Your name:  ").title(),
        'department': input("Enter Your Department:  ").title(),
        'post': input("Enter Your Post:  ").title(),
        'cnic': int(input("Enter Your CNIC:  ")),
        'contact': int(input("Enter your Contact Number:  ")),
        'city': input("Enter Your City Name:  ").title()
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id': int(input("Enter a valid ID to Update Data:  ")),
        # 'name': input("Enter Your name:  ").title(),
        # 'department': input("Enter Your Department:  ").title(),
        # 'post': input("Enter Your Post:  ").title(),
        'cnic': int(input("Enter Your CNIC:  ")),
        # 'contact': int(input("Enter your Contact Number:  ")),
        # 'city': input("Enter Your City Name:  ").title()
    }
    json_data = json.dumps(data)
    r = requests.patch(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()

def delete_data():
    data = {'id': int(input("Enter a Valid ID to Delete Data:  "))}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()
