#!/usr/bin/python3
"""Export to JSON"""

import json
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

    todos = []

    for todo in todos_response:
        n_dict = {}
        n_dict["task"] = todo.get('title')
        n_dict["completed"] = todo.get('completed')
        n_dict["username"] = user_name
        todos.append(n_dict)

    n_format = {f"{user_id}": todos}

    with open(f"{user_id}.json", mode="w") as json_file:
        json.dump(n_format, json_file)
