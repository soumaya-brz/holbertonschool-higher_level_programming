#!/usr/bin/python3
"""
Task 02 - Consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
    else:
        print("Failed to fetch posts.")
