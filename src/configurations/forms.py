# -*- coding: utf8 -*-

from django import forms
from django.utils.translation import ugettext as _

from configurations.models import HashTags


class HashTagForm(forms.ModelForm):
    name = forms.CharField(label=_(u'Nome'))
    hashtag = forms.CharField(label=_(u'Hashtag'),
                             help_text=_(u'Exemplo: #flisoldf'))

    class Meta:
        model = HashTags
