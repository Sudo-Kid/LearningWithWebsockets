from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<chat_room>[\w]+)/$', views.Index.as_view(), name='chat'),
]
