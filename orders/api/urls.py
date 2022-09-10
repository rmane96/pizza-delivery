from django.contrib import admin
from django.urls import path, include
from .views import OrderListView, OrderDetailView, OrderStatusUpdate, UserOrderDetail, UserOrdersView


urlpatterns = [
    path('',OrderListView.as_view(),name='orders-list'),
    path('<int:order_id>/',OrderDetailView.as_view(),name='order_detail'),
    path('updatestatus/<int:order_id>/',OrderStatusUpdate.as_view(),name='update-order-status'),
    path('user/<int:user_id>/orders/',UserOrdersView.as_view(),name='user-orders'),
    path('user/<int:user_id>/orders/<int:order_id>/',UserOrderDetail.as_view(),name='user-order-details'),
]
