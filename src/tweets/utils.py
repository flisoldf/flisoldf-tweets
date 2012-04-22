# -*- coding: utf8 -*-

import urllib
import simplejson as json

TWEET_SEARCH_URL = "http://search.twitter.com/search.json?q=%s&page=%d"


class TweetSearch(object):
    def __init__(self, keyword='#flisol', page=1):
        request = urllib.urlopen(TWEET_SEARCH_URL % (keyword, page))
        results = request.read()

        self.results = json.loads(results)

    def get_tweets(self):
        tweets = []
        for result in self.results.get('results'):
            tweets.append(result)
        return tweets

    def get_page(self):
        return self.results.get('page')
