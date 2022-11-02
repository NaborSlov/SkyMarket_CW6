# Generated by Django 3.2.6 on 2022-11-02 12:42

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.MinLengthValidator(1)])),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Админ')], default='user', max_length=6, verbose_name='Роль')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
