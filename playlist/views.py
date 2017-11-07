# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

import random

from .models import Sound

# Create your views here.

def __getNextUrl(count = 1):

    rand = random.randint(0, 4)
    i = 0

    videos = Sound.objects.filter(stoped = 0).order_by('played').order_by('count')

    news = videos.filter(new = 1)

    for v in videos:
        if(len(news) > 0):
            v = news[0]
            v.playednow(count)
            return v
        if i == rand:
            v.playednow(count)
            return v
        else:
            i += 1

def __getMinCount():
    videos = Sound.objects.order_by('count')[:1]
    return videos[0].count

def play(request):
    url = __getNextUrl()
    if(url.yt_id):
        yt_id = url.yt_id
    else:
        url.getId()
        url.save
        yt_id = url.yt_id
    return render(request, 'playlist/play.html', {'video_id':yt_id})

def addquery(request):
    if(request.POST.get('url')):
        minCount = __getMinCount();
        s = Sound(url=request.POST.get('url'), count = minCount, new = 1)
        s.save()
        s.getId()
        s.getName()
        return redirect(index)
    else:
        return render(request, 'playlist/addform.html', {'error': 1})

def add(request):
    return render(request, 'playlist/addform.html')

def reset(request, sound_id):
    Video =  Sound.objects.get(pk=sound_id)
    Video.new = 1
    Video.save()
    return redirect(index)

def delete(request, sound_id):
    Video = Sound.objects.get(pk=sound_id)
    Video.delete()
    return redirect(index)

def stop(request, sound_id):
    v = Sound.objects.get(pk=sound_id)
    v.stop()
    return redirect(index)

def unstop(request, sound_id):
    v = Sound.objects.get(pk=sound_id)
    v.count = __getMinCount();
    v.save()
    v.unstop()
    return redirect(index)

def getTable(request, params = {'null' : 1}):
    videoList = Sound.objects.order_by('-count')
    params['videos'] = videoList
    return render(request, 'playlist/table.html', params)

def index(request, params = {'null' : 1}):
    videoList = Sound.objects.order_by('-count')
    #for v in videoList:
    #    v.title = v.getName()
    #    v.yt_id = v.getId()
    #    v.save()
    params['videos'] = videoList
    return render(request, 'playlist/playlist.html', params)


