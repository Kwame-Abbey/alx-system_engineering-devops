#!/usr/bin/python3
"""For a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    users_endpoint = f"https://jsonplaceholder.typicode.com/users"
    todos_endpoint = f"https://jsonplaceholder.typicode.com/todos"

    users_payload = {"id": employee_id}
    todos_payload = {"userId": employee_id}

    users_response = requests.get(users_endpoint, params=users_payload).json()

    employee_name = users_response[0].get('name')
    # print(users_response.text)

    todos_response = requests.get(todos_endpoint, params=todos_payload).json()

    len_completed_tasks = 0
    completed_tasks = []
    for todo in todos_response:
        if todo.get('completed') is True:
            len_completed_tasks += 1
            completed_tasks.append(todo.get('title'))

    print(f"Employee {employee_name} is done with tasks"
          f"({len_completed_tasks}/{len(todos_response)}):")
    for title in completed_tasks:
        print(f"\t {title}")
