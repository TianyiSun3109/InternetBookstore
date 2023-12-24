import hashlib
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    try:
        username = request.session['username']
    except KeyError:
        username = None
    return render(request, "user/index.html", context={
        "username": username
    })


def login(request):
    method = request.method
    if method == "GET":
        return render(request, "user/login.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # try:
        #     user = User.objects.get(username=username)
        #     res = password + settings.SECRET_KEY
        #     password = hashlib.md5(res.encode("utf-8")).hexdigest()
        #     if password == user.password:
        #         html = "<div><h1>恭喜！登录成功！</h1><div><a href='/user/index'>进入首页</a></div></div>"
        #         # 将用户信息存储到session里面
        #         # request.session['username'] = user.username

        #     else:
        #         html = "<div><h1>sorry,密码错误，请重新输入密码</h1><div><a href='/user/login'>重新登录</a></div></div>"


        #     return HttpResponse(html)

        # except user.models.User.DoesNotExist:
        #     html = "<div><h1>sorry,用户名不存在</h1><div><a href='/user/login'>重新登录</a></div></div>"
        #     return HttpResponse(html)
              # 使用Django的authenticate方法验证用户凭据
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 用户凭据有效，登录用户
            login(request, user)
            return JsonResponse({'code': 1000, 'msg': '登录成功'})
        else:
            # 用户凭据无效，返回错误信息
            return JsonResponse({'code': 1001, 'msg': '用户名或密码错误'})


def register(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "user/register.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        # """验证用户名是否存在"""
        # if res:
        #     html = "<div><h1>sorry,用户名已被注册，请尝试新的用户名</h1><div><a href='/user/register'>重新注册</a></div></div>"
        #     return HttpResponse(html)

        # """密码加密"""
        # password = request.POST.get("password")
        # res = password + settings.SECRET_KEY
        # password = hashlib.md5(res.encode("utf-8")).hexdigest()

        # email = request.POST.get("email")

        # """添加数据"""
        # User.objects.create(username=username, password=password)

        # html = "<div><h1>恭喜，注册成功！</h1><div><a href='/user/login'>前往登录</div></div>"
        # return HttpResponse(html)
                # Check if the username already exists
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'code': 1001, 'msg': '用户名已存在'})

        # Create a new user if the username does not exist
        User.objects.create_user(username=username,password=password)
        # 登录用户
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return JsonResponse({'code': 1000, 'msg': '注册成功'})

def shoppingcar(request):
    pass

def mainpage(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "user/MainPage.html")
    
def header_views(request):
    return render(request, "user/header.html")