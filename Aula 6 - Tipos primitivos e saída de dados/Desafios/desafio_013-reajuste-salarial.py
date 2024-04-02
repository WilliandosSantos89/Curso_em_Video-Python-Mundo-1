print('=' *20, end=' ')
print('Desafio 013 - Reajuste Salarial', end=' ')
print('=' *20)

#Solicita o salário atual
salario = float(input('Informe seu salário atual: R$ '))

#Calcula um desconto de 15% e já soma com o salário atual
reajuste = salario * (15 / 100) + salario #Optei por fazer em apenas uma linha

#novo_salario = salario + reajuste

#Exibe o novo salário
print('Seu novo salário é R${:.2f}'.format(reajuste))