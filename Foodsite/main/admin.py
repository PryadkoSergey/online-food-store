from django.contrib import admin

# Register your models here.
from .models import *

class StatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'time']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['nameUser', 'phone', 'readyStatus', 'price', 'paid', 'IdTelegram', 'created', 'updated']
    list_editable = ['readyStatus', 'IdTelegram']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'info']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price','image', 'created', 'updated','show']
    list_editable = ['category', 'price','image', 'show']


class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['product', 'percent', 'show']
    list_editable = ['percent', 'show']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'order']


admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Discounts, DiscountsAdmin)
