from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.card_add, name='cart_add'),
    path('remove/<int:product_id>/', views.card_remove,
         name='cart_remove'),
]