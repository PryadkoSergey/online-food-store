from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category

def index (request):
    #context = Product.objects.all()
    context = Product.objects.order_by('created')[:8]
    return render(request,'main/index.html', {'context':context})


def pizza (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 1)
    return render(request,'main/pizza.html',{'context':context, 'category': category})

def sushi (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 3)
    return render(request,'main/sushi.html',{'context':context, 'category': category})

def drink (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 4)
    return render(request,'main/drink.html',{'context':context, 'category': category})

def cart (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 1)
    return render(request,'main/cart.html',{'context':context, 'category': category})

def burger (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 2)
    return render(request,'main/burger.html',{'context':context, 'category': category})

def discount (request):
    context = Product.objects.all()
    return render(request,'main/discount.html',{'context':context} )












