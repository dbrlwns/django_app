from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render

def index(request):
    user = request.user
    if user.is_anonymous:
        user = '로그인 안됨'
    return render(request, 'index.html', {'user': user})