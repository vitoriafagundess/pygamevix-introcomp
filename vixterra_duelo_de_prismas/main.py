import pygame

# Inicializando o pygame
pygame.init() 

# Definindo o tamanho da janela, variavel em maíuscula em python, significa, "essa variavel é uma constante"
LARGURA = 800
ALTURA = 600

# pygame.display é a parte do pygame que cuida de tudo que aparece na tela
# set.mode cria a janela de jogo
tela = pygame.display.set_mode((LARGURA, ALTURA)) # Largura, altura diz ao pygame o tamanho exato da janela que ele deve criar


# Titulo da janela 
pygame.display.set_caption("Vixterra: Duelo de Prismas")


# Loop que vai manter a janela aberta e funcionando:
rodando = True
while rodando: 
    # 1. Lida com os eventos(fechar a janela, etc.)      
    for evento in pygame.event.get(): # para cada item dentro da lista de eventos, chame esse item de evento e faça algo
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche o fundo da tela com uma cor 
    tela.fill((0, 0, 0)) # código RGB Cor preta

    # Atualiza a tela para mostar oque foi desenhado
    pygame.display.flip()


# o jogo termina
pygame.quit()