#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "My user agent 1.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {})
        sub = data.get('subscribers', 0)
        return sub
    else:
        return 0
