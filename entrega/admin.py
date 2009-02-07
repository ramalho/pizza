from django.contrib import admin
from pizza.entrega.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('fone', 'contato', 'endereco')
    list_display_links = ('fone', 'contato')
    search_fields = ('fone', 'contato', 'logradouro')

admin.site.register(Cliente, ClienteAdmin)
