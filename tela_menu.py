import pygame
import sys
from nivelfacil import telanivel_facil


def tela_menu():
    pygame.init()

    # Criar janela
    largura, altura = 800,800
    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption("Texto no Pygame")

    # Carrega a musica
    pygame.mixer.init()  # Inicializa a musica                      
    pygame.mixer.music.load("abertura.mp3")   # Carrega na memôria
    pygame.mixer.music.play(1) # Play na misica
    pygame.mixer.music.set_volume(0.0)   #  Volume da música                                      

    # Definir fonte 
    fonte = pygame.font.SysFont(None, 72) # Fonte o titulo 
    fonte1 = pygame.font.SysFont(None, 25) # Fonte no menu

    # Telas
    tela_atual = "menu"
    tela_anterior = None


    cores = {"branca": (255,255,255),
            "preta": (0,0,0),
            "amarela" : (255, 255, 0),
            "azul" : (0,0,255),
            "verde": (0,255,0),
            "rosaaloma": (255,0,255),
            "amareloaloma": (228,245,11),
            "azulzinho": (2,219,248),
            "cinzaclaro": (165, 165,165)
            }



    def criar_botoes_iniciais(): # Função para criar o esqueleto do retângulo 
        x = 125
        y = 587
        tamanho_do_botao = 150
        altura_do_botão = 50
        espaco_entre_botoes = 50

        botoes= []

        for i in range(3):
            botao = pygame.Rect(x, y,  tamanho_do_botao,altura_do_botão,) #Cria o esqueleto do retângulo 
            botoes.append(botao)
            x += tamanho_do_botao + espaco_entre_botoes

        return botoes

    botoes_iniciais = criar_botoes_iniciais() # Variavel para receber o retorno do botoes e chamar a funcao criar_botoes_iniciais(
    lista_botoes_iniciais = ["Fácil", "Médio", "Difícil"]

    # Criar texto 
    texto = fonte.render("BrainFruit", True, (255, 255, 255)) # Esqueleto do titulo

    # Centralizar o texto na tela
    texto_rect = texto.get_rect(center=(largura//2, altura//2))
    #nivel_rect = fonte1.get_rect(center=(96,587))

    # Loop principal
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Se o click for no botão esquerdo abre a tela do jogo facil
                if botoes_iniciais[0].collidepoint(evento.pos):
                    tela_atual = "nivelfacil"

        # Preencher fundo com preto
        tela.fill((0, 0, 0)) 

  
        if tela_atual == "nivelfacil":
            telanivel_facil()

               

        # Desenhar texto na tela
        tela.blit(texto, texto_rect)
        
        for i, botao in enumerate(botoes_iniciais):
            pygame.draw.rect(tela, cores["cinzaclaro"], botao) #Desenhe o fundo do botao

            niveis = fonte1.render(lista_botoes_iniciais[i], True, cores["rosaaloma"]) # Renderiza a fonte1, escreve o texto que está na lista lista_botoes_iniciais, define a cor
            texto_niveis = niveis.get_rect(center=botao.center)
            tela.blit(niveis, texto_niveis)

        # Atualizar tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

tela_menu()