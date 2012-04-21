# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from tweets.utils import TweetSearch


class TweetsUtilsTest(TestCase):
    """Unit test witch verify Twitter API"""

    def setUp(self):
        self.tweets = TweetSearch('flisol')

    def test_capture_tweets(self):
        results = self.tweets.get_tweets()

        assert results

    def test_capture_tweets_page(self):
        page = self.tweets.get_page()

        self.assertEquals(page, 1)

    def test_capture_tweets_page_two(self):
        tweets = TweetSearch('flisol', 2)
        results = tweets.get_tweets()

        assert results


class TweetsViewTest(TestCase):
    """Unit test witch verify tweets views"""
    def test_success_list_tweets(self):
        response = self.client.get(reverse('tweets:list'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'tweets/tweets_list.html')
