from django.urls import re_path

from . import views
urlpatterns = [
    re_path(r'^play$', views.play, name='play'),
    re_path(r'^add$', views.add, name='add'),
    re_path(r'^addquery$', views.addquery, name="addquery"),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^reset/(?P<sound_id>[0-9]+)$', views.reset, name='reset'),
    re_path(r'^del/(?P<sound_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^stop/(?P<sound_id>[0-9]+)$', views.stop, name='stop'),
    re_path(r'^unstop/(?P<sound_id>[0-9]+)$', views.unstop, name='unstop'),
    re_path(r'^table$', views.getTable, name='table'),
]