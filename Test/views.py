from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'Test/register.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        res_data = {}
        if not (username and email and password and confirm_password):
            res_data['error'] = '모든 값을 입력해주세요.'
        if password != confirm_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            user = User(username=username, email=email, password=make_password(password))
            user.save()
        return render(request, 'Test/register.html', res_data)
    
    
def login(request):
    return render(request, 'Test/login.html')
