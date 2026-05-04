from django.shortcuts import render
from .models import Order

# Create your views here.
def order_list(request):
    # Show all orders, newest first – adjust queryset as needed
    orders = Order.objects.all().order_by('-ordered_at')
    context = {'orders': orders}
    return render(request, 'drinks/order_list.html', context)