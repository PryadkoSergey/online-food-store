
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index, name='home'),
    path('pizza',views.pizza, name='pizza'),
    path('discount',views.discount, name='discount'),
    path('sushi',views.sushi, name='sushi'),
    path('drink',views.drink, name='drink'),
    path('cart',views.cart, name='cart'),
    path('burger',views.burger, name='burger')
]

# В режиме дебаг обращаться у картинке по такому URL:
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)