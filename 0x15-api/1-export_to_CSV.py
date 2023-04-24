#!/usr/bin/python3
"""Sending reqs using requests package
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    params = {'id': user_id}
    users_url = "https://jsonplaceholder.typicode.com/users"
    name_req = requests.get(users_url, params=params).json()
    name = name_req[0].get("username")
    fname = "{}.csv".format(user_id)
    params = {"userId": user_id}
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todo_list = requests.get(todos_url, params=params).json()
    with open(fname, mode='w') as csvfile:
        for item in todo_list:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, name, item.get('completed'), item.get('title')))
