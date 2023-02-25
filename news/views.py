from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class NewView(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer



