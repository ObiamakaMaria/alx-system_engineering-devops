#!/usr/bin/python3
"""Fetches and displays information about an employee's TODO list
using the JSONPlaceholder API and exports data in json format."""

import json
import requests
import sys


if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        response = requests.get('{}/users/{}'.format(base_url, id)).json()
        res_todo = requests.get("{}/todos".format(base_url),
                                params={"userId": id}).json()
        name = response.get("username")

        with open("{}.json".format(id), "w") as file_json:
            json.dump({id: [{"task": c.get("title"),
                            "completed": c.get("completed"),
                             "username": name} for c in res_todo]},
                      file_json)

    except ValueError:
        pass
