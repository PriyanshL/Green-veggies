from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.pre_home, name='pre_home'),
    path("home/", views.home, name='home'),
    path("base/", views.base, name='base'),


]