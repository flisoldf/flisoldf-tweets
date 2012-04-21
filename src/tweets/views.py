# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson as json

from tweets.templatetags.twitterize import twitter_text

from tweets.utils import TweetSearch


def list(request):
    return render(request, 'tweets/tweets_list.html')


def list_ajax(request):
    page = request.GET.get('page')
    tweets = TweetSearch(page=int(page))
    results = tweets.get_tweets()

    # Formating tweet text
    tweets = []
    for result in results:
        text = twitter_text(result.get('text'))
        result['text'] = text
        tweets.append(result)

    mimetype = 'application/json'
    return HttpResponse(json.dumps(tweets), mimetype=mimetype)
