# Generated by Django 4.2.4 on 2024-01-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_jdbook_jdcart_jdcartdetail_jdproduct_jduser_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JdCart',
        ),
        migrations.DeleteModel(
            name='JdCartDetail',
        ),
        migrations.DeleteModel(
            name='JdProduct',
        ),
    ]
