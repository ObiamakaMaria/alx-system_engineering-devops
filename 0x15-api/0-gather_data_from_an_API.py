#!/usr/bin/python3
"""Fetches and displays information about an employee's TODO list
using the JSONPlaceholder API """

import requests
import sys


if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        response = requests.get('{}/users/{}'.format(base_url, id)).json()
        res_todo = requests.get("{}/todos".format(base_url),
                                params={"userId": id}).json()
        task_completed = [c.get('title') for c in res_todo
                     if c.get("completed") is True]
        e = "Employee {} is done with tasks({}/{}):".format(
            response.get('name'), len(task_completed), len(res_todo))
        print(e)
        for c in task_completed:
            print("\t {}".format(c))
    except ValueError:
        pass
