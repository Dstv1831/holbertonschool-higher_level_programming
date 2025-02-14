#!/usr/bin/python3

"""
This module contain an function that serializes
data from a CSV file to JSON
"""

import csv
import json

def convert_csv_to_json(csv_file):
    try:
        with open(file=csv_file, mode="r", encoding="utf-8") as csvf:
            csvreader = csv.DictReader(csvf)
    except FileNotFoundError:
        return False

    with open(file="data.json", mode='w', encoding="utf-8") as jsonf:
            for rows in csvreader:
                json.dump(rows,jsonf)
    return True