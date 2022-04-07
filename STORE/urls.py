from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('acercade', views.acercade, name = 'acercade'),
    path('busqueda', views.busqueda, name = 'busqueda'),
    path('carrito', views.carrito, name = 'carrito'),
    path('contacto', views.contacto, name = 'contacto'),
    path('pago', views.pago, name = 'pago'),
    path('producto', views.producto, name = 'producto'),
    path('teclado', views.teclado, name = 'teclado'),
    path('ratones', views.ratones, name = 'ratones'),
    path('digitalizadoras', views.digitalizadoras, name = 'digitalizadoras'),
    
    #path('registro', views.registro, name = 'registro'),
    path('update_item', views.updateItem, name = 'update_item'),
    

    
]
