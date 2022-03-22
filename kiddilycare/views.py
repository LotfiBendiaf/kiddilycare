from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse
import datetime
from .models import *
import json

from . utils import cookieCart, cartData, guestUser

# Create your views here.
elements = list()

# Interface accueil
def store(request):
    data = cartData(request)

    cartItems = data['cartItems']

    bestseller = Product.objects.all()[0:4]
    bodyProducts = Product.objects.filter(category ="corps")
    faceProducts = Product.objects.filter(category ="Visage")
    jadeProducts = Product.objects.filter(category ="Jade")
    accessories = Product.objects.filter(category ="Accessoires")
    context = {
        "bestseller": bestseller,
        "faceProducts": faceProducts,
        "bodyProducts": bodyProducts,
        "jadeProducts": jadeProducts,
        "accessories": accessories,
        "cartItems": cartItems,

    }
    return render(request, 'store.html', context)

def collections(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {
        "cartItems": cartItems,
    }
    return render(request, 'Collections/collections.html', context)

def products(request):
    data = cartData(request)

    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {
        "products": products,
        "cartItems": cartItems,

    }
    return render(request, 'Collections/products.html', context)

def visage(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsVisage = Product.objects.filter(category ="Visage")
    context = {
        "produitsVisage": produitsVisage,
        "cartItems": cartItems,

    }
    return render(request, 'Collections/produitsVisage.html', context)

def corps(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsCorps = Product.objects.filter(category ="Corps")
    context = {
        "produitsCorps": produitsCorps,
        "cartItems": cartItems,

    }
    return render(request, 'Collections/produitsCorps.html', context)

def jade(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsJade = Product.objects.filter(category ="Jade")
    context = {
        "produitsJade": produitsJade,
        "cartItems": cartItems,

    }
    return render(request, 'Collections/produitsJade.html', context)
def ete(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsEte = Product.objects.filter(category ="Ete")
    context = {
        "produitsEte": produitsEte,
        "cartItems": cartItems,

    }
    return render(request, 'News/modeEte.html', context)

def tendances(request):
    data = cartData(request)

    cartItems = data['cartItems']

    this_month = datetime.datetime.now().month
    produitsTendances = Product.objects.filter(date_created__month = this_month)

    context = {
        "produitsTendances": produitsTendances,
        "cartItems": cartItems,

    }
    return render(request, 'News/tendances.html', context)

def accessoires(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsAccessoires = Product.objects.filter(category ="Accessoires")
    context = {
        "produitsAccessoires": produitsAccessoires,
        "cartItems": cartItems,

    }
    return render(request, 'Collections/accessoires.html', context)

def beaute(request):
    data = cartData(request)

    cartItems = data['cartItems']


    produitsBeaute = Product.objects.filter(category ="Beauté")
    context = {
        "produitsBeaute": produitsBeaute,
        "cartItems": cartItems,

    }
    return render(request, 'Promotions/beaute.html', context)

def sante(request):
    data = cartData(request)

    cartItems = data['cartItems']

    produitsSante = Product.objects.filter(category ="Santé")
    context = {
        "produitsSante": produitsSante,
        "cartItems": cartItems,

    }
    return render(request, 'Promotions/sante.html', context)

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()[0:4]

    context = {
        "order": order,
        "items": items,
        "cartItems": cartItems,
        "products": products,

    }
    return render (request, "cart.html", context)

def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


        
    context = {
        "order": order,
        "items": items,
        "cartItems": cartItems,
    }
    return render (request, "checkout.html", context)

# Site informations
def about(request):
    data = cartData(request)

    cartItems = data['cartItems']

    context = {
        "cartItems": cartItems,
    }

    return render (request, "Site_informations/about.html", context)

def blog(request):
    data = cartData(request)

    cartItems = data['cartItems']
    articles = Article.objects.all()

    context = {
        "cartItems": cartItems,
        "articles": articles,
    }

    return render (request, "Site_informations/blog.html", context)

def contact(request):

    return render (request, "Site_informations/contact.html")

def help_center(request):

    return render (request, "Site_informations/help_center.html")

def terms_of_service(request):

    return render (request, "Policies/terms_of_service.html")

def privacy_policy(request):

    return render (request, "Policies/privacy_policy.html")

def shipping_policy(request):

    return render (request, "Policies/shipping_policy.html")

def refund_policy(request):

    return render (request, "Policies/refund_policy.html")

#Site processes
def updateItem(request):
    data = json.loads(request.body)
    print("Data : ", data)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, status="PENDING")

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if(action == 'add'):
        orderItem.quantity += 1
        operation = "Item was added"
        orderItem.save()
    elif(action == 'add-store'):
        orderItem.quantity += 1
        operation = "Item was added from store"
        orderItem.save()
    elif(action == 'remove'):
        if(orderItem.quantity <= 1):
            orderItem.delete()
            operation = "Order item deleted"
        else:
            orderItem.quantity -= 1
            operation = "Item was removed"
            orderItem.save()
    elif (action == "delete"):
        orderItem.delete()
        operation = "Order item deleted from order"

    return JsonResponse(operation, safe=False)

# def addProduct(request):
#     data = json.loads(request.body)
#     productId = data['productId']

#     order = Order.objects.create()
#     print("Order Id", order)

#     return JsonResponse("Order element recorded", safe=False)

def processOrder(request):
    data = json.loads(request.body)
    form = data['form']
    shipping = data['shipping']

    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, status="PENDING")
    else:
        customer, order = guestUser(request, form)

    total = float(form['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.status = order.Status.CONFIRMED
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=shipping['address'],
            country=shipping['country'],
            city=shipping['city'],
            state=shipping['state'],
            zipcode=shipping['zipcode'],


        )

    return JsonResponse("Payment complete", safe=False)