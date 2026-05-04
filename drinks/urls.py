from django.urls import path
from . import views

app_name = 'drinks'

urlpatterns = [
    path('', views.order_list, name='order_list'),
]