from django.urls import path
from users.views import login_page

urlpatterns = [
    path('', login_page),
]