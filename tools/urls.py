from django.urls import path
from tools.views import tool_index, imgToPdf, crawling, ai_view

urlpatterns = [
    path('', tool_index),
    path('imgToPdf/', imgToPdf),
    path('crawling/', crawling),
    path('ai/', ai_view),
]