# -*- coding: utf8 -*-

from django.test import TestCase

from configurations.models import HashTags


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
