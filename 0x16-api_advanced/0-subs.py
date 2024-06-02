#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom-User-Agent'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']

            return subscribers
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
