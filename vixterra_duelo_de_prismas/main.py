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



# Variavel que indica se o 10 do trunfo ja foi jogado
dez_trunfo_jogado = False 


#função para jogada do jogador
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
solvix = Card("Ás Solvix", "Targon", 11, "Algoritmo Instituinte") #como se fosse o ás na bisca
print(solvix.name)
print(solvix.value)
guardiao_da_ordem = Card("Dezguardião da ordem", "Targon", 10, "")    # como se fosse o 7 na bisca
rei_slugpantheon = Card("Rei Slugpantheon", "Targon", 4, "")        # rei
cavaleiro_slugleona = Card("Valete Slugleona", "Targon", 3, "")  # valete
rainha_slugdiana = Card("Dama SlugDiana","Targon", 2, "")         #rainha
targon_petisco_hexteck = Card("Petisco Hexteck de Targon", "Targon", 0, "")  #as cartas que não vale nada na bisca
targon_isca_hexteck = Card("Isca Hexteck de Targon", "Targon", 0, "")
condutor_prismatico_targon = Card("Condutor Prismatico de Targon", "Targon", 0, "")

        #Piltover(8 cartas) como se fosse outro nipe
caityslug = Card("Ás Caityslug", "Piltover", 11, "Disparo Calibrado")    #padrão de valores se repete para cada nipe
guardiao_da_tecnologia = Card("Dezguardião da Tecnologia", "Piltover", 10, "")
rei_slugheimer = Card("Rei SlugHeimer", "Piltover", 4, "")
cavaleiro_caveirslug = Card("Valete Caveirslug", "Piltover", 3, "")
rainha_slugjinx = Card("Dama SlugJinx","Piltover", 2, "")
piltover_petisco_hexteck = Card("Petisco Hexteck de Piltover", "Piltover", 0, "")
piltover_isca_hexteck = Card("Isca Hexteck de Piltover", "Piltover", 0, "")
condutor_prismatico_piltover = Card("Condutor Prismatico de Piltover", "Piltover", 0, "")

        #Zaun (8 cartas) representa outro nipe
samira = Card("Ás Samira", "Zaun", 11, "Estilo Desafiador")    #padrão  se repete para cada nipe
guardiao_da_mutacao = Card("Dezguardião da Mutação", "Zaun", 10, "")
rei_slugsinged = Card("Rei SlugSinged", "Zaun", 4, "")
cavaleiro_slugekko = Card("Valete SlugEkko", "Zaun", 3, "")
rainha_slugcamille = Card("Dama SlugCamille","Zaun", 2, "")
zaun_petisco_hexteck = Card("Petisco Hexteck de Zaun", "Zaun", 0, "")
zaun_isca_hexteck = Card("Isca Hexteck de Zaun", "Zaun", 0, "")
condutor_prismatico_zaun = Card("Condutor prismatico de Zaun", "Zaun", 0, "")
 
