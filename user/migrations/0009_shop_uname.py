# Generated by Django 4.2.4 on 2024-01-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='uname',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
