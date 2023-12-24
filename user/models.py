from django.db import models



class JdBook(models.Model):
    year = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    pinglun = models.CharField(max_length=63, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    chuban = models.CharField(max_length=255, blank=True, null=True)
    jiage = models.CharField(max_length=63, blank=True, null=True)
    yuanjia = models.CharField(max_length=63, blank=True, null=True)
    discount = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jd_book'


class JdCart(models.Model):
    cid = models.AutoField(primary_key=True)
    userid = models.IntegerField(db_column='userID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'jd_cart'


class JdCartDetail(models.Model):
    did = models.AutoField(primary_key=True)
    cartid = models.IntegerField(db_column='cartID', blank=True, null=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='productID', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jd_cart_detail'


class JdProduct(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=64, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    pic = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jd_product'


class JdUser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=32, blank=True, null=True)
    upwd = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jd_user'


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=32, unique=False)
    class Meta:
        db_table = "user"

class Shop(models.Model):
    bookname = models.CharField(max_length=100,unique=False)
    price = models.FloatField()
    num = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "shopping_car"