# Generated by Django 4.1.5 on 2023-01-21 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='')),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=128, verbose_name='Категория')),
                ('author', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='')),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=128, verbose_name='Категория')),
                ('author', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='')),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=128, verbose_name='Категория')),
                ('author', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='New',
        ),
    ]
