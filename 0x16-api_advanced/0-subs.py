#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers of a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    print(number_of_subscribers("Python"))

