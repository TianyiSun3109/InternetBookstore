# Internet Bookstore

作者：Tianyi Sun 东南大学吴健雄学院 terrill3109@163.com

## 1.项目简介
本项目是东南大学本项目是23-24-2学期东南大学 数据库原理及应用(研讨) 课程项目，模仿[京东](https://www.jd.com/)的风格设计.

实现了登录/注册、主页、详情页、检索、加入购物车、购物车内修改与计算、历史订单、FAQ等功能.

指导老师为[朱夏](https://cse.seu.edu.cn/2019/0105/c23024a257580/page.htm)老师.

## 2.项目使用方法

本项目是使用`Django`框架实现的后端，需要以下环境：

``` 
Python >= 3
Django
```

本项目使用的是`Django 4.2.4`.

首先执行爬虫.py爬取书籍数据，然后分别在manage.py的同级目录下，终端中输入

```
python manage.py makemigrations
python manage.py migrate
```

进行数据库的迁移，随后执行jd.sql将爬到的数据写入数据库.

之后执行

```
python manage.py runserver
```

即可启动服务.

对应的app名为user，urls见文件urls.py. 

例如 主页的位置为http://127.0.0.1:8000/user/MainPage/
