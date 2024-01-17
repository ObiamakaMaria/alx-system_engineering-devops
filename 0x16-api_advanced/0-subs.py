#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or type(subreddit) != str:
        return (0)

    reddit_url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    request_headers = {'User-Agent': 'API project'}

    response = requests.get(reddit_url, headers=request_headers)

    if response.status_code != 200:
        return (0)

    subscriber_count = response.json().get("data").get('subscribers', 0)
    return subscriber_count
