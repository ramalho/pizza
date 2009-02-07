#!/usr/bin/python
# coding: utf-8

'''
A função `selecao_prob` recebe um mapa de itens e probabilidades relativas
e devolve um item sorteado segundo a probabilidade relativa.

A primeira linha da função calcula soma das probabilidades relativas::

  >>> vencedor = [(2,'Rex'), (1,'Fido')]
  >>> reduce(lambda a,b:a+b, [p for p,q in vencedor])
  3
  
Nos exemplos abaixo, parametrizamos o valor de i em vez de sortear, para 
que os testes sejam repetíveis::

  >>> selecao_prob(vencedor, 0)
  'Rex'
  >>> selecao_prob(vencedor, 1)
  'Rex'
  >>> selecao_prob(vencedor, 2)
  'Fido'
  >>> selecao_prob(vencedor, 3)
  Traceback (most recent call last):
    ...
  IndexError: Indice excede a probabilidade total
  
Agora vamos repetir 10000 vezes com valores aleatórios, e verificar que
'Rex' deve ser sorteado aproximadamente 2 em cada 3 vezes::

  >>> rex = 0
  >>> for i in range(10000):
  ...   if selecao_prob(vencedor) == 'Rex':
  ...     rex += 1
  ...
  >>> 6000 < rex < 7333 # 6666 +/- 10%
  True

'''

from random import randrange

def selecao_prob(probs, i=None):
    prob_tot = reduce(lambda a,b:a+b, [p for p,x in probs])
    if i is None:
        i = randrange(prob_tot)
    tot = 0
    for prob, item in probs:
        tot += prob
        if i < tot:
            return item
    else:
        raise IndexError, 'Indice excede a probabilidade total'
            
if __name__=='__main__':
    from doctest import testmod
    testmod()