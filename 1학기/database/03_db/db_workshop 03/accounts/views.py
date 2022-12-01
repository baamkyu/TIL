from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login     # login->auth_login 이름 변경
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #로그인
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)