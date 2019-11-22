from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home, name='home'),
]
