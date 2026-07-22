import os
lista = []

print('Administrar cardapio')
while True:
    
    opcao = input('Digite a primeira letra para inserir, apagar, listar:'  )

    if opcao == 'i':
        os.system('cls')
        print('Escreva o nome da nova comida')
        valor = input('Valor: ')
        
        lista.append(valor)
       
    elif opcao =='a': 
       
        indice_str = input('Escolha o índice para apagar')
    
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:    
            print('Não foi possível apagar esse índice')
        except IndexError:   
                print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')        
       
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada disponível para listar')

        for i, valor in enumerate(lista):
            print(i,valor)    
            
    else:
        print('Por favor, escolha alguma das letras para abrir o programa')       