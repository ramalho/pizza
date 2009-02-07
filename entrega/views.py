# coding: utf-8

from django.shortcuts import render_to_response
from entrega.models import Pizza, Pedido, Cliente
from django import forms

def listar_pizzas(request):
    pizzas = Pizza.objects.all()
    vars = {'pizzas':pizzas}
    return render_to_response('entrega/preparo.html', vars)
    
def ver_pedido(request):
    msg = ped = None
    idp = request.GET.get('id_pedido')
    if idp:
        try:
            ped = Pedido.objects.get(id=idp)
        except Pedido.DoesNotExist:
            msg = u'Não existe pedido #%s' % idp            
    vars = {'ped':ped, 'msg':msg}
    return render_to_response('entrega/pedido.html', vars)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ('outros_contatos', 'obs',)
        
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('entrega/cadastro_confirmado.html', form.cleaned_data)    
    else:
        form = ClienteForm()                    
    vars = {'form':form}
    return render_to_response('entrega/cadastro.html', vars)
    