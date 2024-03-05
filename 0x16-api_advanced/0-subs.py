#!/usr/bin/python3
"""Defines a function that queries the reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the  number of subscribers (not active users,
    total subscribers) for a given subreddit
    """
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Dry-Lingonberry7149'}
    try:
        response = requests.get(subreddit_url, headers=headers,
                                allow_redirects=False).json()

        return response.get('data').get('subscribers')
    except Exception:
        return 0
