from django.db import models




class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32, unique=False)
    email = models.EmailField()

    class Meta:
        db_table = "user"

class Shop(models.Model):
    bookname = models.CharField(max_length=100,unique=False)
    price = models.FloatField()
    num = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "shopping_car"