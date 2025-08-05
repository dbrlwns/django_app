from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from users.forms import LoginForm, SignupForm

from users.models import User

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "GET":
        referer = request.META.get('HTTP_REFERER')
        if referer:
            request.session['next'] = referer
        print(referer)
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_page = request.session.pop('next')
                return redirect(next_page)
            else:
                form.add_error("password", "Wrong password")
                return render(request, 'users/login.html', {'form': form})




def logout_page(request):
    logout(request)
    # 이전 페이지를 유지
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)


def signup(request):
    if request.method == "GET":
        referer = request.META.get('HTTP_REFERER')
        if referer:
            request.session['next'] = referer
        print(referer)

        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            profile_image = form.cleaned_data["profile_image"]

            if password1 != password2:
                form.add_error("password1", "Passwords don't match")

            if User.objects.filter(username=username).exists():
                form.add_error("username", "Username already exists")

            if form.errors:
                return render(request, 'users/signup.html', {'form': form})
            else:
                user = User.objects.create_user(username=username, password=password1, profile_image=profile_image)
                login(request, user)

                next_page = request.session.pop('next', '/')
                return redirect(next_page)


