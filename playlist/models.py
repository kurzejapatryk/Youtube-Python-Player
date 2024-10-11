# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import lxml, urllib
from urllib.parse import urlparse
from lxml import etree

from django.db import models

class Sound(models.Model):
    url = models.URLField('URL', unique="True")
    yt_id = models.CharField('youtube ID', max_length=50, unique="True")
    title = models.CharField('Tytuł', max_length=150, unique="True")
    count = models.IntegerField('Delay', default='0');
    played = models.IntegerField('Odtworzenie', default='0')
    new = models.IntegerField('Czy nowy', default='1')
    stoped = models.IntegerField("Zablokowany", default="0")

    class Meta:
        verbose_name = "Rekord"
        verbose_name_plural = "Rekordy"
    
    def __unicode__(self):
        return self.url

    def getName(self):
        """"Pobiera i zwraca nazwe filmu"""
        youtube = etree.HTML(urllib.urlopen(self.url).read())
        video_title = youtube.xpath("//span[@id='eow-title']/@title")
        self.title = video_title[0]
        self.save()
        return self.title

    def getId(self):
        """Zwraca ID filmu"""
        url_data = urlparse.urlparse(self.url)
        query = urlparse.parse_qs(url_data.query)
        video = query["v"][0]
        self.yt_id = video
        self.save()
        return video

    def stop(self):
        self.stoped = 1
        self.save()
        return self

    def unstop(self):
        self.stoped = 0
        self.save()
        return self

    def playednow(self, count = 1):
        self.count += count
        self.played += 1
        if(self.new > 0):
            self.new -= 1
        self.save()
        return self


