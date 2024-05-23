import re

print('=' *20, end=' ')
print('Desafio 024 - Verificando as primeiras letras de um texto', end=' ')
print('=' *20)


cidade_nascimento = input('Em que cidade você nasceu? ')
procurar = 'santo'


if re.search(procurar, cidade_nascimento, re.IGNORECASE):
    print(f'A cidade {cidade_nascimento} se inicia com {procurar}')

else:
    print(f'A cidade {cidade_nascimento} não se inicia com {procurar}')

