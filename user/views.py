from django.shortcuts import render


# Create your views here.


# 登录页面
def login(request):
    return render(request, 'auth/login.html')


# 注册页面
def register(request):
    return render(request, 'auth/register.html')
