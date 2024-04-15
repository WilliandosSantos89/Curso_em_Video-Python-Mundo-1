print('=' *20, end=' ')
print('Desafio 023 - Separando dígitos de um número', end=' ')
print('=' *20)

"""
Neste projeto, iremos fazer um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados por unidade, dezena, centena e milhar.

"""

n = input('Informe um número de até 4 dígitos: ').zfill(4)

print('Unidade:',n[3])
print('Dezena:',n[2])
print('Centena:', n[1])
print('Milhar:', n[0])

"""
Nesse método, usamos o método .zfill() para garantir que sempre tenha 4 dígitos,
preenchendo com zeros à esquerda, caso a quantidade seja menor.
É um método simples e direto.
Lembre-se que o programa está reconhecendo os caracteres como STRINGS, não como
números, ou seja, caso o usuários digite LETRAS, o programa também irá funcionar.

"""