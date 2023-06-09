from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'new', views.NewView)
router.register(r'article', views.ArticleView)
router.register(r'Review', views.ReviewView)

urlpatterns = [
    path('', include(router.urls)),

]
