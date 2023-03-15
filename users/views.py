from rest_framework import viewsets
from . import models
from . import serializers
from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class MyUserView(viewsets.ModelViewSet):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.MyUserSerializer