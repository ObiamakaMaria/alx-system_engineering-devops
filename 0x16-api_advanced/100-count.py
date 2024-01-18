#!/usr/bin/python3
""" This script fetches top ten posts of a subreddit """
import requests


def count_words(subreddit, word_list, counter={}, after=None):
    """It queries the Reddit API and returns the count of words in
    word_list in the titles """

    sub_data = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_data.status_code != 200:
        return None

    formt_data = sub_data.json()

    hot_l = [child.get("data").get("title")
             for child in formt_data
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if counter == {}:
        counter = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not formt_data.get("data").get("after"):
        sorted_counts = sorted(counter.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(counter.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, counter,
                           info.get("data").get("after"))
