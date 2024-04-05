import random

print('=' *20, end=' ')
print('Desafio 019 - Sorteando um item na lista', end=' ')
print('=' *20)

# Solicita ao usuário os itens a serem sorteados
a1 = input('Informe o primeiro aluno: ')
a2 = input('Informe o segundo aluno: ')
a3 = input('Informe o terceiro aluno: ')
a4 = input('Informe o quarto aluno: ')

# Variável que contem os itens informados pelo usuário
sorteador = [a1, a2, a3, a4]

# Mostra o resultado do sorteio
print('O aluno escolhido para apagar o quadro foi {}'.format(random.choice(sorteador)))

