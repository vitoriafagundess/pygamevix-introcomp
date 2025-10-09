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
def jogada_jogador(mao_jogador):
    print("Sua vez de jogar!")
    print("Suas cartas:")

    for i, carta in enumerate(mao_jogador):
        print(f"[{i+1}] - {carta.name} ({carta.category}/valor:{carta.value})")

    while True:
        try:
            escolha = int(input(f"Escolha o número da carta que você quer jogar (1 a {len(mao_jogador)}): "))
            if 1 <= escolha <= len(mao_jogador):
                carta_jogada_jogador = mao_jogador[escolha - 1]

                # Se for Ás do trunfo, só bloqueia se houver um 10 do mesmo naipe e o jogador
                # tiver MAIS de uma carta (ou seja: existe alternativa para escolher).
                if carta_jogada_jogador.value == 11 and carta_jogada_jogador.category == trunfo.category:
                    if len(mao_jogador) > 1:
                        cartas_10_mesmo_nipe = [c for c in mao_jogador + mao_computador + baralho
                                                if c.value == 10 and c.category == carta_jogada_jogador.category]
                        if cartas_10_mesmo_nipe:
                            print("Atenção: o Ás do trunfo não pode ser jogado antes do 10! Escolha outra carta.")
                            continue
                    # se len(mao_jogador) == 1, passa (última carta; obrigatoriamente joga)

                # Remove da mão e retorna a carta
                return mao_jogador.pop(escolha - 1)

            else:
                print("Escolha inválida!")
        except ValueError:
            print("Digite um número válido!")


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
rainha_slugdiana = Card("Dama SlugDiana","Targon", 2, "")         #rainha
cavaleiro_slugleona = Card("Valete Slugleona", "Targon", 3, "")  # valete
targon_petisco_hexteck = Card("Petisco Hexteck de Targon", "Targon", 0, "")  #as cartas que não vale nada na bisca
targon_isca_hexteck = Card("Isca Hexteck de Targon", "Targon", 0, "")
condutor_prismatico_targon = Card("Condutor Prismatico de Targon", "Targon", 0, "")

        #Piltover(8 cartas) como se fosse outro nipe
caityslug = Card("Ás Caityslug", "Piltover", 11, "Disparo Calibrado")    #padrão de valores se repete para cada nipe
guardiao_da_tecnologia = Card("Dezguardião da Tecnologia", "Piltover", 10, "")
rei_slugheimer = Card("Rei SlugHeimer", "Piltover", 4, "")
rainha_slugjinx = Card("Dama SlugJinx","Piltover", 2, "")
cavaleiro_caveirslug = Card("Valete Caveirslug", "Piltover", 3, "")
piltover_petisco_hexteck = Card("Petisco Hexteck de Piltover", "Piltover", 0, "")
piltover_isca_hexteck = Card("Isca Hexteck de Piltover", "Piltover", 0, "")
condutor_prismatico_piltover = Card("Condutor Prismatico de Piltover", "Piltover", 0, "")

        #Zaun (8 cartas) representa outro nipe
samira = Card("Ás Samira", "Zaun", 11, "Estilo Desafiador")    #padrão  se repete para cada nipe
guardiao_da_mutacao = Card("Dezguardião da Mutação", "Zaun", 10, "")
rei_slugsinged = Card("Rei SlugSinged", "Zaun", 4, "")
rainha_slugcamille = Card("Dama SlugCamille","Zaun", 2, "")
cavaleiro_slugekko = Card("Valete SlugEkko", "Zaun", 3, "")
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
FUNDO_VIXTERRA = "fundoo.png"

try:
    fundo_img = pygame.image.load(FUNDO_VIXTERRA).convert()
    #garante que a imagem tenho o mesmo tamanho da tela
    fundo_img = pygame.transform.scale(fundo_img,(LARGURA, ALTURA))
except pygame.error:
    print(f"Não foi possivel carregar a imagem de fundo: {FUNDO_VIXTERRA}")
    #se der erro, cria um  fundo  para o jogo não quebrar
    fundo_img = pygame.Surface((LARGURA, ALTURA))
    fundo_img.fill((0, 0,0))

#Decidindo quem joga primeiro na rodada 
vez_do_jogador =random.choice(["jogador", "computador"])

# iniciar contagem de rodadas
numero_da_rodada = 1



# Loop que vai manter a janela aberta e funcionando:
rodando = True
while rodando:  #roda o tempo todo 
    # 1. Lida com os eventos(fechar a janela, etc.)      
    for evento in pygame.event.get(): # para cada item dentro da lista de eventos, chame esse item de evento e faça algo
        if evento.type == pygame.QUIT:
            rodando = False

    # CABEÇALHO DA RODADA
    print(f"\n --- Rodada {numero_da_rodada} ---")
    print(f"TRUNFO: {trunfo.name} valor: {trunfo.value}\n")
    numero_da_rodada += 1
    
    
    # 2. LÓGICA DA RODADA
    # verifica se os jogadores tem cartas
    if len(mao_jogador) > 0 and len(mao_computador) > 0:  
            
        # A lógica para a rodada (jogar cartas, etc.) virá aqui!
    
        #LOGICA PARA VER DE QUEM É A VEZ
        
        if vez_do_jogador == "jogador": #Quando o jogador começa a rodada:
            # ---- TURNO  DO JOGADOR ----
            carta_jogada_jogador = jogada_jogador(mao_jogador) #chamei a função jogadada_jogador
            
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
            carta_jogada_jogador = jogada_jogador(mao_jogador)
                

                    
        
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