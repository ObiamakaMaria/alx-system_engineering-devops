#!/usr/bin/python3
"""This script adds to a list of hot posts"""
import requests


def recurse(subreddit, hot_list=[], after="", counter=0):
    """Recursively retrieve top posts from a subreddit using the Reddit API"""
    req_param = {
        'after': after,
        'count': counter,
        'limit': 100
    }
    req_header = {'User-Agent': 'Alx Task'}
    api_url = 'http://www.reddit.com/r/{}/top/.json'.format(subreddit)

    api_response = requests.get(api_url, params=req_param, headers=req_header)

    if api_response.status_code >= 400:
        return None

    api_data = api_response.json().get('data')
    after = api_data.get('after')
    counter += api_data.get('dist')
    post_data = api_data.get('children')

    for post in post_data:
        post_list.append(post.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, counter)
    else:
        return post_list
