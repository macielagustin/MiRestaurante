import os
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from app_Restaurante.forms import ClienteForm
from .models import Cliente,FAQ

# Create your views here.

def index(request):
    return render(request, 'app_Restaurante/index.html')

def pedidos(request):
    clientes= Cliente.objects.all()
    return render(request, 'app_Restaurante/pedidos.html',{'clientes':clientes})

def nuevo_pedido(request):
    if request.method == 'POST':
        formpedido = ClienteForm(request.POST, request.FILES)
        if formpedido.is_valid():
            formpedido.save()
            messages.success(request, 'Pedido Agregado!')
            return redirect('index')  # Asegúrate de que 'index' esté definido en tus urls
        else:
            messages.error(request, 'Atención: Verificar datos ingresados')
    else:
        formpedido = ClienteForm()

    return render(request, 'app_Restaurante/nuevo_pedido.html', {'formpedido': formpedido})
    

def eliminar_pedido(request, cliente_id):  # Asegúrate de usar 'cliente_id' aquí
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    archivo = cliente.imagen.path

    cliente.delete()

    if os.path.exists(archivo):
        os.remove(archivo)

    return redirect('pedidos')  

def faq_view(request):
    query = request.GET.get('q', '')
    if query:
        faqs = FAQ.objects.filter(pregunta__icontains=query)
    else:
        faqs = FAQ.objects.all()
    return render(request, 'app_Restaurante/faq.html', {'faqs': faqs, 'query': query})

def preguntas_frecuentes(request):
    faqs = FAQ.objects.all()  # Recupera todas las FAQs
    return render(request, 'app_Restaurante/preguntas_frecuentes.html', {'faqs': faqs})

def sobre_nosotros(request):
    return render(request, 'app_Restaurante/sobre_nosotros.html')