print('=' *20, end=' ')
print('Desafio 022 - Analisador de Texto', end=' ')
print('=' *20)

"""Iremos criar um programa que leia a nome de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas e minúsculas
 - O total de letras (sem considerar espaços)
  - Quantas letras tem o primeiro nome
"""

nome = input('Insira o nome completo: ')

print('Letras maiúsculas: ', nome.upper())
print('Letras minúsculas: ', nome.lower())
novo_nome = nome.strip() 
print('Quantidade de letras (espaços não considerados): ',len(novo_nome))
dividido = novo_nome
print('Quantidade de letras do 1º nome: ',dividido[0])