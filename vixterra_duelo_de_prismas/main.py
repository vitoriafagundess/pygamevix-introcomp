import pygame #bliblioteca pygame
import random # chama a bliblioteca que lida com coisas aleatórias
import sys
import os  # <--- IMPORTANTE PARA O EXECUTÁVEL

# --- FUNÇÃO  PARA O EXECUTÁVEL FUNCIONAR 
def resource_path(relative_path):
    try:
        # PyInstaller cria uma pasta temporária em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# -------------------------------------------------

# Inicializando o pygame
pygame.init() 

# Definindo o tamanho da janela, variavel em maíuscula em python, significa, "essa variavel é uma constante"
LARGURA = 1366
ALTURA = 900

# pygame.display é a parte do pygame que cuida de tudo que aparece na telaset.mode cria a janela de jogo
tela = pygame.display.set_mode((LARGURA, ALTURA)) # Largura, altura diz ao pygame o tamanho exato da janela que ele deve criar


# Titulo da janela 
pygame.display.set_caption("Vixterra: Duelo de Prismas")



# 2. As "plantas" das classes(modelo, define o que todas as "casas construidas" a partir dela devem ter, 2 quartos,  1 sala...) 
class Card:
    def __init__(self, name, category, value, attack,image_file,):  # init É a função que inicializa o seu objeto, garantindo que ele já nasça com todas as características que você definiu.
        self.name = name                     #self é a maneira que o python tem de se referir ao objeto que esta sendo criado
        self.category = category 
        self.value = value
        self.attack = attack
        self.image_file = image_file #Guarda  o caminho do arquivo
        self.image = None #Guarda a imagem carregada pelo pygame



# Variavel que indica se o 10 do trunfo ja foi jogado
dez_trunfo_jogado = False 


#função para jogada do jogador
'''
def jogada_jogador_mouse(mao_jogador, cartas_retangulos):
    print("Sua vez de jogar!")
    print("Suas cartas:")

    for i, carta in enumerate(mao_jogador):
        print(f"[{i+1}] - {carta.name} ({carta.category}/valor:{carta.value})")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = evento.pos  # posição do clique do mouse

                # verifica qual carta foi clicada
                for idx, rect in enumerate(cartas_retangulos):
                    if rect.collidepoint(pos):
                        carta_jogada_jogador = mao_jogador[idx]

                        # --- lógica do Ás do trunfo ---
                        if carta_jogada_jogador.value == 11 and carta_jogada_jogador.category == trunfo.category:
                            if len(mao_jogador) > 1:
                                cartas_10_mesmo_nipe = [c for c in mao_jogador + mao_computador + baralho
                                                        if c.value == 10 and c.category == carta_jogada_jogador.category]
                                if cartas_10_mesmo_nipe:
                                    print("Atenção: o Ás do trunfo não pode ser jogado antes do 10! Escolha outra carta.")
                                    break  # volta para o while e espera outro clique

                        # se passou na regra do Ás ou não é Ás, remove da mão e retorna
                        return mao_jogador.pop(idx)
'''



def filtrar_as_trunfo(mao_computador, mao_jogador, baralho, trunfo):
    """
    Retorna a lista de cartas válidas para o computador.
    Regras:
    - Bloqueia o Ás do trunfo se o 10 do mesmo naipe ainda não saiu,
      exceto se for a única carta ou se o 10 já tiver sido jogado.
    """

    # Se só tem uma carta, obrigatoriamente joga ela
    if len(mao_computador) == 1:
        return mao_computador  

    cartas_validas = []
    for c in mao_computador:
        # Só aplica a restrição ao Ás do trunfo
        if c.value == 11 and c.category == trunfo.category:
            # Verifica se o 7 ainda está em jogo
            sete_em_jogo = any(x.value == 10 and x.category == trunfo.category
                               for x in mao_jogador + mao_computador + baralho)
            
            # Se o 7 ainda está em jogo, bloqueia o Ás (desde que tenha outras opções)
            if sete_em_jogo:
                continue  

        cartas_validas.append(c)

    # Se nenhuma carta foi adicionada (ex: só sobrou o Ás do trunfo), libera ele
    if not cartas_validas:
        return mao_computador  

    return cartas_validas




# 3. Criação dos objetos( 24 cartas)
        #Targon (8 cartas) como se fosse o nípe copas na bisca por exemplo, ai no nipe copas tem as cartas de copas
solvix = Card("Ás Solvix", "Targon", 11, "Algoritmo Instituinte", "imagens/cartas/solvix.png") #como se fosse o ás na bisca
guardiao_da_ordem = Card("Dezguardião da ordem", "Targon", 10, "", "imagens/cartas/guardiaoordem.png")    # como se fosse o 7 na bisca
rei_slugpantheon = Card("Rei Slugpantheon", "Targon", 4, "", "imagens/cartas/reislugpantheon.png")        # rei
valete_slugleona = Card("Valete Slugleona", "Targon", 3, "", "imagens/cartas/valeteslugleona.png")  # valete
dama_slugdiana = Card("Dama SlugDiana","Targon", 2, "", "imagens/cartas/damaslugdiana.png")         #rainha
targon_veiculo_robotico = Card("Veiculo Robotico de Targon", "Targon", 0, "", "imagens/cartas/veiculotargon.png")  #as cartas que não vale nada na bisca
targon_unidade_hexteck = Card("Unidade Hexteck de Targon", "Targon", 0, "", "imagens/cartas/unidadetargon.png")
condutor_prismatico_targon = Card("Condutor Prismatico de Targon", "Targon", 0, "", "imagens/cartas/condutortargon.png")

        #Piltover(8 cartas) como se fosse outro nipe
caityslug = Card("Ás Caityslug", "Piltover", 11, "Disparo Calibrado", "imagens/cartas/caityslug.png")    #padrão de valores se repete para cada nipe
guardiao_da_tecnologia = Card("Dezguardião da Tecnologia", "Piltover", 10, "", "imagens/cartas/guardiaotecnologia.png")
rei_slugheimer = Card("Rei SlugHeimer", "Piltover", 4, "", "imagens/cartas/reislugheimer.png")
valete_caveiraslug = Card("Valete Caveiraslug", "Piltover", 3, "", "imagens/cartas/valetecaveiraslug.png" )
dama_slugjinx = Card("Dama SlugJinx","Piltover", 2, "", "imagens/cartas/damaslugjinx.png")
piltover_veiculo_robotico = Card("Veiculo Robotico de Piltover", "Piltover", 0, "", "imagens/cartas/veiculopiltover.png")
piltover_unidade_hexteck = Card("Unidade Hexteck de Piltover", "Piltover", 0, "", "imagens/cartas/unidadepiltover.png")
condutor_prismatico_piltover = Card("Condutor Prismatico de Piltover", "Piltover", 0, "", "imagens/cartas/condutorpiltover.png")

        #Zaun (8 cartas) representa outro nipe
