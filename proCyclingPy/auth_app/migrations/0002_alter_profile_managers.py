# Generated by Django 3.2.25 on 2024-05-16 09:32

from django.db import migrations
import proCyclingPy.auth_app.managers


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('objects', proCyclingPy.auth_app.managers.AppUserManager()),
            ],
        ),
    ]