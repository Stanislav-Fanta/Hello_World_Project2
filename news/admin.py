from django.contrib import admin
from .models import News, Review, Article

admin.site.register(News)
admin.site.register(Article)
admin.site.register(Review)