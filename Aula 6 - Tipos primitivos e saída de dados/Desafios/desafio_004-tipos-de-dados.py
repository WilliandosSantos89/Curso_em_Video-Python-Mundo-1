print('*** Desafio 004 - Tipos de dados ***')

n = input('Digite um valor qualquer: ')
tipo = type(n)

print('O tipo primitivo desse valor é ', tipo)

#Verifica se um valor é composto apenas por letras
if n.isalpha():
    print('* {} * contém apenas letras: Sim'.format(n))
else:
    print('* {} * Contém apenas letras? Não'.format(n))

#Verifica se uma string é vazia ou se todos os caracteres estão na tabela ASCII.
if n.isascii():
    print('* {} * Está na tabela ASCII? Sim'.format(n))
else:
    print('* {} * Está na tabela ASCII? Não'.format(n))

#Verifica se todos os caracteres na string são minúsculos.
if n.islower():
    print('* {} * Contém só letras minúsculas? Sim'.format(n)) 
else:
    print('* {} * Contém só letras minúsculas? Não'.format(n)) 

#Verifica se todos os caracteres na string são maiúsculos.
if n.isupper():
    print('* {} * Contém só letras maiúsculas? Sim'.format(n))
else:
    print('* {} * Contém só letras maiúsculas? Não'.format(n))

#Verifica se todos os caracteres são decimais
if n.isdecimal():
    print('* {} * Contém decimais? Sim'.format(n))
else:
    print('* {} * Contém decimais? Não'.format(n))


print(n.isdigit()) #etorna se todos os caracteres na string são dígitos e existe pelo menos um caractere, caso contrário. Dígitos incluem caracteres decimais e dígitos que precisam de tratamento especial, tal como a compatibilidade com dígitos sobre-escritos.
print(n.isidentifier()) #Retorna se a string é um identificador válido conforme a definição da linguagem,

print(n.isnumeric()) #Retorna se todos os caracteres na string são caracteres numéricos, e existe pelo menos um caractere, caso contrário. 
print(n.isspace()) #Retorna se existem apenas caracteres de espaço em branco na string e existe pelo menos um caractere, caso contrário.
print(n.isprintable()) #Retorna se todos os caracteres na string podem ser impressos ou se a string é vazia, caso contrário. Caracteres que não podem ser impressos são aqueles que estão definidos no banco de dados de caracteres Unicode como “Outros” ou “Separadores”, exceto o caractere ASCII que representa o espaço (0x20), o qual é impresso. 
print(n.istitle())

print(n.__init_subclass__())