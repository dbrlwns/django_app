from django.shortcuts import render
from django.urls import path
from pomo.views import pomo, pomo_complete

urlpatterns = [
    path('', pomo),
    path('complete/', pomo_complete),

]