from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_orders = orders.count()
    total_delivered_orders = orders.filter(status='Delivered').count()
    total_pending_orders = orders.filter(status='Pending').count()
    

    context = {'total_orders':total_orders,'total_delivered_orders': total_delivered_orders,'total_pending_orders':total_pending_orders, \
                'customers': customers, 'orders': orders}
    return render(request, 'accounts/dashboard.html',context=context)



def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})



def customer_view(request):
    return render(request, 'accounts/customer.html')


def customer_profile(request, pk):
    customer = Customer.objects.get(id=pk)

    order = Order.objects.filter(customer=customer)
    total_orders = order.count()

    context = {'customer': customer,'total_orders':total_orders,'order':order }
    return render(request, 'accounts/customer.html', context)
