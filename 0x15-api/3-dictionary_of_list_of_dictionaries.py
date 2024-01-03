#!/usr/bin/python3
"""Fetches and displays information about an employee's TODO list
using the JSONPlaceholder API and exports data in json format."""

import json
import requests
import sys


if __name__ == "__main__":
    data = {}
    for x in range(1, 11):
        id = x
        base_url = "https://jsonplaceholder.typicode.com"
        res = requests.get('{}/users/{}'.format(base_url, id)).json()
        res_todo = requests.get("{}/todos".format(base_url),
                                params={"userId": id}).json()
        name = res.get("username")
        user_data = list(map(
                    lambda c: {
                        "task": c.get("title"),
                        "completed": c.get("completed"),
                        "username": name
                    },
                    res_todo
                ))
        data["{}".format(id)] = user_data
    with open('todo_all_employees.json', 'w') as apidata:
        json.dump(data, apidata)
