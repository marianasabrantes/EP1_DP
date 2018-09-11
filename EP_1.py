# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:46:14 2018

@author: Mariana Abrantes
"""

a = True
while a:
    cardapio = ['banana']
    print('0 - sair')
    print('1 - imprimir cardápio')
    print('2 - adicionar item')
    print('3 - remover item')
    print('4 - imprimir comanda')
    
    escolha = int(input('Digite uma escolha: '))
    if escolha == 0:
        a = False
        print ('Até mais!')
    elif escolha == 1:
        print('O cardápio possui os seguintes itens: {0}'.format(cardapio))
    elif escolha == 2:
        nome = input('Digite o nome do produto: ')
        quant = int(input('Digite a quantidade do produto: '))
        if nome in cardapio:
            
        else:
            print('Produto não disponivel')