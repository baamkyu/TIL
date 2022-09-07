from email.mime import audio
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from accounts.forms import CustomUserCreationForm

# Create your views here.
def login(request):
    if request.method == 'POST':    # 로그인 인증 과정
        form = AuthenticationForm(request, request.POST)    # 얘는 어제거랑 다르게 첫번째 인자로 request를 받아줘야 함.
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form, 
    }
    return render(request, 'accounts/signup.html', context)

