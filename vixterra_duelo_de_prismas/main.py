import pygame #bliblioteca pygame
import random # chama a bliblioteca que lida com coisas aleatórias

# Inicializando o pygame
pygame.init() 

# Definindo o tamanho da janela, variavel em maíuscula em python, significa, "essa variavel é uma constante"
LARGURA = 1024
ALTURA = 768

# pygame.display é a parte do pygame que cuida de tudo que aparece na telaset.mode cria a janela de jogo
tela = pygame.display.set_mode((LARGURA, ALTURA)) # Largura, altura diz ao pygame o tamanho exato da janela que ele deve criar


# Titulo da janela 
pygame.display.set_caption("Vixterra: Duelo de Prismas")



# 2. As "plantas" das classes(modelo, define o que todas as "casas construidas" a partir dela devem ter, 2 quartos,  1 sala...) 
class Card:
    def __init__(self, name, category, value, attack):  # init É a função que inicializa o seu objeto, garantindo que ele já nasça com todas as características que você definiu.
        self.name = name                     #self é a maneira que o python tem de se referir ao objeto que esta sendo criado
        self.category = category 
        self.value = value
        self.attack = attack

# 3. Criação dos objetos( 30 cartas)
        #Targon (7 cartas) como se fosse o nípe copas na bisca por exemplo, ai no nipe copas tem as cartas de copas
solvix = Card("Solvix", "Targon", 11, "Algoritmo Instituinte") #como se fosse o ás na bisca
print(solvix.name)
print(solvix.value)
guardiao_da_ordem = Card("Guardião da ordem", "Targon", 10, "")    # como se fosse o 7 na bisca
rei_slugpantheon = Card("Rei Slugpantheon", "Targon", 4, "")        # rei
rainha_slugdiana = Card("Rainha SlugDiana","Targon", 3, "")         #rainha
cavaleiro_slugleona = Card("Cavaleiro Slugleona", "Targon", 2, "")  # valete
targon_unidade_hexteck = Card("Unidade Hexteck de Targon", "Targon", 0, "")  #as cartas que não vale nada na bisca
targon_isca_hexteck = Card("Isca Hexteck de Targon", "Targon", 0, "")

        #Piltover(7 cartas) como se fosse outro nipe
caityslug = Card("Caityslug", "Piltover", 11, "Disparo Calibrado")    #padrão de valores se repete para cada nipe
guardiao_da_tecnologia = Card("Guardião da Tecnologia", "Piltover", 10, "")
rei_slugheimer = Card("Rei SlugHeimer", "Piltover", 4, "")
rainha_slugjinx = Card("Rainha SlugJinx","Piltover", 3, "")
cavaleiro_caveirslug = Card("Cavaleiro Caveirslug", "Piltover", 2, "")
piltover_unidade_hexteck = Card("Unidade Hexteck de Piltover", "Piltover", 0, "")
piltover_isca_hexteck = Card("Isca Hexteck de Piltover", "Piltover", 0, "")

        #Zaun (7 cartas) representa outro nipe
samira = Card("Samira", "Zaun", 11, "Estilo Desafiador")    #padrão  se repete para cada nipe
guardiao_da_mutacao = Card("Guardião da Mutação", "Zaun", 10, "")
rei_slugsinged = Card("Rei SlugSinged", "Zaun", 4, "")
rainha_slugcamille = Card("Rainha SlugCamille","Zaun", 3, "")
cavaleiro_slugekko = Card("Cavaleiro SlugEkko", "Zaun", 2, "")
zaun_unidade_hexteck = Card("Unidade Hexteck de Zaun", "Zaun", 0, "")
zaun_isca_hexteck = Card("Isca Hexteck de Zaun", "Zaun", 0, "")
 
# Ultilizando lista para orgazinar todas as cartas em um unico local, uma lista é como uma gaveta que guarda varios itens,
#facilita manipulação

baralho = [
    solvix, guardiao_da_ordem, rei_slugpantheon, rainha_slugdiana, cavaleiro_slugleona,
    targon_unidade_hexteck, targon_isca_hexteck,

    caityslug, guardiao_da_tecnologia, rei_slugheimer, rainha_slugjinx, cavaleiro_caveirslug,
    piltover_unidade_hexteck, piltover_isca_hexteck,

    samira, guardiao_da_mutacao, rei_slugsinged, rainha_slugcamille, cavaleiro_slugekko,
    zaun_unidade_hexteck, zaun_isca_hexteck
]

# função que mistura coisas dentro de uma lista
random.shuffle(baralho)

#distribuindo as cartas para as mão do jogador e do computador

    #cria uma lista vazia para as mãos 
mao_jogador = [] 
mao_computador = []
    #distribuir 3 cartas para cada jogador
for _ in range(3):  # for com _ quer dizer --> execute este loop 3 vezes, mas não se preocupe em gaurdar o numero na variavel pq nn vai ser usado
    mao_jogador.append(baralho.pop(0)) # a função POP é usada para retirar um item da lista e devolver esse item para algum lugar no meu caso vai adicionar a mão do jogador
    mao_computador.append(baralho.pop(0))

print("Sua mão:") #imprime sua mão no terminal
for carta in mao_jogador: #loop que percorre a sua mao, a cada vez que o loop roda a variavel carta se torna uma das cartas que esta na sua mao
    print(f"- {carta.name} (Valor: {carta.value})")

print("\nMão do computador:")
for carta in mao_computador:
    print(f"- {carta.name}") #f-string permite que voce use variavie diretamente dentro do texto
# Loop que vai manter a janela aberta e funcionando:
rodando = True
while rodando: 
    # 1. Lida com os eventos(fechar a janela, etc.)      
    for evento in pygame.event.get(): # para cada item dentro da lista de eventos, chame esse item de evento e faça algo
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche o fundo da tela com uma cor 
    tela.fill((255, 0, 0)) # código RGB Cor preta

    # Atualiza a tela para mostar oque foi desenhado
    pygame.display.flip()


# o jogo termina
pygame.quit()