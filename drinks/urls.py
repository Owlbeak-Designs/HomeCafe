from django.urls import path, include
from . import views

app_name = 'drinks'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/', views.OrderCreateView.as_view(), name='order_create'),
    path('claim/<int:pk>/', views.ClaimOrderView.as_view(), name='claim_order'),
    path('update-status/<int:pk>/', views.UpdateOrderStatusView.as_view(), name='update_status'),
]