#!/usr/bin/python3

import requests

r = requests.get("https://jsonplaceholder.typicode.com/")

def fetch_and_print_posts():
    status = r.status_code
    print(status)
    if status == 200:
        data = r.json()
        print(data)

def fetch_and_save_posts():
    print()

fetch_and_print_posts()
