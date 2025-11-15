#!/usr/bin/python3
"""Convert a CSV file to JSON format"""
import csv
import json


def convert_csv_to_json(filename=""):
    """Read a CSV file and overwrite it as JSON"""
    try:
        with open(filename, 'r', encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            data = [r for r in reader]
        with open(filename, 'w', encoding="utf-8") as json_f:
            json.dump(data, json_f)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
