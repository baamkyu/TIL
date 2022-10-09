from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login     # login->auth_login 이름 변경
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.


# 회원가입 로직
def signup(request):
    # POST방식으로 받고
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # 유효성 검증 통과하면 user데이터를 저장하고 index.html로 이동
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    # GET방식으로 받으면 signup.html로 이동해서 회원가입 form을 띄움
    else:
        form = CustomUserCreationForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    # POST방식으로 받고
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 유효성 검증 통과하면 index.html로 이동
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    # GET방식으로 받으면 login.html로 이동해서 로그인 form을 띄움
    else:
        form = AuthenticationForm
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)