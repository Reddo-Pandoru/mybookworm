from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('admin/loan/', views.loan_modifier, name='loan_modifier'),
]
