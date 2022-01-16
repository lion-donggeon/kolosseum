from django.urls import path
from django.urls.conf import include, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]