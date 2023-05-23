from django.db import models
from django import forms


class Regiser(models.Model):
    FIO = models.CharField('ФИО', max_length=100)
    User_name = models.CharField('Ник', max_length=100)
    Email = models.EmailField('Почта', max_length=100)
    Phone_number = models.CharField('Телефон', max_length=100)
    Password = models.CharField('Пароль', max_length=100)
    Password_confirmation = models.CharField('Подтверждение', max_length=100)
    Gender = models.BooleanField('Женский пол', default=True)
    Gender_1 = models.BooleanField('Мужской пол', default=True)

    def __str__(self):
        return self.FIO


class Autorization(models.Model):
    Name_Auto = models.CharField('Имя пользователя', max_length=100)
    Password_Auto = models.CharField('Пароль для авторизации', max_length=100)
    Password_confirmation_Auto = models.CharField('Подтверждение пароля', max_length=100)

    def __str__(self):
        return self.Name_Auto


class Info(models.Model):
    Height = models.CharField('Рост', max_length=5)
    Weight = models.CharField('Вес', max_length=3)
    Diseases = models.TextField('Заболевания', max_length=200)

    def __str__(self):
        return self.Height
