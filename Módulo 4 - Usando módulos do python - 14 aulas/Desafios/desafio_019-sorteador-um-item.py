import random

print('=' *20, end=' ')
print('Desafio 019 - Sorteando um item na lista', end=' ')
print('=' *20)

alunos = ['Pedro', 'Thiago', 'João', 'Matheus']
print('O aluno escolhido para apagar o quadro foi {}'.format(random.choice(alunos)))

