# -*- coding: utf8 -*-

from django.db import models


class HashTags(models.Model):
    name = models.CharField(max_length=40)
    hashtag = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'
        db_table = 'hashtags'

    def __unicode__(self):
        return self.name
