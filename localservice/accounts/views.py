from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Profile

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        Profile.objects.create(
            user=user,
            role=form.cleaned_data['role'],
            phone=form.cleaned_data.get('phone', ''),
            city=form.cleaned_data.get('city', ''),
            skill=form.cleaned_data.get('skill', ''),
        )
        login(request, user)
        messages.success(request, f"Welcome, {user.first_name or user.username}!")
        return redirect('/')
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
