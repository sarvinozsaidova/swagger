from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', GetMethod, basename='product')
router.register('category', CategoryOption, basename='category')
router.register('customer', CustomerOption, basename='customer')
urlpatterns =[
    path('customers/<int:customer_id>/product', CustomerPurchasingListAPIView.as_view()),
] + router.urls
