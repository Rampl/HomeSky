from django.conf.urls import url, include
from django.contrib import admin
from emailform import views

urlpatterns = [
    url(r'^contact', views.contactView, name='contact'),
]