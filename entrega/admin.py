from django.contrib import admin
from pizza.entrega.models import Cliente, Pedido, Pizza, Entregador

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'contato', 'endereco')
    list_display_links = ('fone', 'contato')
    search_fields = ('fone', 'contato', 'logradouro', 'numero')

class PizzaInline(admin.StackedInline):
    model = Pizza

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PizzaInline]
    list_display = ('entrou', 'cliente', 'despachado', 'viagem')
    list_display_links = ('entrou', 'cliente')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Entregador)
