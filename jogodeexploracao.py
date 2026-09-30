

# Crie uma Lista de Salas:
salas = ["sala01", "sala02", "sala03", "sala04", "sala05", "sala06", "sala07", ]

# Defina uma lista para armazenar os nomes das salas dos calabouços.
nomes_das_salas = ["Poco dos desejos", "Tavena sem portas",  "Abismo das Sombras", "Cripta dos Suplícios", "Galeria dos Ossos", "Enclave da Perdição", "Poço da Penumbra"]
descricao_das_salas = ["Possui um lago de lama", "Paredes húmidas e revestidas por pedras", "Possui um fosse silencioso", "possui o ambiente frio com vozes das paredes", "Toda a sala e revestida de ossos", "Senssação constante de esta sendo observado", "Possui um fosse silencioso"]

# Inicie outra lista, vazia por agora, para representar as salas visitadas.
salas_visitadas = []



# Use um loop para simular a exploração do calabouço. Dentro do loop:
for sala in nomes_das_salas:
    salas_visitadas.append(sala)
    
# Imprima a sala atual (acesse o último elemento da lista de salas visitadas)    
print(f"A atual sala que wendigo está é {salas_visitadas[-1]}\n Você pode escolher qual sala ele deve voltar ")

for posicao, sala in enumerate(nomes_das_salas): 
    print(f"[{posicao}] {sala}")



    indice = -1
while True:
    # Provenha opções para o jogador escolher a próxima sala do jogo para explorar (de uma lista de salas)
    indice = int(input("PARA VISITAR, DIGITE O ÍNDICE CORRESPONDENTE, OU [9] PARA SAIR: "))
# Caso o jogador decida sair, remova a última sala visitada (simulando voltar)
    if indice == 9:
        if salas_visitadas:
            salas_visitadas.pop()
        break
        # Baseado na escolha do jogador, adicione ao final a nova sala em salas visitadas.
    if 0 <= indice < len(nomes_das_salas):
        salas_visitadas.append(nomes_das_salas[indice])
    else:
        print("Índice inválido.")        
            
print(f"RESUMO DA EXPLORAÇÃO\n A Salas vistadas foram {salas_visitadas}")

for nome,descricao in zip(nomes_das_salas, descricao_das_salas):
    print(nome,descricao)







# # Imprima um Resumo da Exploração:
# print(f" As salas que foram visitadas {salas_visitadas}")