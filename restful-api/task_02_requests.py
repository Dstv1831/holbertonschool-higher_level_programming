#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    status = r.status_code
    if status == 200:
        data = r.json()
        for item in data:
            print(item["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    status = r.status_code
    if status == 200:
        new_data = []
        transferable_keys = ["id", "title", "body"]
        data = r.json()
        for each in data:
            new_dict = {key:value for key, value in each.items() if key in transferable_keys}
            new_data.append(new_dict)
    with open(file="posts.csv", mode="w", encoding="utf-8") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=transferable_keys)
        writer.writeheader()
        writer.writerows(new_data)
