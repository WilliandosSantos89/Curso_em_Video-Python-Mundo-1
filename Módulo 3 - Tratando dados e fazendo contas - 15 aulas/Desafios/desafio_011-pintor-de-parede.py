print('=' *20, end=' ')
print('Pintando a parede', end=' ')
print('=' *20)



#Neste projeto, vamos calcular quantos litros de tinta são necessários para pintar
#uma parede de acordo com a largura, altura e área dadas pelo usuário

#Socilita ao usuário a largura e altura da parede
largura = float(input('Informe a largura da perede: '))
altura = float(input('Informe a altura da perede: '))

#Calcula a área
area = float(largura*altura)

#Calcula quantos litros de tinta serão necessários
tinta_necessaria = area * 2


#Exibe altura,largura e área
print('Largura da parede: {:.2f}'.format(largura))
print('Altura da parede: {:.2f}'.format(altura))
print('A área é de {}m²'.format(area))

#Exibe a tinta necessária, em litros, para pintar a parede
print('Você precisará de {} litros de tinta.'.format(tinta_necessaria))