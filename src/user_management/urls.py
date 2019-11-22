from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
