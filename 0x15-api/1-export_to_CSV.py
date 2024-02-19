#!/usr/bin/python3
"""Export to csv"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    users_endpoint = f"https://jsonplaceholder.typicode.com/users"
    todos_endpoint = f"https://jsonplaceholder.typicode.com/todos"

    users_payload = {"id": user_id}
    todos_payload = {"userId": user_id}

    users_response = requests.get(users_endpoint, params=users_payload).json()

    user_name = users_response[0].get('username')
    # print(users_response.text)

    todos_response = requests.get(todos_endpoint, params=todos_payload).json()

    with open(f"{user_id}.csv", mode="w") as user_file:
        user = csv.writer(user_file, quoting=csv.QUOTE_ALL)

        for todo in todos_response:
            user.writerow([user_id, user_name, todo.get('completed'),
                           todo.get('title')])
