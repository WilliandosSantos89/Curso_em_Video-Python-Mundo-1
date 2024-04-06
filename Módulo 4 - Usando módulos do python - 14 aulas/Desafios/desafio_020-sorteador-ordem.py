import random

print('=' *20, end=' ')
print('Desafio 020 - Sorteando um lista ordenada', end=' ')
print('=' *20)

# Solicita ao usuário os itens a serem sorteados
# Criamos uma lista denominada alunos
alunos = []
alunos.append(input('Informe o primeiro aluno: '))
alunos.append(input('Informe o segundo aluno: '))
alunos.append(input('Informe o terceiro aluno: '))
alunos.append(input('Informe o quarto aluno: '))

# Embaralha a lista de alunos
random.shuffle(alunos)

# Mostra o resultado do sorteio
print('A sequência sorteada foi:\n {}\n {}\n {}\n {}'.format(*alunos))
# usamos o asterismo(*) para apontar a lista alunos

