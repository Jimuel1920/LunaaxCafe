import json

from . models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    orders = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = orders['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.pro_price * cart[i]['quantity'])

            orders['get_cart_total'] += total
            orders['get_cart_items'] += cart[i]['quantity']

            item = {
                'products': {
                    'id': product.id,
                    'pro_price': product.pro_price,
                    'pro_name': product.pro_name,
                    'pro_image': product.pro_image,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'orders': orders,
            'items':items,
            'cartItems': cartItems}

def cartData(request):
    if request.user.is_authenticated:
        costumer = request.user.customer
        orders, created = order.objects.get_or_create(customer=costumer, complete=False)
        items = orders.orderitem_set.all()
        cartItems = orders.get_cart_items

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        orders = cookieData['orders']
        items = cookieData['items']

    return {'items': items,'orders': orders, 'cartItems': cartItems }

def guestOrder(request, data):
        print('user is not login')
        print('Data', request.body)
        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']

        customer, create = Customer.objects.get_or_creat(
            email=email,

        )
        customer.name = name
        customer.save()

        orders = order.objects.create(
            customer=customer,
            complete=False
        )
        for item in items:
            product = Product.objects.get(id=item['products']['id'])

            orderItems = orderitem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']

            )


        return  customer, orders
