from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    # path('login/', views.login),
    # path('register/', views.register),
    path('MainPage/', views.mainpage,name='mainpage'),
    # path('header/',views.header_views,name = 'header'),
    path('login_user/',views.login_user,name='login_user'),
    path('register_user/',views.register_user,name='register_user'),
    path('faq/', views.faq_page, name='faq_page'),
    path('shoppingcar/', views.shopping_car, name='shopping_car'),
    path('product/', views.product_page, name='product_page'),
    path('search/', views.search_books, name='search_books'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('update_num/',views.update_num,name='update_num'),
    path('delete_book/',views.delete_book,name='delete_book'),
    # path('MainPage',views.register)
]