from django.contrib import admin
from django.urls import path
from app1 import views
import os
app_name="app1"
urlpatterns=[
    path('index/',views.index,name="index"),
    path('sample1/',views.sample,name="sample1"),
    path('sample/',views.sample_app1,name="sample_app1"),
]
