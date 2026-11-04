#embaralha somente o texto e nao a imagem das frutas
import pygame
import random

lista_imagens = [
    "Maçã.png",
    "Banana.png",
    "Laranja.png",
    "Uva Roxa.png",
    "Morango.png",
    "Abacaxi.png",
    "Manga.png",
    "Melancia.png",
    "Kiwi.png",
    "Mamão.png",
    "Pêra.png",
    "Pêssego.png",
    "Ameixa.png",
    "Limão.png",
    "Limão Siciliano.png",
    "Tangerina.png",
    "Romã.png",
    "Côco.png",
    "Goiaba.png",
    "Carambola.png",
    "Abacate.png",
    "Cereja.png",
    "Amora.png",
    "Uva Verde.png",
    "Caqui.png",
    "Maracujá.png",
    "Pitaia.png",
    "Mirtilo.png",
    "Siriguela.png",
    "Acerola.png",
    "Tomate.png",
    "Maçã Verde.png"]



def espalhar_cartas_frutas():
    cartas = lista_imagens * 2  # duplica para formar pares
    random.shuffle(cartas)      # embaralha

    x_inicial = 63
    y_inicial = 63
    tamanho_do_fundo = 138   
    espacamento = 62

    matriz4_4frutas=[] # Crio a matriz
    indice = 0
    for l in range(4):
        linha = [] # lista para criar a 4 linha
        for c in range(4):
            # coluna= []
            # Calcular posicao da carta
            x = x_inicial + c * (tamanho_do_fundo + espacamento) # O valor de x é x inicial + o indice da coluna ...
            y = y_inicial + l * (tamanho_do_fundo + espacamento)
            rect = pygame.Rect(x, y, tamanho_do_fundo, tamanho_do_fundo)

            carta = {
                "imagem": cartas[indice],   # nome da imagem embaralhada
                "rect": rect,               # posição na tela
                "aberta": False,  # estado inicial (fechada)
                "fundo": fundo             # verso da carta        #ACREDITO QUE SEJA NECESSARIO CARREGAR TBM NESSE MODULO 
            }
            linha.append(carta)
            indice += 1
        matriz4_4frutas.append(linha)

    return matriz4_4frutas


