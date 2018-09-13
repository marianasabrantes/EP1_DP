# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:46:14 2018

@author: Mariana Abrantes
"""

cardapio = {'chocolate': 3.50, 'jujuba': 2.00, 'sorvete': 3.50}
a = True
while a:
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
        novo_item = str(input('Nome do produto: '))
        if novo_item not in cardapio:
            condicao = True
            cardapio[novo_item] = 0
            while condicao:
                quantidade_produto = int(input('Quantidade inicial: '))
                if quantidade_produto > 0:
                    cardapio[novo_item] = quantidade_produto
                    condicao = False
                    