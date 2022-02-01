#!/usr/bin/python3
"""
This script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


def counter(completed=None):
    """Just to count completed task"""

    cont = 0
    for arg in todo:
        if arg.get('completed') is True:
            cont += 1
    return cont

if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'id': argv[1]}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=payload).json()

    payload2 = {'userId': argv[1]}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=payload2).json()

    print('Employee {} is done with tasks({}/{}):'.format(
        user[0].get('name'),
        counter(todo),
        len(todo)))

    for arg in todo:
        if arg.get('completed') is True:
            print("\t {}".format(arg.get('title')))
