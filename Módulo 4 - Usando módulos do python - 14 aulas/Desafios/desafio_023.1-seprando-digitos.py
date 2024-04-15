print('=' *20, end=' ')
print('Desafio 023 - Separando dígitos de um número', end=' ')
print('=' *20)

"""
Neste projeto, iremos fazer um programa que leia um número de 0 a 9999 e mostre
na tela cada um dos dígitos separados por unidade, dezena, centena e milhar.

"""

n = int(input('Informe um número de até 4 dígitos: '))

unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)

"""
Nesse exemplo, já refinamos mais o código de forma a evitar que o usuário digite
LETRAS, ao invés de números. 

1. unidade = n % 10 - Aqui, usamos o operador de módulo % para obter o resto da divisão 
de n por 10, o que nos dá o último dígito do número, ou seja, a unidade.

2. dezena = (n // 10) % 10 - Primeiro, n // 10 divide n por 10 e descarta o último 
dígito (a unidade), depois % 10 pega o resto da divisão do resultado por 10, 
o que nos dá o penúltimo dígito, ou seja, a dezena.

3. centena = (n // 100) % 10 - Similarmente, n // 100 divide n por 100, descartando os dois 
últimos dígitos, e % 10 nos dá o terceiro dígito a partir da direita, a centena.

4. milhar = (n // 1000) % 10 - Finalmente, n // 1000 divide n por 1000, deixando apenas 
o primeiro dígito se houver, e % 10 nos dá esse dígito, o milhar.

Essas operações são baseadas na forma como os números são construídos em nosso sistema decimal, 
onde cada posição de dígito representa uma potência de 10.

"""