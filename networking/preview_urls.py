from django.urls import path
from . import views
urls= [
    path('netusers/', views.netuser_list, name='netuser-list'),
    path('netusers/<str:pk>/', views.netuser_detail, name='netuser-detail'),
    path('deposits/', views.deposit_list, name='deposit-list'),
    path('deposits/<str:pk>/', views.deposit_detail, name='deposit-detail'),
    path('trades/', views.trade_list, name='trade-list'),
    path('trades/<str:pk>/', views.trade_detail, name='trade-detail'),
    path('orders/', views.order_list, name='order-list'),
    path('orders/<str:pk>/', views.order_detail, name='order-detail'),
    path('withdrawls/', views.withdrawl_list, name='withdrawl-list'),
    path('withdrawls/<str:pk>/', views.withdrawl_detail, name='withdrawl-detail'),
    path('preview/', views.Preview, name='Preview'),
]