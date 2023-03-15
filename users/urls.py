from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'new', views.UserView)
router.register(r'new', views.MyUserView)

urlpatterns = [
    path('', include(router.urls)),

]