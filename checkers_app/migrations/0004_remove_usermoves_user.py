# Generated by Django 3.0.8 on 2020-07-30 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkers_app', '0003_usermoves_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermoves',
            name='user',
        ),
    ]