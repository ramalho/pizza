# coding: utf-8

from django.db import models

class Cliente(models.Model):
    ddd = models.CharField(max_length=2, default='11')
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
        ordering = ['logradouro', 'numero'] 
        
    def endereco(self):
        end = '%s, %s' % (self.logradouro, self.numero)
        if self.complemento:
            end += ', ' + self.complemento
        return end
    endereco.short_description = u'endereço'
    