print('='*20, end=' ')
print('Desafio 007 - Média Aritimética', end=' ')
print('='*20)

# Solicita as notas do usuário
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))

# Calcula a média
media = (nota1 + nota2) / 2

#Verifica se o aluno está aprovado ou em recuperação
if media >= 6:    
    print('Sua média é ', media)
    print('Você está aprvado!')
else:
    print('Recuperação')



