# Generated by Django 4.0 on 2023-05-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedMain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Auto', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('Password_Auto', models.CharField(max_length=100, verbose_name='Пароль для авторизации')),
                ('Password_confirmation_Auto', models.CharField(max_length=100, verbose_name='Подтверждение пароля')),
            ],
        ),
    ]