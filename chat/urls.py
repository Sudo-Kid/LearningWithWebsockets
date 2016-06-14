from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(chat_group='home'), name='chat'),
    url(r'^(?P<chat_group>[\w]+)/$', views.Index.as_view(), name='group'),
]
