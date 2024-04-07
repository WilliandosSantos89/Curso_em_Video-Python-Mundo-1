#Manipulação de strings

#Fatiamento
frase = 'Curso em Vídeo Python'
"""print(frase[9]) #índice 9
print(frase[9:13]) #índice 9 ao 12
print(frase[9:21:2]) #9 e 21: argumentos para índices / 2: pula de 2 em 2
print(frase[:5]) #índice zero ao 4
print(frase[15:]) #índice 15 ao último
print(frase[9::3])"""

#Análise
"""print(frase.count('o'))#procura o elemento e achando, mostra o índice
print(len(frase)) #tamanho da string
print(frase.count('o', 0, 13))
print(frase.find('deo')) #indica o índice onde o caractere informado começa"""

#Transformação
"""print(frase.replace('Python', 'Android')) #substitui
print(frase.upper()) #caixa alta
print(frase.lower()) #caixa baixa
print(frase.capitalize()) #só o 1º caractere maiúsculo
print(frase.title()) #iniciais de cada palavra maiúscula
print(frase.strip()) #remove espaços no início e fim
print(frase.rstrip()) #remove espaços da extremidade direita (r)
print(frase.lstrip()) #remove espaços da extremidade esquerda (l)"""

#Divisão
print(frase.split()) #gera uma lista com cada palavra da cadeia (espaço)

#Junção
print('-'.join(frase))
