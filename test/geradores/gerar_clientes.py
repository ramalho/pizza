#!/usr/bin/env python
# coding: utf-8

from random import choice, randint, randrange
from selecao_prob import selecao_prob
from pprint import pprint
from django.utils import simplejson

clientes = [{"pk": 1, "model": "entrega.cliente", "fields": {"ramal": "", "complemento": "ap. 23", "fone": "38163698", "logradouro": "Rua Girassol", "contato": "Luciano", "numero": 1291, "outros_contatos": "Marta", "obs": "", "ddd": "11"}}, {"pk": 2, "model": "entrega.cliente", "fields": {"ramal": "", "complemento": "", "fone": "38121234", "logradouro": "Rua Harmonia", "contato": u"João", "numero": 123, "outros_contatos": "", "obs": "", "ddd": "11"}}]

ruas = u'''
Rua Harmonia, 1014
Rua Jericó, 255
Rua Delfina, 65
Rua Purpurina, 155
Rua Mourato Coelho, 1120
Rua Fidalga, 900
Rua Girassol, 1400
Rua Wizard, 500
Rua Aspicuelta, 800
Rua Rodésia, 200
Travessa Tim Maia, 100
Praça Benedito Calixto, 200
'''

ruas = [(e.split(u',')[0], int(e.split(u',')[1])) for e in ruas.strip().split(u'\n')]

prefixos = u'3031 3032 3034 3812 3813 3815 3816 3097 3819 3037'.split()

predios = []

nomes = file('prenomes.txt').read().decode('utf-8').split()

campos = 'ddd fone ramal contato outros_contatos logradouro numero complemento obs'.split()

def gerar_contatos():
    contatos = set()
    qt = selecao_prob([(60,1),(20,2),(10,3),(10,4),(5,5),(8,7)])
    while len(contatos) < qt:
        contatos.add(choice(nomes))
    return tuple(contatos)
    
for i in range(3,769):
    cli = dict(pk=i, model='entrega.cliente')
    ddd = selecao_prob([(95,'11'),(3,'13'),(2,'19')])
    fone = choice(prefixos) + '%04d' % randint(1,9999)
    tam_ramal = selecao_prob([(90,0),(5,3),(5,4)])
    ramal = ('%04d' % randint(1,9999))[:tam_ramal]
    contatos = gerar_contatos()
    contato = contatos[0]
    if len(contatos) > 1:
        outros_contatos = ', '.join(contatos[1:])
    else:
        outros_contatos = ''
    logradouro, num_max = choice(ruas)
    numero = randint(1, num_max)
    if len(predios) < 50:
        predios.append((logradouro, numero))
    complemento = ''
    if randrange(100) < 30:
        logradouro, numero = choice(predios)
        complemento = 'ap. %d' % (randrange(0,250,10)+randint(1,4))
        if randrange(100) < 15:
            complemento += ' bloco ' + selecao_prob([(45,'A'),(45,'B'),(6,'C'),(4,'D'),])
    if not complemento and (randrange(100) < 3):
        obs = u'cuidado com o cão'
    else:
        obs = ''
    
    cli['fields'] = fields = dict()
    for campo in campos:
        fields[campo] = locals()[campo]
    clientes.append(cli)
    
print simplejson.dumps(clientes)
#pprint(clientes)
