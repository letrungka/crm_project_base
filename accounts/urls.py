from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products,name='product'),
    path('customer/', views.customer_view, name='customer'),
    path('customer/<str:pk>/', views.customer_profile, name='customer_profile')
]
