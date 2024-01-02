import hashlib
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from .models import User
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user.models import JdUser
from django.contrib.auth import logout
from .models import JdBook

def index(request):
    try:
        username = request.session['username']
    except KeyError:
        username = None
    return render(request, "user/index.html", context={
        "username": username
    })


def mainpage(request):
    method = request.method # 请求方法
    username = request.session.get('username', '')
    goods = JdBook.objects.filter(year = 2018);
    context = {'username': username, 'goods': goods}
    # if method == "GET":
    return render(request, "user/MainPage.html",context)
    
# def header_views(request):
#     return render(request, "user/header.html")

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        uname = list(JdUser.objects.values_list('uname', flat=True))
        upwd = list(JdUser.objects.values_list('upwd', flat=True))
        temp = False

        print(username, password)
        print(uname,upwd)
        if username in uname:
            index = uname.index(username)
            if password == upwd[index]:
                user = authenticate(request, username=username, password=password)
                temp = True
                if temp is True:
                    print("true")
                    # login(request, user)
                    request.session['username'] = username  # 将用户名存储在 session 中
                    return JsonResponse({'success': True})
                
        return JsonResponse({'success': False, 'error': 'Invalid credentials'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        uname = list(JdUser.objects.values_list('uname', flat=True))
        upwd = list(JdUser.objects.values_list('upwd', flat=True))

        if username in uname:
            print('username is duplicated')
            return JsonResponse({'success': False, 'error': 'username is duplicated'})
        
        current_count = JdUser.objects.count()
        user = JdUser.objects.create(uid = current_count + 1,uname=username, upwd=password)


        return JsonResponse({'success': True})
    

def faq_page(request):
    # 如果需要，可以在这里添加 F.A.Q 页面的数据获取逻辑
    username = request.session.get('username', '')
    # 将登录信息传递到 faq.html 的上下文中
    context = {'username': username}
    return render(request, 'user/FAQ.html',context)

def shopping_car(request):
    # 如果需要，可以在这里添加 F.A.Q 页面的数据获取逻辑
    username = request.session.get('username', '')
    # 将登录信息传递到 faq.html 的上下文中
    context = {'username': username}
    return render(request, 'user/shoppingcart.html',context)

def product_page(request):
    # 如果需要，可以在这里添加 F.A.Q 页面的数据获取逻辑
    username = request.session.get('username', '')
    # 将登录信息传递到 faq.html 的上下文中
    context = {'username': username}
    return render(request, 'user/productlist.html',context)


        

def search_books(request):
    # username = request.session.get('username', '')
    # context = {'username': username}
    if 'q' in request.GET:
        query = request.GET['q']
        results = JdBook.objects.filter(name__icontains=query)
    else:
        results = None
    return render(request, 'user/search_results.html', {'results': results})
