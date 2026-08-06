# Calculadora 

num_1 = input("Digite o primeiro número ")

num_2 = input("Digite o segundo número ")

if type(num_1) != int or type(num_2) != int:
    print("Você não digitou um número inteiro")

operacao = input('Qual operação você quer fazer? Para adição digite [+], para subtração digite[-], para multiplicação digite [*]'
'para divisão digite [/]')

num_1 == int(num_1)
num_2 == int(num_2)


if operacao == "+" :
    print(num_1 + num_2)
elif operacao == "-":
    print(num_1 - num_2)
elif operacao == "*":
    print(num_1 * num_2)
elif operacao == "/":
    print(num_1 / num_2)            
else:
    print("Você não digitou um operador matemático")