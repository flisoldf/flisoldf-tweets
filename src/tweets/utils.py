# -*- coding: utf8 -*-

import urllib
import simplejson as json

TWEET_SEARCH_URL = "http://search.twitter.com/search.json?q="


class TweetSearch(object):
    def __init__(self, keyword='flisoldf'):
        request = urllib.urlopen(TWEET_SEARCH_URL + keyword)
        results = request.read()

        self.results = json.loads(results)

    def get_tweets(self):
        tweets = []
        for result in self.results.get('results'):
            tweets.append(result)
        return tweets

    def get_page(self):
        return self.results.get('page')
