from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'magicball'
urlpatterns = [
    path('', views.index, name='index'),
]