from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index') #url pattern is just views.index
]

