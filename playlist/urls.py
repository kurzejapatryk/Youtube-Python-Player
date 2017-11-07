from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^play$', views.play, name='play'),
    url(r'^add$', views.add, name='add'),
    url(r'^addquery$', views.addquery, name="addquery"),
    url(r'^$', views.index, name='index'),
    url(r'^reset/(?P<sound_id>[0-9]+)$', views.reset, name='reset'),
    url(r'^del/(?P<sound_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^stop/(?P<sound_id>[0-9]+)$', views.stop, name='stop'),
    url(r'^unstop/(?P<sound_id>[0-9]+)$', views.unstop, name='unstop'),
    url(r'^table$', views.getTable, name='table'),
]