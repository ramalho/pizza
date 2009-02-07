from django.contrib import admin
from pizza.entrega.models import Cliente, Pedido, Entregador, Pizza

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'contato', 'endereco')
    list_display_links = ('fone', 'contato')
    search_fields = ('fone', 'contato', 'logradouro', 'numero')

class PizzaInline(admin.TabularInline):
    model = Pizza

class PedidoAdmin(admin.ModelAdmin):
    inlines = [PizzaInline]
    list_display = ('entrou', 'cliente',
                    'nome_entregador', 'partiu', 'despachado')
    list_display_links = ('entrou', 'cliente')
    
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pedido', '__unicode__')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Entregador)
