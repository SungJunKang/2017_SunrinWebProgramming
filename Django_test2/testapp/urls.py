from django.urls import path
from . import views

urlpatterns = [
    path(r'index', views.index),
    path(r'second',views.second),
    path(r'third',views.third),
]
