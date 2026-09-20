from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.productPage, name='product'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('user/', views.user, name='user'),
    path('orders/', views.orders, name='orders'),
    path('buynow/', views.buynow, name='buynow'),
    path('checkout/', views.checkout, name='checkout'),
    path('mycart/', views.mycart, name='mycart'),
    path('update_cart/', views.update_cart, name='update_cart'),
]
