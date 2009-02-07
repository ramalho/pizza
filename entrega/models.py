# coding: utf-8

from django.db import models

DDD_DEFAULT = u'11'

class Cliente(models.Model):
    ddd = models.CharField(max_length=2, default=DDD_DEFAULT)
    fone = models.CharField(max_length=8, db_index=True)
    ramal = models.CharField(max_length=4, blank=True, db_index=True)
    contato = models.CharField(max_length=64, db_index=True)
    outros_contatos = models.TextField(blank=True)
    logradouro = models.CharField(max_length=32, db_index=True)
    numero = models.PositiveIntegerField(u'número', db_index=True)
    complemento = models.CharField(max_length=32, blank=True)
    obs = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['ddd', 'fone', 'ramal']
        # no admin, apenas o primeiro criério de ordenação é usado
        # http://docs.djangoproject.com/en/dev/ref/models/options/#ordering
        ordering = ['fone', 'ramal'] 
        
    def __unicode__(self):
        fone = self.fone
        if self.ddd != DDD_DEFAULT:
            fone = '(%s)%s' % (self.ddd, fone)
        if self.ramal:
            fone += ' r.' + self.ramal
        return u'%s - %s' % (fone, self.contato)

    def endereco(self):
        end = '%s, %s' % (self.logradouro, self.numero)
        if self.complemento:
            end += ', ' + self.complemento
        return end
    endereco.short_description = u'endereço'
    
class Pedido(models.Model):
    inclusao = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    entregador = models.ForeignKey('Entregador', null=True, blank=True)
    partida = models.TimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-inclusao']
    
    def __unicode__(self):
        return u'%s / %s' % (self.entrou(), self.cliente)

    def entrou(self):
        return self.inclusao.strftime('%H:%M')

    def nome_entregador(self):
        return self.entregador and self.entregador or ''

    def partiu(self):
        if self.partida:
            return self.partida.strftime('%H:%M')
        else:
            return ''

    def despachado(self):
        return (self.entregador is not None) and (self.partida is not None)
    despachado.boolean = True            

class Entregador(models.Model):
    nome = models.CharField(max_length=64)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.nome, self.id)
    
    class Meta:
        verbose_name_plural = u'Entregadores'

SABORES = [
    ('atum' ,u'Atum'),
    ('calabresa' ,u'Calabresa'),
    ('catupiry' ,u'Catupiry'),
    ('marguerita' ,u'Marguerita'),
    ('mussarela' ,u'Mussarela'),
    ('portuguesa' ,u'Portuguesa'),
    ('quatro queijos' ,u'Quatro Queijos'),
]
    
class Pizza(models.Model):
    pedido = models.ForeignKey(Pedido)
    sabor1 = models.CharField(u'sabor 1', max_length=32, choices=SABORES)
    coberto1 = models.BooleanField(u'cob.')
    sabor2 = models.CharField(u'sabor 2', max_length=32, choices=SABORES, blank=True)
    coberto2 = models.BooleanField(u'cob.')

    def __unicode__(self):
        sabor = self.sabor1
        if self.coberto1:
            sabor += ' coberta'
        if self.sabor2:
            sabor2 = self.sabor2
            if self.coberto2:
                sabor2 += ' coberta'
            sabor = u'½ %s, ½ %s' % (sabor, sabor2) 
        return sabor
    
