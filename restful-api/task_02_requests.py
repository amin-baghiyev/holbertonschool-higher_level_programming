#!/usr/bin/python3
import requests as req
import csv

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    res = req.get(url)
    print(f"Status Code: {res.status_code}")
    if (res.status_code == 200):
        posts = res.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    res = req.get(url)
    if (res.status_code == 200):
        posts = res.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.csv", 'w', newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
