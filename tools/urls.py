from django.urls import path
from tools.views import tool_index, imgToPdf

urlpatterns = [
    path('', tool_index),
    path('imgToPdf/', imgToPdf),
]