# Generated by Django 3.2.4 on 2021-07-13 15:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_auto_20210713_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='datejoined',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='lastlogin',
        ),
        migrations.AddField(
            model_name='registration',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
