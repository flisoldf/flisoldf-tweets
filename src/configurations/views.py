# -*- coding: utf8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse


from configurations.models import HashTags
from configurations.forms import HashTagForm


def list(request):
    hashtags = HashTags.objects.all()
    return render(request, 'configurations/configurations_list.html',
                  {'hashtags': hashtags})


def new(request):
    form = HashTagForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('configurations:list'), permanent=True)

    return render(request, 'configurations/configurations_form.html',
                  {'form': form})


def edit(request, hashtag):
    hashtag = get_object_or_404(HashTags, pk=hashtag)

    form = HashTagForm(request.POST or None, instance=hashtag)

    if form.is_valid():
        form.save()
        return redirect(reverse('configurations:list'), permanent=True)

    return render(request, 'configurations/configurations_form.html',
                  {'form': form})


def delete(request, hashtag):
    hashtag = get_object_or_404(HashTags, pk=hashtag)
    hashtag.delete()

    return redirect(reverse('configurations:list'), permanent=True)
