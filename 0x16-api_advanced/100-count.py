#!/usr/bin/python3
"""Defines a function to count words in all hot posts
of a given Reddit subreddit.
"""

import requests


def count_words(subreddit, word_list, count_dict={}, after=None):
    """Prints counts of given words found in hot post
    """
    params = {"limit": 50}
    if after:
        params["after"] = after
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={
            "User-Agent": "underscoDe@alx-holbertonschool"},
        params=params,
        allow_redirects=False)
    if req.status_code == 200:
        posts = req.json().get("data").get("children")
        for post in posts:
            title = post.get("data").get("title")
            word_list = [word.lower() for word in word_list]
            for word in word_list:
                w_count = title.split().count(word)
                if count_dict.get(word):
                    count_dict[word] += w_count
                else:
                    count_dict[word] = w_count
        if req.json().get("data").get("after"):
            count_words(
                subreddit,
                word_list=word_list,
                count_dict=count_dict,
                after=req.json().get("data").get("after"))
        else:
            for pair in sorted(
                    count_dict.items(),
                    key=lambda kv: (
                        kv[1],
                        kv[0]),
                    reverse=True):
                if pair[1]:
                    print("{}: {}".format(pair[0].strip(), pair[1]))
