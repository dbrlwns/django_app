from django.urls import path
from users.views import login_page, logout_page, signup

urlpatterns = [
    path('', login_page),
    path('logout/', logout_page),
    path('signup/', signup),
]