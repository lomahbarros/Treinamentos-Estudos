#Crie um print para "Seu pedido de pizza {sabor_escolhido} está sendo preparado"

pedido = input("Bem-vindo, para pizza digite [p] ")

sabores = ["Calabresa", "Mussarela", "Portuguesa"]

if pedido == "p":
    print("Cardápio de sabores:")
    for indice, sabor in enumerate(sabores):
        print(f"{indice} - {sabor}")

    indice_escolhido = int(input("Escolha o sabor digitando o índice: "))
    sabor_escolhido = sabores[indice_escolhido]

    print(f"Seu pedido de pizza {sabor_escolhido} está sendo preparado")
else:
    print("Pedido não reconhecido.")
