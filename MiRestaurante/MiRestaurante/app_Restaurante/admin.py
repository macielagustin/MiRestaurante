from django.contrib import admin

# Register your models here.

from .models import Pedido,Cliente

class PedidoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'id')

class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre', 'pedido','email','imagen', 'creado','editado')
    list_filter=('pedido','creado')

admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Cliente,ClienteAdmin)