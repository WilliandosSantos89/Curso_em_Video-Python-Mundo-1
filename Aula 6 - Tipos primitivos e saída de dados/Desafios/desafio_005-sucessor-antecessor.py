print('='*20, end=' ')
print('Desafio 005 - Sucessor e Antecessor', end=' ')
print('='*20)

n = int(input('Digite um número: '))

sucessor = n + 1
antecessor = n - 1

print('O sucessor de {} é {}'.format(n, sucessor))
print('O antecessor de {} é {}'.format(n, antecessor))