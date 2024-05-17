# Generated by Django 3.2.25 on 2024-05-16 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamManager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='team_manager', serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='BASE_DIR / team-managers')),
            ],
        ),
    ]
