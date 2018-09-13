# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:46:14 2018

@author: Mariana Abrantes
"""
cardapio = {'chocolate': 3, 'jujuba': 2, 'sorvete': 3}
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
        quantidade_produto = int(input('Quantidade inicial: '))
        if novo_item not in cardapio:
            condicao = True
            cardapio[novo_item] = quantidade_produto
            while condicao:
                if quantidade_produto >= 0:
                    cardapio[novo_item] = quantidade_produto
                    condicao = False
                else:
                    print('Não é possível adicionar quantidade negativa.')
                    condicao = False
        else:
            if quantidade_produto < 0:
                print('Não é possível adicionar quantidade negativa.')
            else:
                cardapio[novo_item] += quantidade_produto
    elif escolha == 3:
        del_prod = input('Digite o nome do produto a ser removido: ')
        if del_prod in cardapio:
            quant = int(input('Digite a quantidade a ser removida: '))
            cardapio[del_prod] -= quant
            if cardapio[del_prod] == 0:
                del cardapio[del_prod]
        else:
            print('Produto não encontrado.')
    elif escolha == 4:
        for i in cardapio:
            print('{0}: {1}'.format(i, cardapio[i]))
        
    else:
        print('Opção inváda.')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            