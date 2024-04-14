print('=' *20, end=' ')
print('Desafio 022 - Analisador de Texto', end=' ')
print('=' *20)

"""Iremos criar um programa que leia a nome de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas e minúsculas
 - O total de letras (sem considerar espaços)
  - Quantas letras tem o primeiro nome
"""

nome = input('Insira o nome completo: ').strip()

print('Letras maiúsculas: ', nome.upper())
print('Letras minúsculas: ', nome.lower())

#Calcula a quantidade de letras sem considerar espaços
qdt_letras = len(nome) - nome.count(' ')
print('Quantidade de letras (sem considerar espaços): ', qdt_letras)

#Encontra o primeiro nome e calcula o número de letras nele
primeiro_nome = nome.split()[0]
print('Quantidade de letras no primeiro nome: ',len(primeiro_nome))

""""
Explicando o código:

*Utilizei o método .strip() diretamente após a entrada do usuário para 
remover espaços extras.
*Para calcular a quantidade de letras sem considerar espaços, subtraí 
a quantidade de espaços do comprimento total da string.
*Para encontrar a quantidade de letras do primeiro nome, dividi 
a string pelo espaço e peguei a primeira parte, que é o primeiro nome.

"""