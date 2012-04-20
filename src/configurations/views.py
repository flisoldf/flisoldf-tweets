# -*- coding: utf8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse


def list(request):
    return render(request, 'configurations/configurations_list.html')
