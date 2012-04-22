# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson as json

from tweets.templatetags.twitterize import twitter_text, to_datetime

from tweets.utils import TweetSearch


def list(request):
    return render(request, 'tweets/tweets_list.html')


def list_ajax(request):
    page = request.GET.get('page')
    tweets = TweetSearch(page=int(page))
    results = tweets.get_tweets()

    # Formating tweet text and datetime
    tweets = []
    for result in results:
        # Formating text for retweet link
        result['retweet'] = result.get('text').replace(' ', '+')

        text = twitter_text(result.get('text'))
        datetime = to_datetime(result.get('created_at'))
        result['text'] = text
        result['created_at'] = datetime.strftime('%d/%m/%Y %R:%M')
        tweets.append(result)

    mimetype = 'application/json'
    return HttpResponse(json.dumps(tweets), mimetype=mimetype)
