# Generated by Django 4.0 on 2023-05-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedMain', '0002_autorization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Height', models.CharField(max_length=5, verbose_name='Рост')),
                ('Weight', models.CharField(max_length=3, verbose_name='Вес')),
                ('Diseases', models.TextField(max_length=200, verbose_name='Заболевания')),
            ],
        ),
    ]