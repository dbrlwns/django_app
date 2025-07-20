from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from users.forms import LoginForm

from users.models import User

from django.contrib.auth import authenticate, login
# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("password", "Wrong password")

    else:
        form = LoginForm()

    #print(request.user.is_authenticated)

    return render(request, 'users/login.html', {'form': form})