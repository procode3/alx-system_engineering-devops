#!/usr/bin/python3
"""Sending reqs using requests package
"""
import json
import requests

if __name__ == "__main__":
    """getting all users from db
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()
    fname = "todo_all_employees.json"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    all_todo = {}
    for user in users:
        user_name = user.get("username")
        user_id = user.get("id")
        key = int(user_id)
        params = {"userId": user_id}
        todos = requests.get(todos_url, params=params).json()
        all_todo[key] = []
        for item in todos:
            obj = {}
            obj["username"] = user_name
            obj["task"] = item.get("title")
            obj["completed"] = item.get("completed")
            all_todo[key].append(obj)
    with open(fname, 'w') as f:
        json.dump(all_todo, f)
