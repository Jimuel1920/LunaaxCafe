import datetime
import json    ,sys
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .utils import cookieCart, cartData , guestOrder


# Create your views here.


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'front/store.html', context)

@csrf_exempt
def cart(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    orders = data['orders']
    items = data['items']

    context ={
        'orders': orders,
        'items':items,
        'cartItems': cartItems}

    return render(request, 'front/cart.html', context)

@csrf_exempt
def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    orders = data['orders']
    items = data['items']

    context = {'items': items,'orders': orders, 'cartItems': cartItems }
    return render(request, 'front/checkout.html', context)


@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    orders, created = order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = orderitem.objects.get_or_create(orders=orders, products=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        orders, created = order.objects.get_or_create(customer=customer, complete = False)
        
       
    else:
        customer, orders = guestOrder(request, data)
    
    total = float(data['form']['total'])
    orders.transation_id = transaction_id

    if total == float(orders.get_cart_total):
        orders.complete = True
    orders.save()

    if orders.shipping == True:
        Shippingaddress.objects.create(
            customer=customer,
            order=orders,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment Complete', safe=False)
