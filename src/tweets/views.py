# -*- coding: utf8 -*-

from django.shortcuts import render

from tweets.utils import TweetSearch


def list(request):
    tweets = TweetSearch()
    tweets = tweets.get_tweets()
    return render(request, 'tweets/tweets_list.html', {'tweets': tweets})
