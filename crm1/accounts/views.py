from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.

from .models import Customer, Product, Order, Tag
from .forms import OrderForm
from .filters import OrderFilter

def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	
	customer_count  = customers.count()
	order_count  = orders.count()
	delivered_count = orders.filter(status = 'Delivered').count()
	pending_count = orders.filter(status = 'Pending').count()

	context = {
		'customers': customers,
		'orders': orders,
		'customer_count': customer_count,
		'order_count': order_count,
		'delivered_count': delivered_count,
		'pending_count': pending_count,
	}
	return render(
		request,
		'accounts/dashboard.html',
		context,
	)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
	customer = Customer.objects.get(id = pk)
	orders = customer.order_set.all()
	order_count = orders.count()

	my_filter = OrderFilter(request.GET, queryset = orders)
	orders = my_filter.qs

	context = {
		'customer': customer,
		'orders': orders,
		'my_filter': my_filter,
		'order_count': order_count,
	}
	return render(
		request, 
		'accounts/customer.html',
		context,
	)
	
def create_order(request, pk):

	customer = Customer.objects.get(id = pk)
	OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 5)
	
	if request.method == 'POST':
		form_set = OrderFormSet(request.POST, instance = customer)
		if form_set.is_valid():
			form_set.save()
			return redirect('/')
	
	form_set = OrderFormSet(queryset = Order.objects.none(), instance = customer)
	# form = OrderForm(initial = {'customer':customer})
	
	context = {
		'form_set': form_set,
	}
	return render(request, 'accounts/order_form.html', context)

def update_order(request, pk):

	order = Order.objects.get(id = pk)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance = order)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	form = OrderForm(instance = order)
	
	context = {'form': form}
	return render(request, 'accounts/order_form.html', context)
	
def delete_order(request, pk):
	order = Order.objects.get(id = pk)
	
	if request.method == 'POST':
		order.delete()
		return redirect('/')
	
	context = {'order':order}
	return render(request, 'accounts/delete.html', context)