# Ultilizando lista para orgazinar todas as cartas em um unico local, uma lista é como uma gaveta que guarda varios itens,
#facilita manipulação
baralho = [
    solvix, guardiao_da_ordem, rei_slugpantheon, rainha_slugdiana, cavaleiro_slugleona,
    targon_petisco_hexteck, targon_isca_hexteck, condutor_prismatico_targon,

    caityslug, guardiao_da_tecnologia, rei_slugheimer, rainha_slugjinx, cavaleiro_caveirslug,
    piltover_petisco_hexteck, piltover_isca_hexteck, condutor_prismatico_piltover,

    samira, guardiao_da_mutacao, rei_slugsinged, rainha_slugcamille, cavaleiro_slugekko,
    zaun_petisco_hexteck, zaun_isca_hexteck, condutor_prismatico_zaun
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
FUNDO_VIXTERRA = "vixterra_iniciar.png"

try:
    fundo_img = pygame.image.load(FUNDO_VIXTERRA).convert()
    #garante que a imagem tenho o mesmo tamanho da tela
    fundo_img = pygame.transform.scale(fundo_img,(LARGURA, ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem de fundo: {FUNDO_VIXTERRA}")
    #se der erro, cria um  fundo  para o jogo não quebrar
    fundo_img = pygame.Surface((LARGURA, ALTURA))
    fundo_img.fill((0, 0,0))

# --- CONFIGURAÇÃO DA TELA INICIAL COM FUNDO ANIMADO E LOGO ---

LOGO_PNG = "nome_vixterra.png"  # nome do arquivo da logo

# Carrega fundo 
try:
    fundo_img = pygame.image.load(FUNDO_VIXTERRA).convert()
    fundo_img = pygame.transform.scale(fundo_img, (1080, ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem de fundo: {FUNDO_VIXTERRA}")
    fundo_img = pygame.Surface((LARGURA, ALTURA))
    fundo_img.fill((0, 0, 0))

# Carrega logo com canal alpha (transparência)
try:
    logo = pygame.image.load(LOGO_PNG).convert_alpha()
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
MENU_PRINCIPAL_IMG = "menu_vixterra.png"
try:
    menu_principal = pygame.image.load(MENU_PRINCIPAL_IMG).convert()
    menu_principal = pygame.transform.scale(menu_principal, (LARGURA, ALTURA))
except pygame.error:
    print(f"Não foi possível carregar a imagem: {MENU_PRINCIPAL_IMG}")
    menu_principal = pygame.Surface((LARGURA, ALTURA))
    menu_principal.fill((50, 50, 50))  # fundo cinza se der erro

# --- MENU INTERATIVO ---
menu_ativo = True  # variável de controle para manter o menu ativo

# Criar retângulos para botões interativos
botao_voltar_rect = pygame.Rect(20, ALTURA - 40 - 20, 120, 40)
  # botão "Voltar" (x, y, largura, altura)
aba_cartas_rect = pygame.Rect(400, 300, 200, 50)  # botão "Cartas" (x, y, largura, altura)

#botao jogar
botao_jogar_rect = pygame.Rect(400, ALTURA - 100, 120, 40)  # x, y, largura, altura

# fonte para os textos dos botões
fonte = pygame.font.SysFont(None, 28)

    


#Decidindo quem joga primeiro na rodada 
vez_do_jogador =random.choice(["jogador", "computador"])

# iniciar contagem de rodadas
numero_da_rodada = 1



# Loop que vai manter a janela aberta e funcionando:
jogo_ativo = False
rodando = True

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
                    jogo_ativo = True
                    menu_ativo = False

                # Botão "Cartas"
                elif aba_cartas_rect.collidepoint(evento.pos):
                    print("Abrir tela das cartas") 

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

    
    # --- ESTADO C: JOGO ATIVO ---
    elif jogo_ativo:
        # A lógica de rodada completa (incluindo jogada_jogador_mouse) deve estar aqui
        
        # CABEÇALHO DA RODADA
        print(f"\n --- Rodada {numero_da_rodada} ---")
        print(f"TRUNFO: {trunfo.name} valor: {trunfo.value}\n")
        numero_da_rodada += 1
        
        
        # LÓGICA DA RODADA
        if len(mao_jogador) > 0 and len(mao_computador) > 0: 
            
            # 1. Montar e Desenhar Cartas do Jogador (visualização)
            cartas_retangulos = []
            margem_x = 100; y_cartas = ALTURA - 220; larg_card, alt_card = 120, 180
            for idx, carta in enumerate(mao_jogador):
                x = margem_x + idx * (larg_card + 20); rect = pygame.Rect(x, y_cartas, larg_card, alt_card)
                cartas_retangulos.append(rect)
                pygame.draw.rect(tela, (200, 200, 200), rect)
                texto_nome = fonte_peq.render(carta.name, True, (0, 0, 0))
                tela.blit(texto_nome, (x + 6, y_cartas + 6))
                
            pygame.display.flip() 
        
    
    # --- ESTADO B: MENU PRINCIPAL ---
    elif menu_ativo:
        # --- EVENTOS DO MENU ---
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN: 
                if evento.button == 1:
                    # Botão "Voltar" (volta para Splash)
                    if botao_voltar_rect.collidepoint(evento.pos): 
                        menu_ativo = False
                        splash_rodando = True
                        # Reseta as variáveis da Splash para que ela role novamente
                        tempo_splash = 0
                        splash_congelada = False
                        splash_start = pygame.time.get_ticks() 
                        scroll_total = 0 # Volta o scroll para zero
                    
                    # Botão "Jogar" (vai para o Jogo)
                    elif botao_jogar_rect.collidepoint(evento.pos):
                        jogo_ativo = True
                        menu_ativo = False
        
        # --- DESENHO DO MENU ---
        tela.blit(menu_principal, (0, 0))

        # Desenhar BOTÕES
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

    
    # --- ESTADO C: JOGO ATIVO ---
    elif jogo_ativo:
            # CABEÇALHO DA RODADA
            print(f"\n --- Rodada {numero_da_rodada} ---")
            print(f"TRUNFO: {trunfo.name} valor: {trunfo.value}\n")
            numero_da_rodada += 1
            
            
            # 2. LÓGICA DA RODADA
            # verifica se os jogadores tem cartas
            if len(mao_jogador) > 0 and len(mao_computador) > 0:  
                    
                # A lógica para a rodada (jogar cartas, etc.) virá aqui!
                        # --- Montar retângulos clicáveis para a mão do jogador ---
                cartas_retangulos = []                             # lista de pygame.Rect (áreas clicáveis)
                margem_x = 100                                    # posição inicial no eixo X (margem esquerda)
                y_cartas = ALTURA - 220                           # posição Y das cartas na tela (um pouco acima da base)
                larg_card, alt_card = 120, 180                    # largura e altura de cada carta (ajuste se quiser)

                for idx, carta in enumerate(mao_jogador):          # percorre cada carta da mão do jogador
                    x = margem_x + idx * (larg_card + 20)          # calcula posição X com espaçamento entre cartas
                    rect = pygame.Rect(x, y_cartas, larg_card, alt_card)  # cria o retângulo clicável da carta
                    cartas_retangulos.append(rect)                 # adiciona o retângulo à lista

                    # --- Desenhar a carta (provisório, até ter imagens) ---
                    pygame.draw.rect(tela, (200, 200, 200), rect)  # desenha o retângulo cinza (a carta)
                    fonte_peq = pygame.font.SysFont(None, 20)      
                    texto_nome = fonte_peq.render(carta.name, True, (0, 0, 0))  # mostra o nome da carta
                    tela.blit(texto_nome, (x + 6, y_cartas + 6))  # desenha o nome dentro da "carta"

                pygame.display.flip()  # atualiza a tela para o jogador ver as cartas

                #LOGICA PARA VER DE QUEM É A VEZ
                
                if vez_do_jogador == "jogador": #Quando o jogador começa a rodada:
                    # ---- TURNO  DO JOGADOR ----
                    #carta_jogada_jogador = jogada_jogador(mao_jogador) #chamei a função jogadada_jogador so funciona no terminal isso
                    # desenhar as áreas clicáveis das cartas antes (ver passo 2)
                    carta_jogada_jogador = jogada_jogador_mouse(mao_jogador, cartas_retangulos)

                    
                    if carta_jogada_jogador.value == 10 and carta_jogada_jogador.category == trunfo.category:
                        dez_trunfo_jogado = True


                    # --- TURNO DO COMPUTADOR ---
                    print("\nVez do computador...\n")

                    # Inicializamos a variável para garantir que ela sempre exista
                    carta_jogada_computador = None

                    # Pega a lista de cartas que a IA pode jogar (respeitando a regra do Ás)
                    mao_computador_validas = filtrar_as_trunfo(mao_computador, mao_jogador, baralho, trunfo)

                    # --- LÓGICA REESTRUTURADA ---
                    # A IA vai testar cada estratégia em ordem de prioridade.

                    # ESTRATÉGIA 1 : Contra-atacar cartas de valor alto (10 ou 11) com um trunfo.
                    if carta_jogada_jogador.value >= 10 and carta_jogada_jogador.category != trunfo.category:
                        trunfos_validos = [c for c in mao_computador_validas if c.category == trunfo.category]
                        if trunfos_validos:
                            # Joga o menor trunfo possível para economizar os maiores
                            carta_jogada_computador = min(trunfos_validos, key=lambda c: c.value)

                    # ESTRATÉGIA 2 : Se a estratégia 1 não foi usada, tenta vencer com uma carta maior do mesmo naipe.
                    if carta_jogada_computador is None: # Só entra aqui se a estratégia anterior falhou
                        cartas_mesmo_nipe = [c for c in mao_computador_validas if c.category == carta_jogada_jogador.category]
                        if cartas_mesmo_nipe:
                            cartas_maiores = [c for c in cartas_mesmo_nipe if c.value > carta_jogada_jogador.value]
                            if cartas_maiores:
                                # Se tem cartas que vencem, joga a menor delas
                                carta_jogada_computador = min(cartas_maiores, key=lambda c: c.value)
                            else:
                                # Se não pode vencer, joga a menor carta que tiver do mesmo naipe (para perder pouco)
                                carta_jogada_computador = min(cartas_mesmo_nipe, key=lambda c: c.value)

                    # ESTRATÉGIA 3 (Fallback): Se nenhuma das anteriores funcionou (porque não tinha as cartas certas).
                    if carta_jogada_computador is None:
                        # Se não tem cartas do mesmo naipe, a prioridade é usar o menor trunfo
                        cartas_trunfo_validas = [c for c in mao_computador_validas if c.category == trunfo.category]
                        if cartas_trunfo_validas:
                            carta_jogada_computador = min(cartas_trunfo_validas, key=lambda c: c.value)
                        else:
                            # Se não tem mesmo naipe NEM trunfo, joga a carta de menor valor que tiver na mão
                            # para perder o mínimo de pontos possível.
                            carta_jogada_computador = min(mao_computador_validas, key=lambda c: c.value)
                    
                    # Executa a jogada que foi decidida em uma das estratégias acima
                    mao_computador.remove(carta_jogada_computador)
                    print(f"- O computador jogou: {carta_jogada_computador.name} ({carta_jogada_computador.category}/valor:{carta_jogada_computador.value})\n")
                        
        
                else: #-----Quando o computador começa a rodada:-------
                    # --- TURNO DO COMPUTADOR ---
                    print("\nVez do computador...")

                    # Filtra cartas válidas respeitando o bloqueio do Ás do trunfo
                    mao_computador_validas = filtrar_as_trunfo(mao_computador, mao_jogador, baralho, trunfo)

                    # Prioridades de jogada:
                    # 1. Carta de baixo custo (valor >0 e <=3)
                    cartas_baixo_custo = [c for c in mao_computador_validas if 0 < c.value <= 3]

                    # 2. Carta que não vale nada (valor 0)
                    cartas_sem_valor = [c for c in mao_computador_validas if c.value == 0]

                    # 3. Cartas de trunfo válidas (menos o Ás bloqueado)
                    cartas_trunfo_validas = [c for c in mao_computador_validas if c.category == trunfo.category]

                    # 4. Cartas altas fora do trunfo
                    cartas_altas_nao_trunfo = [c for c in mao_computador_validas if c.value > 3 and c.category != trunfo.category]

                    # Escolher a carta seguindo a prioridade
                    if cartas_baixo_custo:
                        carta_jogada_computador = min(cartas_baixo_custo, key=lambda c: c.value)  # menor carta de baixo custo
                    elif cartas_sem_valor:
                        carta_jogada_computador = cartas_sem_valor[0]  # joga qualquer carta sem valor
                    elif cartas_trunfo_validas:
                        carta_jogada_computador = min(cartas_trunfo_validas, key=lambda c: c.value)  # menor trunfo, respeitando Ás
                    elif cartas_altas_nao_trunfo:
                        carta_jogada_computador = max(cartas_altas_nao_trunfo, key=lambda c: c.value)  # maior carta fora do trunfo
                    else:
                        # Se nada se encaixa, joga o maior trunfo restante (incluindo Ás se for último)
                        carta_jogada_computador = max(mao_computador, key=lambda c: c.value)

                    # Remove a carta da mão
                    mao_computador.remove(carta_jogada_computador)

                    # Atualiza estado se for o 10 do trunfo
                    if carta_jogada_computador.value == 10 and carta_jogada_computador.category == trunfo.category:
                        dez_trunfo_jogado = True

                    # Mostra a carta jogada
                    print(f"- O computador jogou: {carta_jogada_computador.name} ({carta_jogada_computador.category}/valor:{carta_jogada_computador.value})\n")

                    # --- TURNO DO JOGADOR ---
                    # desenhar as áreas clicáveis das cartas antes (ver passo 2)
                    carta_jogada_jogador = jogada_jogador_mouse(mao_jogador, cartas_retangulos)

                        

                            
                
                # LOGICA PARA DECIDIR O VENCEDOR
                #mesa para a rodada
                mesa = [carta_jogada_jogador, carta_jogada_computador] #lista chamada mesa e adiciona as cartas do computador e do jogador

                # DECIDE O NIPE DA RODADA(O DA PRIMEIRA CARTA DO JOGADOR)
                naipe_da_rodada = carta_jogada_jogador.category

                #Encontra as cartas trunfo na mesa, passo crucial para que o jogo saiba se a regra de trunfo se aplica ou não
                cartas_trunfo_na_mesa = [carta for carta in mesa if carta.category == trunfo.category]  

                vencedor = None 

                
                if len(cartas_trunfo_na_mesa) > 0:    #verifar se a lista de trunfo na mesa ta vazia ou nao
                    #Lógica para quando há trunfo na mesa
                    #1. encontrar a carta trunfo de maior valor na mesa
                    carta_vencedora = max(cartas_trunfo_na_mesa, key=lambda carta: carta.value) # função lambda cria a regra de que a função max() deve comparar as cartas apenas com base no seu valor(pontuação)
                    #2. decide quem é o vencedor com base na carta
                    if carta_vencedora == carta_jogada_jogador:
                        vencedor = "jogador"
                    else:
                        vencedor = "computador"
                else:
                    # lógica para quando não há trunfo na mesa
                    # se o nipe da carta do computador é mesmo da rodada 
                    if carta_jogada_computador.category == naipe_da_rodada:
                        #A carta de maior valor vence
                        if carta_jogada_computador.value > carta_jogada_jogador. value:
                            vencedor = "computador"
                        else:
                            vencedor = "jogador"
                    # se o naipe da carta do computador é diferente, o jogador vence
                    else:
                        vencedor = "jogador"

                
                
                #  PONTUAÇÃO E COMPRAR NOVAS CARTAS
                    #soma pontos
                if vencedor == "jogador":
                    for carta in mesa:
                        score_jogador += carta.value #soma o valor da carta ao score do jogador
                else:
                    for carta in mesa:
                        score_computador += carta.value 

                if vencedor == "jogador":
                    print(f"Você venceu a rodada!\n")
                    print(f"Seu score: {score_jogador}\nScore oponente: {score_computador}")
                else:
                    print(f"O computador venceu a rodada!\n")
                    print(f"Score do oponente: {score_computador}\nSeu Score: {score_jogador}")


                #define quem joga primeiro na próxima rodada
                if vencedor == "jogador":
                    vez_do_jogador = "jogador"
                else:
                    vez_do_jogador = "computador"


                    #comprando as cartas e verifica quem é o vencedor da rodada e faz com que ele compre a carta primeiro
            if len(baralho) > 0:
                if vencedor == "jogador":
                    mao_jogador.append(baralho.pop(0)) #função pop pega a carta do baralho e adiciona á mao do jogador
                    if len(baralho) > 0:
                        mao_computador.append(baralho.pop(0))
                else:
                    mao_computador.append(baralho.pop(0))
                    if len(baralho) > 0:
                        mao_jogador.append(baralho.pop(0))
            
            if len(mao_jogador) == 0 and len(mao_computador) == 0 and len(baralho) == 0:   #verifica o fim do jogo somente depois que os jogadores compram as cartas    
                # Fim do jogo
                print("\nFim do jogo!")
                if score_jogador > score_computador:
                    print("---- PARABÉNS!! Você venceu!!! ----\n")
                elif score_computador > score_jogador:
                    print("---- Vitória do oponente, tente novamente!! ----\n")
                else:
                    print("---- Empate! ----\n")   
                rodando = False 
            

            # 3. Lógica de renderização da tela
            tela.blit(fundo_img, (0, 0)) # código RGB 
            # Atualiza a tela para mostar oque foi desenhado
            pygame.display.flip()

    


    # o jogo termina
pygame.quit()