from django.urls import path
from app_Restaurante import views
from .views import eliminar_pedido, faq_view, preguntas_frecuentes

urlpatterns = [
    path('', views.index, name='index'),  # Asegúrate de que esta línea esté correcta
    path('pedidos/', views.pedidos, name='pedidos'),
    path('nuevo_pedido/', views.nuevo_pedido, name="nuevo_pedido"),
    path('eliminar_pedido/<int:cliente_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('faq/', faq_view, name='faq'),
    path('preguntas-frecuentes/', preguntas_frecuentes, name='preguntas_frecuentes'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]
