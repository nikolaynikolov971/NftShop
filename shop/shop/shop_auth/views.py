from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

# Create your views here.
from shop.shop_auth.forms import LoginForm, RegisterForm


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'log-in.html', context)


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_user')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'create_user.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing_page')