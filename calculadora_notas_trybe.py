# Criar a calculadora
# Permitir ler cada nota 
# Calcular a média 
# Se > 6 - Aprovado
# Se < 6 - Reprovado


nota_1 = 5
nota_2 = 9
nota_3 = 6

soma_das_notas = nota_1 + nota_2 + nota_3
media_notas = soma_das_notas / 3

print(media_notas)

if media_notas > 6:
    print('Aprovado')
else:
    print('Reprovado')    