samira = Card("Ás Samira", "Zaun", 11, "Estilo Desafiador", "imagens/cartas/samira.png")    #padrão  se repete para cada nipe
guardiao_da_mutacao = Card("Dezguardião da Mutação", "Zaun", 10, "", "imagens/cartas/guardiaomutacao.png")
rei_slugsinged = Card("Rei SlugSinged", "Zaun", 4, "", "imagens/cartas/reislugsinged.png")
valete_slugekko = Card("Valete SlugEkko", "Zaun", 3, "", "imagens/cartas/valeteslugekko.png")
dama_slugcamille = Card("Dama SlugCamille","Zaun", 2, "", "imagens/cartas/damaslugcamille.png")
zaun_veiculo_robotico = Card("Veiculo Robotico de Zaun", "Zaun", 0, "", "imagens/cartas/veiculozaun.png")
zaun_unidade_hexteck = Card("Unidade Hexteck de Zaun", "Zaun", 0, "", "imagens/cartas/unidadezaun.png")
condutor_prismatico_zaun = Card("Condutor prismatico de Zaun", "Zaun", 0, "", "imagens/cartas/condutorzaun.png")
 
# Ultilizando lista para orgazinar todas as cartas em um unico local, uma lista é como uma gaveta que guarda varios itens,
#facilita manipulação
baralho = [
    solvix, guardiao_da_ordem, rei_slugpantheon, valete_slugleona, dama_slugdiana,
    targon_veiculo_robotico, targon_unidade_hexteck, condutor_prismatico_targon,

    caityslug, guardiao_da_tecnologia, rei_slugheimer, valete_caveiraslug, dama_slugjinx,
    piltover_veiculo_robotico, piltover_unidade_hexteck, condutor_prismatico_piltover,

    samira, guardiao_da_mutacao, rei_slugsinged, valete_slugekko ,dama_slugcamille,
    zaun_veiculo_robotico, zaun_unidade_hexteck, condutor_prismatico_zaun
]

# copia do baralho, que nunca será alterada:
baralho_completo = baralho[:]

print("Carregando imagens das cartas...")
for carta in baralho_completo:
    try:
        # Carrega a imagem e a guarda dentro do próprio objeto da carta
        carta.image = pygame.image.load(resource_path(carta.image_file)).convert_alpha()
    except pygame.error as e:
        print(f"ERRO: Não foi possível carregar a imagem '{carta.image_file}' - {e}")
        # Se der erro, cria uma superfície para o jogo não quebrar e você ver qual imagem faltou
        carta.image = pygame.Surface((100, 150)) 
        carta.image.fill((32, 178, 170))
print("Imagens carregadas.")


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
    print(f"- {carta.name} (Categoria:{carta.category} / Valor:{carta.value})")

print("\nMão do computador:")
for carta in mao_computador:
    print(f"- {carta.name} (Categoria:{carta.category} / Valor:{carta.value})") #f-string permite que voce use variavie diretamente dentro do texto

#loop para escolher uma carta aleatória para ser o trunfo e garantir que não seja de 10 ou 11 pontos
trunfo_carta = None #None significa --> essa variavel existe mas nao tem nada guardado nela ainda
while trunfo_carta is None or trunfo_carta.value >= 10:
    trunfo_carta = random.choice(baralho) # "continue executando enquanto o valor da carta for maior ou igual a 10, ou seja pare assim que encontrar um valor menor que 10, assim nunca vai ser um 10 ou um 11"
#print(trunfo_carta.name)

#remove a carta da sua posição atual no baralho
baralho.remove(trunfo_carta)

#coloca a carta do trunfo no final do bralho
baralho.append(trunfo_carta)

#define a categoria do trunfo e imprime
trunfo = trunfo_carta
print(f"O Trunfo da partida é a categoria: {trunfo.category}")
print(f"A carta do Trunfo é: {trunfo.name}")
print(f"O valor do Trunfo é: {trunfo.value}")




# CRIANDO O PLACAR ANTES DO JOGO COMEÇAR 
score_jogador = 0
score_computador = 0

#criando o fundo
FUNDO_VIXTERRA = "imagens/background/vixterra_iniciar.png"

