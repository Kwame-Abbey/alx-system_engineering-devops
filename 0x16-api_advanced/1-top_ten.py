#!/usr/bin/python3
"""Defines a function that queries a reddit API
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a
    given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    payload = {'limit': 10}
    headers = {'User-Agent': 'Dry-Lingonberry7149'}

    response = requests.get(url, params=payload, headers=headers,
                            allow_redirects=False).json()

    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
