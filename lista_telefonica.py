lista = []

while True:
    print("1) Adicionar Contato")
    print("2) Remover contato")
    print("3) Exibir a agenda")
    print("0) Sair")
    opcao = int(input("Digite uma opção [0-3]:"))

    if opcao ==0:
        break

    elif opcao ==1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        contato = {"nome": nome, "telefone": telefone}
        lista.append(contato)

    elif opcao ==2:
        nome = input("Digite o nome do contato que deseja remover") 
        
        contato_encontrado = False # Criando essa variavel, para for não interar a lista mostrando mensagem iten a inten, somente mostrar quando encontrar
        for contato in lista: # For intera o nome das chaves dos dicionários
            if contato["nome"] == nome:
                lista.remove(contato)
                print(f"{nome} foi removido.")  
            #else: Se esse else ficar nessa estrutura, toda vez que não encontrar ele vai mostrar essa mensagem, caso tenha 100 nomes terá sem texto como esse
                # print(f"{nome} não foi encontrato")
                contato_encontrado = True
                break # Quando o contato for entrontrado, parar o loop
        if contato_encontrado == False:
            print(f"{nome} não foi encontrato")

    elif opcao == 3:
        print("\nLISTA DE CONTATOS:")
        for contato in lista:
            print(f"Nome: {contato['nome']} ") # Uso de aspas simples é apenas para não confundir o programa
            print(f"Telefone: {contato['telefone']}")
    else:
        print("Opção inválida")