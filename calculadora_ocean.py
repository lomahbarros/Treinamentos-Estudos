# Calculadora da Aloma

try:
    num_1 = int(input("Digite o primeiro número "))
    num_2 = int(input("Digite o segundo número "))

except ValueError:
    print("Você não digitou um número inteiro")
    exit()

operacao = input('Qual operação você quer fazer? Para adição digite [+], para subtração digite[-], para multiplicação digite [*]'
'para divisão digite [/]')



if operacao == "+" :
    print(num_1 + num_2)
elif operacao == "-":
    print(num_1 - num_2)
elif operacao == "*":
    print(num_1 * num_2)
elif operacao == "/":    
    if num_1 == 0:  
        print(f"Impossível dividir Zero por {num_2}")
    else:
        print(num_1 / num_2)          
else:
    print("Você não digitou um operador matemático")