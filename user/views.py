from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from user.models import User

def signin(request):
    # 값을 읽고 싶을 때 GET - URL Parameter(http://ooo.com?title=안녕하세요)
    # 값을 지우고 싶을 때 DELETE - URL Parameter

    # 값을 수정 PUT
    # 값을 생성 POST
    if request.method == "GET":
        return render(request, "page/signin.html")
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('board')
        
        else:
            messages.error(request, '입력값을 확인해 주세요.')
            return redirect('signin')
        
        return render(request, "page/signin.html")

def signup(request):
    if request.method == "GET":
        return render(request, "page/signup.html")
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        chk_password = request.POST['chk_password']
        nickname = request.POST['nickname']

        user = User.objects.filter(username=username)
        # 존재 시 True, 아니면 False
        if user.exists():
            messages.error(request, '이미가입된 아이디입니다.')
            return redirect('signup')

        else:
            new_user = User(
                username = username,
                password = make_password(password),
                nickname = nickname,
            )

            new_user.save()
            login(request, new_user)

            return redirect('board')
            

def signout(request):
    # request method가 GET일 경우 로그아웃 수행.
    if request.method == 'GET':
        logout(request)
        return redirect('board')