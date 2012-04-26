# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from configurations.models import HashTags
from configurations.forms import HashTagForm


class HashTagsModelTest(TestCase):
    """Class responsible for performing
    unit tests on the model ``HashTags``
    """

    def test_insert_hashtag(self):
        hashtag = HashTags.objects.create(
            name="Flisol SP",
            hashtag="#flisolsp"
        )

        self.assertEquals(hashtag.id, 1)
        self.assertEquals(HashTags.objects.count(), 1)

    def test_delete_hastag(self):
        hashtag = HashTags.objects.create(
            name="Flisol DF",
            hashtag="#flisoldf"
        )
        hashtag.delete()

        self.assertRaises(HashTags.DoesNotExist, HashTags.objects.get,
                          pk=hashtag.id)


class HashTagsFormTest(TestCase):
    """Class responsible for performing
    unit tests on the model form ``HashTagsForm``
    """

    def test_insert_hashtag(self):
        form = HashTagForm({
            'name': 'Flisol RJ',
            'hashtag': '#flisolrj'
        })

        self.assertTrue(form.is_valid())

    def test_insert_hashtag_with_name_empty(self):
        form = HashTagForm({
            'name': '',
            'hashtag': '#flisolrj'
        })

        self.assertFalse(form.is_valid())

    def test_insert_hashtag_with_hashtag_empty(self):
        form = HashTagForm({
            'name': 'Flisol RJ',
            'hashtag': ''
        })

        self.assertFalse(form.is_valid())


class HashTagsViewTest(TestCase):
    """Class responsible for performing
    unit test for views.
    """

    def test_success_list(self):
        response = self.client.get(reverse('configurations:list'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response,
                                'configurations/configurations_list.html')

    def test_success_new(self):
        response = self.client.get(reverse('configurations:new'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response,
                                'configurations/configurations_form.html')
