#!/usr/bin/env python
# coding: utf-8

''''
------------------------------------------------
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
------------------------------------------------
1913786 Aaron David Magalhaes Pereira
7627592 Aaron Juraski
2643596 Aaron Zarenczanski
'''

from random import shuffle

nomes = []
for lin in file('conv2007.txt'):
    if lin.startswith(lin[0]*8): continue
    lin = lin.strip()
    if not lin: continue
    nomes.append(lin[8:])

shuffle(nomes)

prenomes = [nome.split()[0] for nome in nomes[:700]]

print '\n'.join(prenomes)    