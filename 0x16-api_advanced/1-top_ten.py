#!/usr/bin/python3
"""
  This script gets the top ten subreddit API.
"""
import requests

def top_ten(subreddit):
    """
    List the top 10 posts from a subreddit using the Reddit API.
    """

    if subreddit is None or type(subreddit) != str:
        print('None')
        return
    
    req_param = {'limit': 10}
    req_header = {'User-Agent': 'Reddit API'}
    
    api_url = "http://www.reddit.com/r/{}/top/.json".format(subreddit)
    api_response = requests.get(api_url, params=req_param, headers=req_header)

    if api_response.status_code != 200:
        print('None')
        return

    response_data = api_response.json().get('data').get('children')
    for post in response_data:
        print(post.get('data').get('title'))
