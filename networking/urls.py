from django.urls import path
from . import views

urlpatterns = [
    path('netusers/', views.netuser_list, name='netuser-list'),
    path('create/netusers/', views.create, name='create'),
    path('netusers/<str:pk>/', views.netuser_detail, name='netuser-detail'),
    path('deposits/', views.deposit_list, name='deposit-list'),
    path('deposits/<str:pk>/', views.deposit_detail, name='deposit-detail'),
    path('trades/', views.trade_list, name='trade-list'),
    path('trades/<str:pk>/', views.trade_detail, name='trade-detail'),
    path('orders/', views.order_list, name='order-list'),
    path('create_order/', views.create_order, name='order-create'),
    path('orders/<str:pk>/', views.order_detail, name='order-detail'),
    path('withdrawls/', views.withdrawl_list, name='withdrawl-list'),
    path('completed_orders_list/<str:user_id>/', views.completed_order_list, name='order-detail_list'),
    path('pending_order_list/<str:user_id>/', views.pending_order_list, name='pending-list'),
    path('withdrawls/<str:pk>/', views.withdrawl_detail, name='withdrawl-detail'),
    path('com/<str:user_id>/', views.get_commision, name='commission'),
    path('bal/<str:user_id>/', views.balance, name='balance'),
    path('withdraw/<str:user_id>/', views.create_withdrawl, name='create_withdrawl'),
    path('withdraw_list/<str:user_id>/', views.user_withdrawls, name='user_withdrawls'),
    path('deposit_list/<str:user_id>/', views.user_deposits, name='user_deposits'),
    path('confirm_withdrawl/<int:pk>/', views.confirm_withdrawl, name='confirm_withdrawl'),
    path('deposit_by_user/<str:user_id>/', views.deposit_by_user, name='deposit_by_user'),
    path('links/', views.link_list, name='link-list'),
    path('links/<int:pk>/edit/', views.edit_link, name='edit_link'),
    path('cbal/<str:user_id>/', views.Getbalance, name='Getbalance'),
    path('user_stats/<str:user_id>/', views.UserDetailsView, name='get-detail')

]
# create_withdrawl
# user_withdrawls
# deposit_by_user