from django.shortcuts import render_to_response
from entrega.models import Pizza

def listar_pizzas(request):
    pizzas = Pizza.objects.all()
    template_vars = {'pizzas':pizzas}
    return render_to_response('entrega/preparo.html', template_vars)