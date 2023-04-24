#!/usr/bin/python3
"""Sending reqs using requests package
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    params = {'id': user_id}
    users_url = "https://jsonplaceholder.typicode.com/users"
    name_req = requests.get(users_url, params=params).json()
    name = name_req[0].get("username")
    fname = "{}.json".format(user_id)
    params = {"userId": user_id}
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todo_list = requests.get(todos_url, params=params).json()
    all_todos = {}
    all_todos[user_id] = []
    for item in todo_list:
        obj = {}
        obj["task"] = item.get("title")
        obj["completed"] = item.get("completed")
        obj["username"] = name
        all_todos[user_id].append(obj)

    with open(fname, 'w') as f:
        json.dump(all_todos, f)
