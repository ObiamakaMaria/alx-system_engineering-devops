#!/usr/bin/python3
"""Fetches and displays information about an employee's TODO list
using the JSONPlaceholder API and exports data in CSV format."""

import requests
import csv
import sys


if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"
        response = requests.get('{}/users/{}'.format(base_url, id)).json()
        res_todo = requests.get("{}/todos".format(base_url),
                                params={"userId": id}).json()
        name = response.get("username")

        with open("{}.csv".format(id), "w") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            [csv_writer.writerow([id, name, c.get("completed"),
                                 c.get("title")]) for c in res_todo]

    except ValueError:
        pass
