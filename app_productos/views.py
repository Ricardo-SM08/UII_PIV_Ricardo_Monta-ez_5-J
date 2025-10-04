from django.shortcuts import render

# Create your views here.


def mostrar_datos(request):
    """
    Genera y envía una lista de productos a la plantilla.
    """
    
    # 1. Lista de tres diccionarios con datos de productos
    productos_tienda = [
        {
            'nombre': 'Balón de Fútbol Pro', 
            'precio': 45.99, 
            'stock': 150
        },
        {
            'nombre': 'Zapatillas Running Ultra', 
            'precio': 89.50, 
            'stock': 75
        },
        {
            'nombre': 'Camiseta NBA Edición Limitada', 
            'precio': 65.00, 
            'stock': 40
        }
    ]
    
    # 2. Contexto: el diccionario que Django envía a la plantilla
    contexto = {
        'titulo_pagina': 'Tienda Deportiva - Ofertas',
        'productos': productos_tienda  # La lista de diccionarios se pasa aquí
    }
    
    # 3. Renderiza la plantilla, pasando el contexto
    return render(request, 'index.html', contexto)