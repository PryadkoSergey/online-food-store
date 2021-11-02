from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request,'main/index.html' )


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












