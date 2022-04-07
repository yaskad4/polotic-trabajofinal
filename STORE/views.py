from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
#from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# Create your views here.
def index(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []

    products = Product.objects.filter().order_by('-id')[0:3]
    restoproducts = Product.objects.filter().order_by('-id')[3:]


    context = {'products':products, 'restoproducts':restoproducts, 'cartItems': cartItems}

    return render(request,'store/index.html',context)

def acercade(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []

    context = {'cartItems': cartItems}
    return render(request,'store/acercade.html',context)

def busqueda(request):
    context = {}
    return render(request,'store/busqueda.html',context)

def carrito(request):
    # chequeo si mi user esta autentificado
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order, 'cartItems':cartItems}

    return render(request,'store/carrito.html',context)

def contacto(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []
    context = {'cartItems':cartItems}
    return render(request,'store/contacto.html',context)

def login(request):

    context = {}
    return render(request,'store/login.html',context)

def pago(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'cartItems':0}

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/pago.html',context)

def producto(request):

    product = Product.objects.get(id=productId)
    context = {'productid':productId}
    return render(request,'store/producto.html',context)

def registro(request):
    context = {}
    return render(request,'store/registro.html',context)


def updateItem(request):
    data = json.loads(request.body)
    print(type(data))
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    print('Action:', action)
    print('productID:', productId)
    return JsonResponse('Producto añadido', safe=False)

def teclado(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []
    products = Product.objects.filter(category_id="2")
    context = {'products':products,'cartItems':cartItems}
    return render(request,'store/teclado.html',context)

def digitalizadoras(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []
    products = Product.objects.filter(category_id="3")
    context = {'products':products,'cartItems':cartItems}
    return render(request,'store/digitalizadoras.html',context)

def ratones(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
        
    else:
        cartItems = []
    products = Product.objects.filter(category_id="1")
    context = {'products':products,'cartItems':cartItems}
    return render(request,'store/ratones.html',context)


def busqueda(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items    
    else:
        cartItems = []

    if request.method == "POST":
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains=searched)
        context={'searched':searched, 'products':products,'cartItems':cartItems}
        return render(request, 'store/busqueda.html',context)
    else:
        context ={'searched':searched, 'cartItems':cartItems}
        return render(request, 'store/busqueda.html',context)
    
    