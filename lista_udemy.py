import os
lista = []

while True:
    print('Administrar cardapio')
    opcao = input('Digite a primeira letra para inserir, apagar, listar' )

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
       
    elif opcao =='a': 
        indice_str = input('Escolha o índice para apagar')
        indice = int(indice_str)
        del lista[indice]
        print('a')
       
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada disponível para listar')

        for i, valor in enumerate(lista):
            print(i,valor)    
            
    else:
        print('Por favor, escolha alguma das letras para abrir o programa')       