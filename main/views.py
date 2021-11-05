from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category

from django.core.paginator import Paginator
from django.views.generic import ListView



class ContactListView(ListView):
    paginate_by = 2
    model = Product

def index (request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    context = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'context': context})


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
    
def burger (request):
    context = Product.objects.all()
    category = Category.objects.get(pk = 2)
    return render(request,'main/burger.html',{'context':context, 'category': category})

def discount (request):
    contact_list = Product.objects.all()
    paginator = Paginator(contact_list, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    context = paginator.get_page(page_number)
    return render(request,'main/discount.html',{'context':context} )


def cart (request):
    context = Product.objects.all()
    return render(request,'main/cart.html',{'context':context})












