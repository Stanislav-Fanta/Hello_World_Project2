from . import models
from rest_framework import serializers


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'