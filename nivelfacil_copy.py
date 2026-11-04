import pygame
import sys
from funcoes import espalhar_imagem_nivel_facil
from embaralhar import espalhar_cartas_frutas
from carregar_todas_imagens import carregar_imagens


def telanivel_facil():
    global matriz_cartas, matriz_cartas_frutas
    pygame.init()
    matriz_cartas = espalhar_imagem_nivel_facil() # Chama a função para espalhar as cartas
    matriz_cartas_frutas = espalhar_cartas_frutas()

    # Criar janela
    largura, altura = 867,867
    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption("Aloma Jogo tela")

  
    preto = (0,0,0)  #Cores 

    fundo = pygame.image.load("fundo.png")   #Carregar a imagem com mais rapidez atraves da função convert    
    fundo = pygame.transform.scale(fundo, (138, 138))  
    fundo_rect = fundo.get_rect(topleft=(63,63))


    #Loop principal
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        tela.fill(preto) #  Preencher uvaverde com preto

        # for linha in matriz_cartas: # Esse loop, só carrega a imagem de fundo
        #     for carta in linha:             
        #         tela.blit(fundo, carta)
        # pygame.display.flip()

        for linha in matriz4_4frutas: #Esse loop mostra a carta embaralhada e o fundo da foto fundo
            for carta in linha:
                if carta["aberta"]:
                    img = pygame.image.load(carta["imagem"])
                    tela.blit(img, carta["rect"])
                else:
                    tela.blit(fundo, carta["rect"])  # fundo padrão
        

        # # Desenhar texto na tela
        
        #tela.blit(fundo_transformado, fundo_rect)

        # Atualizar tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

telanivel_facil()