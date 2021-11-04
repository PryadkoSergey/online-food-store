from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index (request):
    #context = Product.objects.all()
    context = Product.objects.order_by('created')[:8]
    return render(request,'main/index.html', {'context':context})


def pizza (request):
    return render(request,'main/pizza.html' )

def discount (request):
    return render(request,'main/discount.html' )

def sushi (request):
    return render(request,'main/sushi.html' )

def drink (request):
    return render(request,'main/drink.html' )

def cart (request):
    return render(request,'main/cart.html' )

def burger (request):
    return render(request,'main/burger.html' )












