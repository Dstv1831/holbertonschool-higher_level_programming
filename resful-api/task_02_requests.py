#!/usr/bin/python3

import requests



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
        data = r.json()
        for each in data:
            new_dict = {key:value for key, value in each.items() if key == "id"}
            print (new_dict)



fetch_and_save_posts()
