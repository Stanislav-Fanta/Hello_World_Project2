from django.db import models
from django.contrib.auth.models import User


class Template(models.Model):
    name = models.CharField('Заголовок', max_length=128)
    description = models.CharField('Описание', max_length=256)
    image = models.ImageField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, max_length=128, on_delete=models.CASCADE)
    category = models.CharField('Категория', max_length=128)

    class Meta:
        abstract = True


class Article(Template):
    pass


class Review(Template):
    pass


class News(Template):
    pass
