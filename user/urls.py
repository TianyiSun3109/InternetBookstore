from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('MainPage/', views.mainpage),
    path('header/',views.header_views,name = 'header'),
    path('login_user/',views.login_user,name='login_user'),
    # path('MainPage',views.register)
]