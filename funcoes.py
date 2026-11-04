# Criar botões iniciais
import pygame

def criar_botoes_iniciais():
    x = 96
    y = 587
    tamanho_do_botao = 150
    altura_do_botão = 50
    espaco_entre_botoes = 50

    botoes= []

    for i in range(3):
        botao = pygame.Rect(x, y,  tamanho_do_botao,altura_do_botão)
        botoes.append(botao)
        x += tamanho_do_botao + espaco_entre_botoes

    return botoes


def espalhar_imagem_nivel_facil():
    x_inicial = 63
    y_inicial = 63
    tamanho_do_fundo = 138
    largura_do_fundo = 138
    espacamento = 62

    matriz4_4 =[] # Crio a matriz
    for l in range(4):
        linha = [] # lista para criar a 4 linha

        for c in range(4):
            # coluna= []
            # Calcular posicao da carta
            x = x_inicial + c * (tamanho_do_fundo + espacamento) # O valor de x é x inicial + o indice da coluna ...
            y = y_inicial + l * (tamanho_do_fundo + espacamento)
            carta_fundo = pygame.Rect(x, y, tamanho_do_fundo, tamanho_do_fundo)
            linha.append(carta_fundo) # Adicione na minha linha as colunas

        matriz4_4.append(linha) # Adicione na minha matriz as linhas com as colunas já adicionadas no loop interno

    return matriz4_4