try:
    fundo_img = pygame.image.load(resource_path(FUNDO_VIXTERRA)).convert()
    #garante que a imagem tenho o mesmo tamanho da tela
    fundo_img = pygame.transform.scale(fundo_img,(LARGURA, ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem de fundo: {FUNDO_VIXTERRA}")
    #se der erro, cria um  fundo  para o jogo não quebrar
    fundo_img = pygame.Surface((LARGURA, ALTURA))
    fundo_img.fill((0, 0,0))

# --- CONFIGURAÇÃO DA TELA INICIAL COM FUNDO ANIMADO E LOGO ---

LOGO_PNG = "imagens/words/nome_vixterra.png"  # nome do arquivo da logo

# Carrega fundo 
try:
    fundo_img = pygame.image.load(resource_path(FUNDO_VIXTERRA)).convert()
    fundo_img = pygame.transform.scale(fundo_img, (1400, ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem de fundo: {FUNDO_VIXTERRA}")
    fundo_img = pygame.Surface((LARGURA, ALTURA))
    fundo_img.fill((0, 0, 0))


#Carregar a imagem do verso da carta ###
try:
    verso_carta_img = pygame.image.load(resource_path("imagens/cartas/verso_carta.png")).convert_alpha()
except pygame.error as e:
    print(f"Erro ao carregar o verso da carta: {e}")
    # Cria uma superfície preta se a imagem não for encontrada
    verso_carta_img = pygame.Surface((100, 150))
    verso_carta_img.fill((10, 10, 10))

### Carregar fundos da tela de jogo ###
try:
    fundo_jogo_targon = pygame.transform.scale(pygame.image.load(resource_path("imagens/background/campo_targon.png")).convert(), (LARGURA, ALTURA))
    fundo_jogo_zaun = pygame.transform.scale(pygame.image.load(resource_path("imagens/background/campo_zaun.png")).convert(), (LARGURA, ALTURA))
    fundo_jogo_piltover = pygame.transform.scale(pygame.image.load(resource_path("imagens/background/campo_piltover.png")).convert(), (LARGURA, ALTURA))
except pygame.error as e:
    print(f"Erro ao carregar fundos de jogo: {e}")
    # Se der erro, usa o fundo padrão
    fundo_jogo_targon = fundo_img
    fundo_jogo_zaun = fundo_img
    fundo_jogo_piltover = fundo_img

# Carrega logo com canal alpha (transparência)
try:
    logo = pygame.image.load(resource_path(LOGO_PNG)).convert_alpha()
    # opções de escala: deixa a logo proporcional ao tamanho da tela (ex: 30% da largura)
    logo_largura = int(LARGURA * 0.40)
    logo_altura = int(logo.get_height() * (logo_largura / logo.get_width())) #calcula a altura proporcional para não deformar a imagem
    logo = pygame.transform.smoothscale(logo, (logo_largura, logo_altura)) 
except pygame.error:
    print(f"Não foi possivel carregar a logo: {LOGO_PNG}")
    logo = None

# Para scroll horizontal contínuo do fundo: vamos desenhar duas cópias lado a lado
bg_x1 = 0
bg_x2 = 2048 #largura real da imagem
scroll_speed = 20  # pixels por segundo (ajusta para ficar mais rápido/lento)

# Parâmetros da splash
SPLASH_DURATION = 3000  # ms (duração total da splash)
FADE_IN_DURATION = 900  # ms (duração do fade-in da logo)
clock = pygame.time.Clock()
splash_start = pygame.time.get_ticks()

# Loop da splash (antes do loop principal do jogo)
# --- TELA INICIAL (SPLASH) ---
# --- TELA INICIAL (SPLASH) ---
splash_rodando = True
MAX_SCROLL = 200       # pixels que o fundo vai se mover antes de congelar
scroll_total = 0       # deslocamento acumulado
splash_congelada = False

# temporizador para congelar o fundo após alguns segundos
tempo_splash = 0       # tempo acumulado em ms
TEMPO_SCROLL = 2000    # tempo que o fundo vai rolar antes de congelar (2 segundos)

splash_start = pygame.time.get_ticks()  # marca início da splash



# Ao sair da splash, segue normalmente para o loop principal do jogo...
# --- TELA DE MENU PRINCIPAL ---
MENU_PRINCIPAL_IMG = "imagens/background/menu_vixterra.png"
try:
    menu_principal = pygame.image.load(resource_path(MENU_PRINCIPAL_IMG)).convert()
    menu_principal = pygame.transform.scale(menu_principal, (LARGURA, ALTURA))
except pygame.error:
    print(f"Não foi possível carregar a imagem: {MENU_PRINCIPAL_IMG}")
    menu_principal = pygame.Surface((LARGURA, ALTURA))
    menu_principal.fill((50, 50, 50))  # fundo cinza se der erro

### CARREGANDO FUNDO DA TELA DE CARTAS ###
TELA_CARTAS_FUNDO_IMG = "imagens/background/fundo_cartas_vixterra.png"
try:
    fundo_tela_cartas = pygame.image.load(resource_path(TELA_CARTAS_FUNDO_IMG)).convert()
    fundo_tela_cartas = pygame.transform.scale(fundo_tela_cartas, (LARGURA,ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem: {TELA_CARTAS_FUNDO_IMG}")
    fundo_tela_cartas = pygame.Surface((LARGURA, ALTURA))
    fundo_tela_cartas.fill((20, 0, 30)) #um fundo roxo escuro caso a imagem nao carregue

# --- MENU INTERATIVO ---
menu_ativo = True  # variável de controle para manter o menu ativo

# Criar retângulos para botões interativos
botao_voltar_rect = pygame.Rect(15, ALTURA - 35 - 10, 100, 30)


# --- BOTÕES CENTRALIZADOS ---

# dimensões dos botões uma vez
largura_botoes_menu = 200
altura_botoes_menu = 50

#  posição X que centraliza os botões na tela
x_central_botoes = LARGURA // 2 - (largura_botoes_menu // 2)

#  retângulos usando as posições calculadas
# O botão "Jogar" ficará a 70% da altura da tela
botao_jogar_rect = pygame.Rect(x_central_botoes, int(ALTURA * 0.70), largura_botoes_menu, altura_botoes_menu)

# O botão "Cartas" ficará a 85% da altura da tela, logo abaixo do "Jogar"
aba_cartas_rect = pygame.Rect(x_central_botoes, int(ALTURA * 0.85), largura_botoes_menu, altura_botoes_menu)
#Botões de Categoria ###
largura_botao_cat = 150
altura_botao_cat = 40
espaco_botoes_cat = 20
y_botoes_cat = 20 # Altura dos botões na tela
largura_total_botoes = (3 * largura_botao_cat) + (2 * espaco_botoes_cat)
x_inicial_botoes = (LARGURA - largura_total_botoes) / 2

botao_targon_rect = pygame.Rect(x_inicial_botoes, y_botoes_cat, largura_botao_cat, altura_botao_cat)
botao_zaun_rect = pygame.Rect(x_inicial_botoes + largura_botao_cat + espaco_botoes_cat, y_botoes_cat, largura_botao_cat, altura_botao_cat)
botao_piltover_rect = pygame.Rect(x_inicial_botoes + 2 * (largura_botao_cat + espaco_botoes_cat), y_botoes_cat, largura_botao_cat, altura_botao_cat)

# fonte para os textos dos botões
fonte = pygame.font.SysFont(None, 28)
fonte_titulo = pygame.font.SysFont("Palatino Linotype", 26, bold=True)
fonte_peq = pygame.font.SysFont(None, 20)
fonte_anuncio = pygame.font.SysFont("Palatino Linotype", 60, bold=True)    


#Decidindo quem joga primeiro na rodada 
vez_do_jogador =random.choice(["jogador", "computador"])
# Define o texto de status inicial (para a primeira rodada)
if vez_do_jogador == "jogador":
    status_texto = "Sua Vez de Jogar! Escolha uma carta!"
else:
    status_texto = "Vez do Computador!"

# iniciar contagem de rodadas
numero_da_rodada = 1



# Loop que vai manter a janela aberta e funcionando:
jogo_ativo = False
rodando = True
tela_cartas_ativa = False
categoria_visivel = "Targon" #começar mostrando targon

#novas variaveis
fase_da_rodada = "ANUNCIO"  # Controla o fluxo da rodada
carta_jogada_jogador = None
carta_jogada_computador = None
vencedor_da_rodada = None
tempo_resolucao = 0
cartas_retangulos = [] #lista de retangulos da mao do jogador
fonte_anuncio = pygame.font.SysFont("Palatino Linotype", 48, bold=True)

aviso_texto = "" # Guarda a mensagem de aviso
aviso_timer = 0  # Guarda por quanto tempo (em ms) o aviso deve aparecer

status_texto = "" # Guarda a mensagem de status da rodada
jogo_finalizado = False       # Nova flag para dizer "o jogo acabou, mostre a mensagem"
mensagem_fim_jogo = ""      # Guarda o texto "VOCÊ VENCEU!" ou "VOCÊ PERDEU!"
tempo_fim_jogo = 0
while rodando: 
    dt = clock.tick(60)

    # 1. TRATAMENTO DE EVENTOS UNIFICADO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        # --- EVENTOS DA SPLASH ---
        if splash_rodando:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and splash_congelada:
                    splash_rodando = False
                    menu_ativo = True
                    
        # --- EVENTOS DO MENU ---
        elif menu_ativo:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Botão "Voltar" (volta para Splash)
                if botao_voltar_rect.collidepoint(evento.pos): 
                    menu_ativo = False
                    splash_rodando = True
                    # Reset das variáveis da Splash:
                    tempo_splash = 0
                    splash_congelada = False
                    splash_start = pygame.time.get_ticks() 
                    scroll_total = 0
                
                # Botão "Jogar" (vai para o Jogo)
                elif botao_jogar_rect.collidepoint(evento.pos):
                    print("--- RESETANDO PARA UM NOVO JOGO ---")

                    # 1. Reseta o baralho (pega a cópia completa e embaralha)
                    baralho = baralho_completo[:] 
                    random.shuffle(baralho)

                    # 2. Reseta as mãos (distribui 3 novas cartas)
                    mao_jogador = [] 
                    mao_computador = []
                    for _ in range(3):
                        mao_jogador.append(baralho.pop(0))
                        mao_computador.append(baralho.pop(0))

                    # 3. Reseta o Trunfo (escolhe um novo)
                    trunfo_carta = None
                    while trunfo_carta is None or trunfo_carta.value >= 10:
                        trunfo_carta = random.choice(baralho)
                    
                    baralho.remove(trunfo_carta)
                    baralho.append(trunfo_carta)
                    trunfo = trunfo_carta
                    print(f"O NOVO Trunfo é: {trunfo.category}")

                    # 4. Reseta o Placar
                    score_jogador = 0
                    score_computador = 0

                    # 5. Reseta as Variáveis de Estado da Partida
                    dez_trunfo_jogado = False
                    vez_do_jogador = random.choice(["jogador", "computador"])
                    numero_da_rodada = 1
                    fase_da_rodada = "ANUNCIO"
                    carta_jogada_jogador = None
                    carta_jogada_computador = None
                    vencedor_da_rodada = None
                    tempo_resolucao = 0
                    cartas_retangulos = []
                    aviso_texto = ""
                    aviso_timer = 0
                    status_texto = ""
                
                    jogo_ativo = True
                    menu_ativo = False

                    

                # Botão "Cartas"
                elif aba_cartas_rect.collidepoint(evento.pos):
                    #print("Abrir tela das cartas")
                    menu_ativo = False
                    tela_cartas_ativa = True 
                
        elif tela_cartas_ativa:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Verifica se o clique foi no mesmo retângulo do botão "Voltar"
                if botao_voltar_rect.collidepoint(evento.pos):
                    tela_cartas_ativa = False # Desliga a tela de cartas
                    menu_ativo = True         # Liga o menu novamente
                    
                ##Lógica de clique para os botões de categoria ###
                elif botao_targon_rect.collidepoint(evento.pos):
                    categoria_visivel = "Targon"
                elif botao_zaun_rect.collidepoint(evento.pos):
                    categoria_visivel = "Zaun"
                elif botao_piltover_rect.collidepoint(evento.pos):
                    categoria_visivel = "Piltover"
        elif jogo_ativo:
            # Só processa cliques se for a fase de jogada E for a vez do jogador
            if fase_da_rodada == "JOGADA" and vez_do_jogador == "jogador":
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    pos = evento.pos # posição do clique do mouse

                    # verifica qual carta foi clicada
                    for idx, rect in enumerate(cartas_retangulos):
                        if rect.collidepoint(pos):
                            
                            # Pega a carta que foi clicada
                            carta_escolhida = mao_jogador[idx]

                            # --- lógica do Ás do trunfo ---
                            if carta_escolhida.value == 11 and carta_escolhida.category == trunfo.category:
                                if len(mao_jogador) > 1:
                                    # Verifica se o 10 do trunfo AINDA está em jogo (na mão de alguém ou no baralho)
                                    # (Corrigi a lógica para checar a carta "10" e não a "7")
                                    dez_em_jogo = any(c.value == 10 and c.category == trunfo.category
                                                      for c in mao_jogador + mao_computador + baralho)
                                    
                                    if dez_em_jogo:
                                        #print("Atenção: o Ás do trunfo não pode ser jogado enquanto o 10 estiver em jogo!")
                                        aviso_texto = "Atenção: O Ás do Trunfo só pode ser jogado após o 10 do trunfo!"
                                        aviso_timer = 3000 # Mostra o aviso por 3 segundos (3000 ms)
                                        # Não faz nada, espera outro clique
                                        break # Sai do loop "for idx, rect..."
                            
                            # Se passou na regra, joga a carta
                            print(f"Você jogou: {carta_escolhida.name}")
                            
                            # Atualiza a flag do 10 do trunfo (NOVO, estava faltando aqui!)
                            if carta_escolhida.value == 10 and carta_escolhida.category == trunfo.category:
                                dez_trunfo_jogado = True
                                
                            carta_jogada_jogador = mao_jogador.pop(idx) # Tira da mão e coloca na "mesa"
                            
                            # Se o jogador estava esperando o PC, agora os dois jogaram
                            if carta_jogada_computador is not None:
                                fase_da_rodada = "RESOLUCAO"
                            # Se o jogador foi o primeiro, muda a vez
                            else:
                                vez_do_jogador = "computador"
                            
                            break # Sai do loop "for idx, rect..."
                

    # 2. LÓGICA DE ATUALIZAÇÃO E DESENHO
    
    # --- ESTADO A: SPLASH SCREEN (TELA INICIAL) ---
    if splash_rodando:
        tempo_splash += dt 

        # Lógica de Scroll
        if not splash_congelada:
            desloc = scroll_speed * (dt / 1000.0)
            scroll_total += desloc
            if tempo_splash >= TEMPO_SCROLL:
                splash_congelada = True
                scroll_total = min(scroll_total, MAX_SCROLL)

        # Desenho
        tela.blit(fundo_img, (-scroll_total, 0))

        if logo:
            agora = pygame.time.get_ticks()
            elapsed = agora - splash_start
            alpha = int(255 * (elapsed / FADE_IN_DURATION)) if elapsed < FADE_IN_DURATION else 255
            logo_surf = logo.copy(); logo_surf.set_alpha(alpha)
            logo_x = (LARGURA - logo.get_width()) // 2
            logo_y = int(ALTURA * 0.08)
            tela.blit(logo_surf, (logo_x, logo_y))

        agora = pygame.time.get_ticks()
        if (agora // 1200) % 2 == 0:
            sombra = fonte.render("Pressione ESPAÇO para continuar!", True, (0,0,0))
            tx = (LARGURA - sombra.get_width()) // 2
            ty = int(ALTURA * 0.85)
            tela.blit(sombra, (tx+1, ty+1))
            texto = fonte.render("Pressione ESPAÇO para continuar!", True, (255,255,255))
            tela.blit(texto, (tx, ty))

        pygame.display.flip()
        
    
    # --- ESTADO B: MENU PRINCIPAL ---
    elif menu_ativo:
        
        # Desenho
        tela.blit(menu_principal, (0, 0))
        
        frase = "Boas vindas a Vixterra! Duele pelo domínio da energia prismática." # <-- ESCOLHA SUA FRASE PREFERIDA AQUI
        
        # Renderiza a sombra
        sombra_surf = fonte_titulo.render(frase, True, (0, 0, 0))
        sombra_rect = sombra_surf.get_rect(center=(LARGURA // 2 + 2, 42)) # Posição da sombra (deslocada)
        tela.blit(sombra_surf, sombra_rect)

        # Renderiza o texto principal
        texto_surf = fonte_titulo.render(frase, True, (230, 230, 255)) # Cor de lavanda/branco
        texto_rect = texto_surf.get_rect(center=(LARGURA // 2, 40)) # Posição do texto
        tela.blit(texto_surf, texto_rect)

        pygame.draw.rect(tela, (0,255, 255), botao_voltar_rect) 
        texto_voltar = fonte.render("Voltar", True, (255, 255, 255))
        tx = botao_voltar_rect.x + (botao_voltar_rect.width - texto_voltar.get_width()) // 2
        ty = botao_voltar_rect.y + (botao_voltar_rect.height - texto_voltar.get_height()) // 2
        tela.blit(texto_voltar, (tx, ty))

        pygame.draw.rect(tela, (0, 100, 200), aba_cartas_rect) 
        texto_aba = fonte.render("Cartas", True, (255, 255, 255))
        tx = aba_cartas_rect.x + (aba_cartas_rect.width - texto_aba.get_width()) // 2
        ty = aba_cartas_rect.y + (aba_cartas_rect.height - texto_aba.get_height()) // 2
        tela.blit(texto_aba, (tx, ty))

        pygame.draw.rect(tela, (0, 200, 0), botao_jogar_rect)
        texto_jogar = fonte.render("Jogar", True, (255, 255, 255))
        tx = botao_jogar_rect.x + (botao_jogar_rect.width - texto_jogar.get_width()) // 2
        ty = botao_jogar_rect.y + (botao_jogar_rect.height - texto_jogar.get_height()) // 2
        tela.blit(texto_jogar, (tx, ty))

        pygame.display.flip()


        # --- NOVO ESTADO: TELA DE CARTAS (VERSÃO COM BOTÕES E CORREÇÃO) ---
    elif tela_cartas_ativa:
        # 1. Desenha o fundo e o botão Voltar
        tela.blit(fundo_tela_cartas, (0, 0))
        pygame.draw.rect(tela, (0, 255, 255), botao_voltar_rect)
        texto_voltar = fonte.render("Voltar", True, (0, 0, 0))
        tx = botao_voltar_rect.x + (botao_voltar_rect.width - texto_voltar.get_width()) // 2
        ty = botao_voltar_rect.y + (botao_voltar_rect.height - texto_voltar.get_height()) // 2
        tela.blit(texto_voltar, (tx, ty))

        # 2. Desenha os botões de categoria (Targon, Zaun, Piltover)
        cor_ativa = (255, 215, 0) # Dourado
        cor_inativa = (0, 100, 200) # Azul escuro

        cor_targon = cor_ativa if categoria_visivel == "Targon" else cor_inativa
        pygame.draw.rect(tela, cor_targon, botao_targon_rect, border_radius=8)
        texto_targon = fonte.render("Targon", True, (255, 255, 255))
        tela.blit(texto_targon, texto_targon.get_rect(center=botao_targon_rect.center))

        cor_zaun = cor_ativa if categoria_visivel == "Zaun" else cor_inativa
        pygame.draw.rect(tela, cor_zaun, botao_zaun_rect, border_radius=8)
        texto_zaun = fonte.render("Zaun", True, (255, 255, 255))
        tela.blit(texto_zaun, texto_zaun.get_rect(center=botao_zaun_rect.center))
        
        cor_piltover = cor_ativa if categoria_visivel == "Piltover" else cor_inativa
        pygame.draw.rect(tela, cor_piltover, botao_piltover_rect, border_radius=8)
        texto_piltover = fonte.render("Piltover", True, (255, 255, 255))
        tela.blit(texto_piltover, texto_piltover.get_rect(center=botao_piltover_rect.center))

        # 3. Filtra as cartas e seleciona qual lista desenhar
        cartas_targon = [c for c in baralho_completo if c.category == "Targon"]
        cartas_zaun = [c for c in baralho_completo if c.category == "Zaun"]
        cartas_piltover = [c for c in baralho_completo if c.category == "Piltover"]
        
        cartas_para_desenhar = []
        if categoria_visivel == "Targon":
            cartas_para_desenhar = cartas_targon
        elif categoria_visivel == "Zaun":
            cartas_para_desenhar = cartas_zaun
        elif categoria_visivel == "Piltover":
            cartas_para_desenhar = cartas_piltover
        
        # 4. Nova configuração da grade (2x4, para cartas bem maiores)
        margem_x = 40
        margem_y_inicial = 90
        espacamento_h = 30
        espaco_entre_linhas = 30
        num_cartas_por_linha = 4
        
        # Cálculo de tamanho baseado na LARGURA
        card_larg = int((LARGURA - 2 * margem_x - (num_cartas_por_linha - 1) * espacamento_h) / num_cartas_por_linha)
        
        # 5. Desenha as 8 cartas da categoria selecionada
        # Verifica se a lista não está vazia para evitar erros
        if cartas_para_desenhar:
            for i, carta in enumerate(cartas_para_desenhar):
                # Calcula a coluna (0 a 3) e a linha (0 ou 1)
                coluna = i % num_cartas_por_linha
                linha = i // num_cartas_por_linha
                
                
                # PRIMEIRO: Calcula a altura correta mantendo a proporção da arte
                original_larg, original_alt = carta.image.get_size()
                card_alt_calculado = int(original_alt * (card_larg / original_larg))

                # SEGUNDO: Usa a altura calculada para definir a posição Y
                posicao_x = margem_x + coluna * (card_larg + espacamento_h)
                posicao_y = margem_y_inicial + linha * (card_alt_calculado + espaco_entre_linhas)

                # TERCEIRO: Redimensiona e desenha a imagem
                imagem_redimensionada = pygame.transform.smoothscale(carta.image, (card_larg, card_alt_calculado))
                tela.blit(imagem_redimensionada, (posicao_x, posicao_y))

        # Atualiza a tela para mostrar tudo
        pygame.display.flip()
        # --- ESTADO C: JOGO ATIVO ---
    # --- ESTADO C: JOGO ATIVO ---
    elif jogo_ativo:
        
        # ==========================================================
        # 1. PARTE DE DESENHO (Acontece todo frame)
        # ==========================================================
        
        # 1.1. Desenha o Fundo
        fundo_atual_jogo = fundo_img
        if trunfo.category == "Targon": fundo_atual_jogo = fundo_jogo_targon
        elif trunfo.category == "Zaun": fundo_atual_jogo = fundo_jogo_zaun
        elif trunfo.category == "Piltover": fundo_atual_jogo = fundo_jogo_piltover
        tela.blit(fundo_atual_jogo, (0, 0))
        
        # 1.2. Desenha o Placar (NOVO!)
        sombra_placar = fonte_titulo.render(f"Jogador: {score_jogador}", True, (0,0,0))
        texto_placar = fonte_titulo.render(f"Jogador: {score_jogador}", True, (255,255,255))
        tela.blit(sombra_placar, (22, 22))
        tela.blit(texto_placar, (20, 20))
        
        sombra_placar_cpu = fonte_titulo.render(f"Computador: {score_computador}", True, (0,0,0))
        texto_placar_cpu = fonte_titulo.render(f"Computador: {score_computador}", True, (255,255,255))
        tela.blit(sombra_placar_cpu, (22, 52))
        tela.blit(texto_placar_cpu, (20, 50))

        # 1.3. Desenha a Pilha de Cartas
        # (Seu código original, estava ótimo)
        larg_pilha = 100
        alt_pilha = int(larg_pilha * (verso_carta_img.get_height() / verso_carta_img.get_width()))
        verso_pilha_redimensionado = pygame.transform.smoothscale(verso_carta_img, (larg_pilha, alt_pilha))
        deck_pos = (LARGURA - larg_pilha - 30, 30)
        if len(baralho) > 2: tela.blit(verso_pilha_redimensionado, (deck_pos[0] + 8, deck_pos[1] + 8))
        if len(baralho) > 1: tela.blit(verso_pilha_redimensionado, (deck_pos[0] + 4, deck_pos[1] + 4))
        if len(baralho) > 0:
            tela.blit(verso_pilha_redimensionado, deck_pos)
            texto_baralho = fonte.render(f"{len(baralho)}", True, (255, 255, 255))
            texto_rect = texto_baralho.get_rect(center=(deck_pos[0] + larg_pilha / 2, deck_pos[1] + alt_pilha + 15))
            tela.blit(texto_baralho, texto_rect)

        # 1.4. Desenha a Mão do Computador (Verso)
        if mao_computador:
            larg_card_cpu = 150
            espaco_entre_cartas_cpu = 15
            original_verso_larg, original_verso_alt = verso_carta_img.get_size()
            alt_card_cpu = int(original_verso_alt * (larg_card_cpu / original_verso_larg))
            verso_redimensionado_cpu = pygame.transform.smoothscale(verso_carta_img, (larg_card_cpu, alt_card_cpu))
            num_cartas_cpu = len(mao_computador)
            largura_total_cpu = (num_cartas_cpu * larg_card_cpu) + ((num_cartas_cpu - 1) * espaco_entre_cartas_cpu)
            x_inicial_cpu = (LARGURA - largura_total_cpu) / 2
            y_cartas_cpu = 5 #pixels a partir do topo da tela
            for i in range(num_cartas_cpu):
                x = x_inicial_cpu + i * (larg_card_cpu + espaco_entre_cartas_cpu)
                tela.blit(verso_redimensionado_cpu, (x, y_cartas_cpu))
        # 1.3.1. Desenha a CARTA DE TRUNFO 
        
        # Só desenha se a carta ainda não foi comprada
        if len(baralho) > 0:
        
            # --- 1. CONFIGURAÇÃO DE TEXTO ---
            categoria_trunfo = trunfo.category.upper()
            texto_str = f"TRUNFO: {categoria_trunfo}"
            
            sombra_trunfo_txt = fonte_peq.render(texto_str, True, (0,0,0))
            texto_trunfo_txt = fonte_peq.render(texto_str, True, (255, 215, 0))
            
            # Pega o retângulo do texto para facilitar o posicionamento
            texto_rect = texto_trunfo_txt.get_rect()
            sombra_rect = sombra_trunfo_txt.get_rect()
            
            # --- 2. CONFIGURAÇÃO DA CARTA ---
            larg_trunfo_display = 220
            
            img_trunfo = trunfo.image
            original_larg, original_alt = img_trunfo.get_size()
            alt_trunfo_display = int(original_alt * (larg_trunfo_display / original_larg))
            
            img_trunfo_redim = pygame.transform.smoothscale(img_trunfo, (larg_trunfo_display, alt_trunfo_display))
            
            # --- 3. CÁLCULO DE POSIÇÃO ---
            
            # Centro horizontal da área
            centro_da_pilha_x = deck_pos[0] + (larg_pilha / 2)
            
            # Posição Y do TEXTO (Abaixo da pilha)
            pos_y_bloco_texto = deck_pos[1] + alt_pilha + 65
            
            # Centraliza o retângulo do texto
            texto_rect.center = (centro_da_pilha_x, pos_y_bloco_texto + (texto_rect.height / 2))
            sombra_rect.center = (texto_rect.centerx + 1, texto_rect.centery + 1)
            
            #  Cria o retângulo marrom de fundo 
            rect_fundo_marrom = texto_rect.inflate(10, 6)
            COR_MARROM = (101, 67, 33) # Um tom de marrom escuro
            
            # Posição Y da CARTA (Abaixo do retângulo marrom)
            pos_y_carta = rect_fundo_marrom.bottom + 10  # 10 pixels abaixo do fundo
            pos_x_carta = centro_da_pilha_x - (larg_trunfo_display / 2)
            
            # --- 4. DESENHAR ---
            
            # 1. Desenha o fundo marrom
            pygame.draw.rect(tela, COR_MARROM, rect_fundo_marrom, border_radius=4)
            
            # 2. Desenha a sombra do texto
            tela.blit(sombra_trunfo_txt, sombra_rect)
            
            # 3. Desenha o texto principal
            tela.blit(texto_trunfo_txt, texto_rect)
            
            # 4. Desenha a carta de trunfo
            tela.blit(img_trunfo_redim, (pos_x_carta, pos_y_carta))

        # 1.5. Desenha a Mão do Jogador (Frente)
        cartas_retangulos = [] # Limpa os retângulos para recalcular
        num_cartas_mao = len(mao_jogador)
        if num_cartas_mao > 0:
            # (Seu código original para calcular o tamanho da mão)
            max_largura_mao_pct = 0.60
            espaco_entre_cartas_mao = 25
            margem_inferior = 5
            MAX_CARTAS_NA_MAO = 3
            largura_total_disponivel = LARGURA * max_largura_mao_pct
            largura_total_espacos_fixo = espaco_entre_cartas_mao * (MAX_CARTAS_NA_MAO - 1)
            larg_card_mao = int((largura_total_disponivel - largura_total_espacos_fixo) / MAX_CARTAS_NA_MAO)
            largura_total_espacos = espaco_entre_cartas_mao * (num_cartas_mao - 1)
            
            primeira_carta_mao = mao_jogador[0]
            original_larg, original_alt = primeira_carta_mao.image.get_size()
            alt_card_mao = int(original_alt * (larg_card_mao / original_larg))
            
            y_cartas_mao = ALTURA - alt_card_mao - margem_inferior
            largura_real_mao = (num_cartas_mao * larg_card_mao) + largura_total_espacos
            x_inicial_mao = (LARGURA - largura_real_mao) / 2

            for idx, carta in enumerate(mao_jogador):
                x = x_inicial_mao + idx * (larg_card_mao + espaco_entre_cartas_mao)
                rect = pygame.Rect(x, y_cartas_mao, larg_card_mao, alt_card_mao)
                cartas_retangulos.append(rect) # Salva o retângulo para o clique
                
                imagem_redimensionada = pygame.transform.smoothscale(carta.image, (larg_card_mao, alt_card_mao))
                tela.blit(imagem_redimensionada, rect.topleft)
        
        #1.5.1. DESENHA AVISO DE JOGADA ILEGAL
        if aviso_timer > 0:
            # Usa a fonte pequena para o aviso
            aviso_surf = fonte_peq.render(aviso_texto, True, (255, 255, 255)) # Texto branco
            
            # Posição: Centralizado, um pouco acima da sua mão
            aviso_x = (LARGURA - aviso_surf.get_width()) / 2
            aviso_y = ALTURA - alt_card_mao - 40 # pixels acima da mão
            
            # Desenha um fundo escuro (vermelho) para o aviso
            fundo_rect = aviso_surf.get_rect(center=(LARGURA / 2, aviso_y + 10))
            fundo_rect.inflate_ip(20, 10) # Aumenta o retângulo (padding)
            pygame.draw.rect(tela, (150, 0, 0), fundo_rect, border_radius=5) # Fundo vermelho escuro
            
            # Desenha o texto
            tela.blit(aviso_surf, (aviso_x, aviso_y))
            

        # 1.6. Desenha as Cartas na "Mesa" 
        larg_carta_mesa = 240 # Tamanho de destaque
        alt_carta_mesa = 0
        
        # Posições
        y_mesa = (ALTURA - 300) / 2 - 50# Posição Y (estimada, ajuste se precisar)
        x_jogador_mesa = LARGURA / 2 - larg_carta_mesa - 15 -5
        x_cpu_mesa = LARGURA / 2 + 15 +5

        if carta_jogada_jogador:
            # Calcula a altura correta (só na primeira vez)
            if alt_carta_mesa == 0:
                original_larg, original_alt = carta_jogada_jogador.image.get_size()
                alt_carta_mesa = int(original_alt * (larg_carta_mesa / original_larg))
                y_mesa = (ALTURA - alt_carta_mesa) / 2 -  50 # Recalcula Y com altura real
            
            img_jog_mesa = pygame.transform.smoothscale(carta_jogada_jogador.image, (larg_carta_mesa, alt_carta_mesa))
            tela.blit(img_jog_mesa, (x_jogador_mesa, y_mesa))

        if carta_jogada_computador:
            # Calcula a altura correta (só na primeira vez)
            if alt_carta_mesa == 0:
                original_larg, original_alt = carta_jogada_computador.image.get_size()
                alt_carta_mesa = int(original_alt * (larg_carta_mesa / original_larg))
                y_mesa = (ALTURA - alt_carta_mesa) / 2 -50# Recalcula Y com altura real
            
            img_cpu_mesa = pygame.transform.smoothscale(carta_jogada_computador.image, (larg_carta_mesa, alt_carta_mesa))
            tela.blit(img_cpu_mesa, (x_cpu_mesa, y_mesa))


        # ==========================================================
        # 2. LÓGICA DE JOGO (Máquina de Estados)
        # ==========================================================

       # FASE 1: ANÚNCIO 
        if fase_da_rodada == "ANUNCIO":
            
            # Define o texto
            if vez_do_jogador == "jogador":
                anuncio_txt = "Sua Vez de Jogar! Escolha uma carta!"
            else:
                anuncio_txt = "Vez do Computador!"
                
            sombra_anuncio = fonte_peq.render(anuncio_txt, True, (0,0,0))
            texto_anuncio = fonte_peq.render(anuncio_txt, True, (255, 255, 255)) 
            
            # Pega os retângulos do texto
            sombra_rect = sombra_anuncio.get_rect()
            texto_rect = texto_anuncio.get_rect()
            
            # Posição Y ajustada para ficar abaixo do score ---
            # O score do computador está em y=50. 
            pos_y_base = 100 # Da para ajustar conforme o espaçamento desejado
            sombra_rect.topleft = (22, pos_y_base + 1) # Posição X ajustada para ficar alinhado ao score
            texto_rect.topleft = (20, pos_y_base)      # Posição X ajustada para ficar alinhado ao score
            
            # ---  Retângulo Verde Escuro ---
            COR_VERDE_ESCURO = (0, 70, 0) # Um verde bem escuro
            rect_fundo_verde = texto_rect.inflate(20, 12) 

            # --- Ordem de Desenho Atualizada ---
            
            # 1. Desenha o fundo verde (com bordas arredondadas)
            pygame.draw.rect(tela, COR_VERDE_ESCURO, rect_fundo_verde, border_radius=8)
            
            # 2. Desenha a sombra do texto
            tela.blit(sombra_anuncio, sombra_rect)

            # 3. Desenha o texto principal (branco)
            tela.blit(texto_anuncio, texto_rect)

            # Lógica do timer 
            tempo_resolucao += dt 
            
            if tempo_resolucao > 1000: # anuncio de quem é a vez
                tempo_resolucao = 0
                fase_da_rodada = "JOGADA"
                
                print(f"\n --- Rodada {numero_da_rodada} ---")
                print(f"TRUNFO: {trunfo.category} (Carta: {trunfo.name})")
                numero_da_rodada += 1

        # FASE 2: JOGADA
        elif fase_da_rodada == "JOGADA":
            # Esta fase fica esperando a ação do jogador (no loop de eventos)
            # ou executa a jogada do computador.
            # --- Lógica do Timer de Aviso ---
            if aviso_timer > 0:
                aviso_timer -= dt # 'dt' é o tempo do frame
                if aviso_timer <= 0:
                    aviso_texto = "" # Limpa o texto quando o tempo acabar
            # Vez do Computador de jogar
            if vez_do_jogador == "computador" and carta_jogada_computador is None:
                
                # Atraso pequeno para o PC "pensar"
                pygame.time.wait(500) 
                
                print("\nVez do computador...")
                
                # --- LÓGICA DA IA  ---
                mao_computador_validas = filtrar_as_trunfo(mao_computador, mao_jogador, baralho, trunfo)
                
                # Se o PC JOGA PRIMEIRO
                if carta_jogada_jogador is None:
                    cartas_baixo_custo = [c for c in mao_computador_validas if 0 < c.value <= 3]
                    cartas_sem_valor = [c for c in mao_computador_validas if c.value == 0]
                    cartas_trunfo_validas = [c for c in mao_computador_validas if c.category == trunfo.category]
                    cartas_altas_nao_trunfo = [c for c in mao_computador_validas if c.value > 3 and c.category != trunfo.category]

                    if cartas_baixo_custo:
                        carta_jogada_computador = min(cartas_baixo_custo, key=lambda c: c.value)
                    elif cartas_sem_valor:
                        carta_jogada_computador = cartas_sem_valor[0]
                    elif cartas_trunfo_validas:
                        carta_jogada_computador = min(cartas_trunfo_validas, key=lambda c: c.value)
                    elif cartas_altas_nao_trunfo:
                        carta_jogada_computador = max(cartas_altas_nao_trunfo, key=lambda c: c.value)
                    else:
                        # Se só sobrou carta alta de trunfo (ex: Ás), joga
                        carta_jogada_computador = max(mao_computador_validas, key=lambda c: c.value)
                
                # Se o PC RESPONDE
                else:
                    if carta_jogada_jogador.value >= 10 and carta_jogada_jogador.category != trunfo.category:
                        trunfos_validos = [c for c in mao_computador_validas if c.category == trunfo.category]
                        if trunfos_validos:
                            carta_jogada_computador = min(trunfos_validos, key=lambda c: c.value)

                    if carta_jogada_computador is None:
                        cartas_mesmo_nipe = [c for c in mao_computador_validas if c.category == carta_jogada_jogador.category]
                        if cartas_mesmo_nipe:
                            cartas_maiores = [c for c in cartas_mesmo_nipe if c.value > carta_jogada_jogador.value]
                            if cartas_maiores:
                                carta_jogada_computador = min(cartas_maiores, key=lambda c: c.value)
                            else:
                                carta_jogada_computador = min(cartas_mesmo_nipe, key=lambda c: c.value)

                    if carta_jogada_computador is None:
                        cartas_trunfo_validas = [c for c in mao_computador_validas if c.category == trunfo.category]
                        if cartas_trunfo_validas:
                            carta_jogada_computador = min(cartas_trunfo_validas, key=lambda c: c.value)
                        else:
                            carta_jogada_computador = min(mao_computador_validas, key=lambda c: c.value)

                # --- Fim da Lógica da IA ---
                
                mao_computador.remove(carta_jogada_computador) # Remove da mão
                print(f"- O computador jogou: {carta_jogada_computador.name}")

                # Atualiza estado se for o 10 do trunfo
                if carta_jogada_computador.value == 10 and carta_jogada_computador.category == trunfo.category:
                    dez_trunfo_jogado = True
                
                # Se o PC estava esperando o jogador, agora os dois jogaram
                if carta_jogada_jogador is not None:
                    fase_da_rodada = "RESOLUCAO"
                # Se o PC foi o primeiro, passa a vez para o jogador
                else:
                    vez_do_jogador = "jogador"
            
            # Se for a vez do jogador, o loop de eventos (Passo 2) está cuidando disso

        # FASE 3: RESOLUÇÃO
        elif fase_da_rodada == "RESOLUCAO":
            # Ambas as cartas estão na mesa. Hora de calcular o vencedor.
            
            # Pausa para mostrar as cartas
            tempo_resolucao += dt
            if tempo_resolucao < 5000: # Pausa por 5 segundos
                # (Ainda esta desenhando, então o jogador vê as 2 cartas)
                pass # Continue esperando
            else:
                # LÓGICA DE DECISÃO (Revisada e corrigida)
                mesa = [carta_jogada_jogador, carta_jogada_computador]
                
                # Define o naipe da rodada (carta de quem começou)
                carta_inicial = None
                carta_resposta = None
                
                # Este if checa quem começou a rodada
                if vez_do_jogador == "computador": # O PC respondeu
                    carta_inicial = carta_jogada_jogador
                    carta_resposta = carta_jogada_computador
                    vencedor_da_rodada = "jogador" # Assume que jogador ganha
                else: # O Jogador respondeu
                    carta_inicial = carta_jogada_computador
                    carta_resposta = carta_jogada_jogador
                    vencedor_da_rodada = "computador" # Assume que PC ganha
                    
                naipe_da_rodada = carta_inicial.category

                # 1. Alguém jogou trunfo?
                if carta_inicial.category == trunfo.category or carta_resposta.category == trunfo.category:
                    
                    if carta_inicial.category == trunfo.category and carta_resposta.category == trunfo.category:
                        # Ambos jogaram trunfo, o maior vence
                        if carta_resposta.value > carta_inicial.value:
                            vencedor_da_rodada = "computador" if vez_do_jogador == "computador" else "jogador"
                    
                    elif carta_inicial.category == trunfo.category:
                        # Só o primeiro jogou trunfo
                        vencedor_da_rodada = "jogador" if vez_do_jogador == "computador" else "computador"
                        
                    elif carta_resposta.category == trunfo.category:
                        # Só o segundo jogou trunfo
                        vencedor_da_rodada = "computador" if vez_do_jogador == "computador" else "jogador"
                        
                # 2. Ninguém jogou trunfo
                elif carta_resposta.category != naipe_da_rodada:
                    # O segundo "falhou" (jogou naipe errado)
                    vencedor_da_rodada = "jogador" if vez_do_jogador == "computador" else "computador"
                    
                # 3. Ninguém jogou trunfo E ambos jogaram o naipe da rodada
                elif carta_resposta.value > carta_inicial.value:
                    vencedor_da_rodada = "computador" if vez_do_jogador == "computador" else "jogador"
                
                # Se nenhuma condição acima mudou o vencedor, o vencedor inicial (quem jogou a carta_inicial) ganha.

                # PONTUAÇÃO E MENSAGEM
                if vencedor_da_rodada == "jogador":
                    score_jogador += carta_jogada_jogador.value + carta_jogada_computador.value
                    print(f"Você venceu a rodada!\n")
                else:
                    score_computador += carta_jogada_jogador.value + carta_jogada_computador.value
                    print(f"O computador venceu a rodada!\n")
                
                print(f"Placar: Jogador {score_jogador} vs PC {score_computador}")
                
                # Define quem joga primeiro na próxima rodada
                vez_do_jogador = vencedor_da_rodada
                
                # Limpa a mesa
                carta_jogada_jogador = None
                carta_jogada_computador = None
                
                # Reseta o timer
                tempo_resolucao = 0
                
                # Próxima fase
                fase_da_rodada = "DISTRIBUIR"

        # FASE 4: DISTRIBUIÇÃO
        elif fase_da_rodada == "DISTRIBUIR":
            # Compra novas cartas e verifica o fim do jogo
            
            # Se ainda há cartas no baralho, compra
            if len(baralho) > 0:
                if vencedor_da_rodada == "jogador":
                    mao_jogador.append(baralho.pop(0))
                    if len(baralho) > 0:
                        mao_computador.append(baralho.pop(0))
                else:
                    mao_computador.append(baralho.pop(0))
                    if len(baralho) > 0:
                        mao_jogador.append(baralho.pop(0))
            
            # Verifica Fim do Jogo
            # Checa se as mãos estão vazias E se o jogo já não foi marcado como finalizado
            if len(mao_jogador) == 0 and len(mao_computador) == 0 and not jogo_finalizado:
                print("\nFim de jogo!")
                if score_jogador > score_computador:
                    print("---- PARABÉNS!! Você venceu!!! ----\n")
                    mensagem_fim_jogo = "VOCÊ VENCEU! Parabens!! Dominou a energia prismatica!"
                elif score_computador > score_jogador:
                    print("---- Vitória do oponente, tente novamente!! ----\n")
                    mensagem_fim_jogo = "VOCÊ PERDEU! Tente novamente! Domine a energia prismatica!"
                else:
                    print("---- Empate! ----\n")
                    mensagem_fim_jogo = "EMPATE!"
                
                # ATIVA A FLAG DE FIM DE JOGO
                jogo_finalizado = True
                tempo_fim_jogo = pygame.time.get_ticks() # MARCA A HORA QUE O JOGO ACABOU
            
            # Se o jogo NÃO acabou e NÃO está finalizado, continua
            elif not jogo_finalizado:
                fase_da_rodada = "ANUNCIO"
        
        
        # ==========================================================
        # 3. LÓGICA E DESENHO DE FIM DE JOGO 
        # ==========================================================
        
        # Este bloco agora roda DEPOIS de toda a lógica de jogo (como distribuir)
        # mas ANTES de atualizar a tela
        
        if jogo_finalizado:
            
            # --- Lógica do Timer (O "Delay") ---
            tempo_agora = pygame.time.get_ticks()
            
            # Se já se passaram 3 segundos (3000 ms)
            if tempo_agora - tempo_fim_jogo > 3000:
                jogo_ativo = False      # Desliga o jogo
                menu_ativo = True       # Liga o menu
                jogo_finalizado = False # Reseta para o próximo jogo
                mensagem_fim_jogo = ""
            
            # --- Desenho da Mensagem ---
            # (Só desenha enquanto o timer não estourou)
            else:
                # Cria uma superfície 
                overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 180)) # Preto com 180 de transparência
                tela.blit(overlay, (0, 0))

                # Define a fonte e a cor
                fonte_fim_jogo = pygame.font.SysFont("Palatino Linotype", 20, bold=True)
                cor = (255, 255, 0) # Amarelo para empate 
                
                if "VENCEU" in mensagem_fim_jogo:
                    cor = (34, 139, 34) 
                elif "PERDEU" in mensagem_fim_jogo:
                    cor = (255, 140, 0) 
                
                # Sombra
                sombra_fim = fonte_fim_jogo.render(mensagem_fim_jogo, True, (0, 0, 0))
                rect_sombra = sombra_fim.get_rect(center=(LARGURA / 2 + 3, ALTURA / 2 + 3))
                tela.blit(sombra_fim, rect_sombra)
                
                # Texto
                texto_fim = fonte_fim_jogo.render(mensagem_fim_jogo, True, cor)
                rect_texto = texto_fim.get_rect(center=(LARGURA / 2, ALTURA / 2))
                tela.blit(texto_fim, rect_texto)

        
        # ==========================================================
        # 4. ATUALIZAÇÃO FINAL DA TELA
        # ==========================================================
        pygame.display.flip()

    


    # o jogo termina
pygame.quit()