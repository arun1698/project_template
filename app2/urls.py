from django.contrib import admin
from django.urls import path
from app2 import views
import os
app_name="app2"
urlpatterns=[
    path('index',views.index,name="index"),
    path('sample2/',views.sample,name="sample2"),
    path('sample/',views.sample_app2,name="sample_app2"),
]