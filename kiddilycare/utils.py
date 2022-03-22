import json
from . models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print("Cart user : ", cart)

    items = []
    total = 0
    cartItems = 0

    order = {
        "get_cart_items": cartItems,
        "get_cart_total": total,
        "shipping": False
    }
    cartItems = order["get_cart_items"]

    for i in cart:
        try:
            cartItems+= cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total += product.price * cart[i]["quantity"]

            item = {
                "product": {
                    'id': product.id,
                    'product_name': product.product_name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                    'digital': product.digital
                },
                'quantity': cart[i]["quantity"],
                'get_item_total': product.price * cart[i]["quantity"]
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
        order['get_cart_items'] = cartItems
        order['get_cart_total'] = total

    return { 
        'cartItems': cartItems,
        'order': order,
        'items': items
    }

def cartData(request):
    if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, status="PENDING")
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return { 
        'cartItems': cartItems,
        'order': order,
        'items': items
    }

def guestUser(request, form):
    print("Guest user...")

    print("Cookies : ", request.COOKIES)
    name = form['name']
    email = form['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        customer_email = email,
    )
    customer.customer_name = name
    print("Customer name : ", customer)
    customer.save()

    order = Order.objects.create(
        customer=customer,
        status="PENDING"
    )

    for item in items:
        product= Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
