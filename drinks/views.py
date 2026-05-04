from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from .models import Order
from .forms import OrderForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def order_list(request):
    # Show all orders, newest first – adjust queryset as needed
    orders = Order.objects.all().order_by('-ordered_at')
    context = {'orders': orders}
    return render(request, 'drinks/order_list.html', context)

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'drinks/order_form.html'
    success_url = reverse_lazy('drinks:order_list')

    def form_valid(self, form):
        form.instance.ordered_by = self.request.user   # now user is authenticated
        return super().form_valid(form)

class ClaimOrderView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        # Only allow claiming if not already claimed
        if order.claimed_by is None:
            order.claimed_by = request.user
            order.save()
        return redirect('drinks:order_list')

class UpdateOrderStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        # Only the barista who claimed it can update status
        if order.claimed_by == request.user:
            new_status = request.POST.get('status')
            if new_status in ['pending', 'making', 'ready']:
                order.status = new_status
                order.save()
        return redirect('drinks:order_list')