# Generated by Django 4.1.6 on 2023-03-13 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Время создания')),
                ('code', models.CharField(max_length=6)),
            ],
        ),
    ]
