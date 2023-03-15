from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = "__all__"