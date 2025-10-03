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
# Estado global que controla se o 10 do trunfo já foi jogado
dez_trunfo_jogado = False  

def jogada_jogador(mao_jogador):
    global dez_trunfo_jogado  # usamos a variável global dentro da função

    print("Sua vez de jogar!")
    print("Suas cartas:")

    for i, carta in enumerate(mao_jogador):
        print(f"[{i+1}] - {carta.name} ({carta.category}/valor:{carta.value})")

    while True:
        try:
            escolha = int(input(f"Escolha o número da carta que você quer jogar (1 a {len(mao_jogador)}): "))

            if 1 <= escolha <= len(mao_jogador):
                carta_jogada_jogador = mao_jogador[escolha - 1]

                # --- Regra do Ás do trunfo ---
                if carta_jogada_jogador.value == 11 and carta_jogada_jogador.category == trunfo.category:
                    if not dez_trunfo_jogado and len(mao_jogador) > 1:
                        print("⚠️ Atenção: o Ás do trunfo não sai antes da carta que vale 10 pontos")
                        continue  # volta para escolher outra carta

                # Remove a carta da mão
                carta_jogada_jogador = mao_jogador.pop(escolha - 1)

                # Atualiza estado se for o 10 do trunfo
                if carta_jogada_jogador.value == 10 and carta_jogada_jogador.category == trunfo.category:
                    dez_trunfo_jogado = True

                print(f"- Você jogou: {carta_jogada_jogador.name} ({carta_jogada_jogador.category}/valor:{carta_jogada_jogador.value})")
                return carta_jogada_jogador  # só retorna a carta, sem precisar de dois valores
            else:
                print(f"Escolha inválida! Você só tem cartas de 1 a {len(mao_jogador)} para escolher.")
        except (ValueError, IndexError):
            print("Entrada inválida! Por favor, digite um número.")





# 3. Criação dos objetos( 30 cartas)
        #Targon (7 cartas) como se fosse o nípe copas na bisca por exemplo, ai no nipe copas tem as cartas de copas
solvix = Card("Ás Solvix", "Targon", 11, "Algoritmo Instituinte") #como se fosse o ás na bisca
print(solvix.name)
print(solvix.value)
guardiao_da_ordem = Card("Dezguardião da ordem", "Targon", 10, "")    # como se fosse o 7 na bisca
rei_slugpantheon = Card("Rei Slugpantheon", "Targon", 4, "")        # rei
rainha_slugdiana = Card("Dama SlugDiana","Targon", 2, "")         #rainha
cavaleiro_slugleona = Card("Valete Slugleona", "Targon", 3, "")  # valete
targon_petisco_hexteck = Card("Petisco Hexteck de Targon", "Targon", 0, "")  #as cartas que não vale nada na bisca
targon_isca_hexteck = Card("Isca Hexteck de Targon", "Targon", 0, "")

        #Piltover(7 cartas) como se fosse outro nipe
caityslug = Card("Ás Caityslug", "Piltover", 11, "Disparo Calibrado")    #padrão de valores se repete para cada nipe
guardiao_da_tecnologia = Card("Dezguardião da Tecnologia", "Piltover", 10, "")
rei_slugheimer = Card("Rei SlugHeimer", "Piltover", 4, "")
rainha_slugjinx = Card("Dama SlugJinx","Piltover", 2, "")
cavaleiro_caveirslug = Card("Valaete Caveirslug", "Piltover", 3, "")
piltover_petisco_hexteck = Card("Petisco Hexteck de Piltover", "Piltover", 0, "")
piltover_isca_hexteck = Card("Isca Hexteck de Piltover", "Piltover", 0, "")

        #Zaun (7 cartas) representa outro nipe
samira = Card("Ás Samira", "Zaun", 11, "Estilo Desafiador")    #padrão  se repete para cada nipe
guardiao_da_mutacao = Card("Dezguardião da Mutação", "Zaun", 10, "")
rei_slugsinged = Card("Rei SlugSinged", "Zaun", 4, "")
rainha_slugcamille = Card("Dama SlugCamille","Zaun", 2, "")
cavaleiro_slugekko = Card("Valete SlugEkko", "Zaun", 3, "")
zaun_petisco_hexteck = Card("Petisco Hexteck de Zaun", "Zaun", 0, "")
zaun_isca_hexteck = Card("Isca Hexteck de Zaun", "Zaun", 0, "")
 
# Ultilizando lista para orgazinar todas as cartas em um unico local, uma lista é como uma gaveta que guarda varios itens,
#facilita manipulação
baralho = [
    solvix, guardiao_da_ordem, rei_slugpantheon, rainha_slugdiana, cavaleiro_slugleona,
    targon_petisco_hexteck, targon_isca_hexteck,

    caityslug, guardiao_da_tecnologia, rei_slugheimer, rainha_slugjinx, cavaleiro_caveirslug,
    piltover_petisco_hexteck, piltover_isca_hexteck,

    samira, guardiao_da_mutacao, rei_slugsinged, rainha_slugcamille, cavaleiro_slugekko,
    zaun_petisco_hexteck, zaun_isca_hexteck
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

    # 2. LÓGICA DA RODADA
    # verifica se os jogadores tem cartas
    if len(mao_jogador) > 0 and len(mao_computador) > 0:  
            
        # A lógica para a rodada (jogar cartas, etc.) virá aqui!
        
        print(f"\n --- Rodada {numero_da_rodada} ---") #separando visualmente no terminal as rodadas
        numero_da_rodada += 1
        print(f" categoria do trunfo: {trunfo.category}\n")
        


        #LOGICA PARA VER DE QUEM É A VEZ
        
        if vez_do_jogador == "jogador": #Quando o jogador começa a rodada:
            # ---- TURNO  DO JOGADOR ----
            carta_jogada_jogador = jogada_jogador(mao_jogador) #chamei a função jogadada_jogador
            
            # --- TURNO DO COMPUTADOR
            print("\nVez do computador...\n")

            #carta do jogador
            carta_jogador = carta_jogada_jogador
            
            
            #lista de cartas do mesmo naipe da rodada
            cartas_mesmo_nipe = [c for c in mao_computador if c.category == carta_jogador.category]
            #lista de cartas de trunfo
            cartas_trunfo = [c for c in mao_computador if c.category == trunfo.category]
            #lista de cartas que não valem pontos
            cartas_hexteck = [c for c in mao_computador if c.value == 0]
            #Conter as cartas que não tem nada haver com a jogada "atual"
            cartas_outras = [c for c in mao_computador if c.category != carta_jogador.category and c.category != trunfo.category] #c for c in mao_computador vai percorre todas as cartas na mão do computador e selecionar algumas de acordo com a condição que vem depois
            
            #definir carta que será jogada
            carta_jogada_computador = None

            
            # 1. ---- Cartas do mesmo naipe da rodada ----
            if cartas_mesmo_nipe:
                
                #carta do mesmo naipe e é trunfo
                if carta_jogador.category == trunfo.category:
                    #jogador jogou trunfo
                    #verifica se existe carta que pode vencer
                    cartas_que_vence = [c for c in cartas_mesmo_nipe if c.value > carta_jogador.value]
                        # Se o jogador jogou carta de 10 e temos 11, joga para o relé
                    if carta_jogador.value ==10:
                        carta_11 = [c for c in cartas_que_vence if c.value == 11]
                        if carta_11:
                            carta_jogada_computador = carta_11[0] #joga o 11 para dar rele
                    
                    if not carta_jogada_computador: #so entra nesse loop se não tiver a carta 11, ou seja o computador não jogou a carta
                        if cartas_que_vence:
                            carta_jogada_computador = min(cartas_que_vence, key=lambda c: c.value) #joga a menor carta que vence
                        elif cartas_hexteck:
                            carta_jogada_computador = cartas_hexteck[0] #joga carta que não vale nada
                        elif cartas_outras:
                            carta_jogada_computador = min(cartas_outras, key=lambda c: c.value) #jogda menor carta de outro naipe
                        else:
                            carta_jogada_computador = min(cartas_trunfo, key=lambda c: c.value) #jofa o menor trunfo
                # Carta do mesmo naipe, mas não é o trunfo.
                cartas_maiores = [c for c in cartas_mesmo_nipe if c.value > carta_jogador.value] #filtra apenas cartas cujo valor é maior que o valor da carta que o jogador jogou
                if cartas_maiores:
                    carta_jogada_computador = min(cartas_maiores, key=lambda c: c .value) # joga a menor que ainda vence
                elif cartas_hexteck:
                    carta_jogada_computador = cartas_hexteck[0] #joga carta que não vale nada
                else:
                    carta_jogada_computador = min(cartas_mesmo_nipe, key=lambda c: c.value) #joga a menor carta do mesmo naipe

                
            # --- 2. Se não houver cartas do mesmo naipe---
            elif cartas_trunfo: #se não tem cartas do mesmo nipe mas o computador tem cartas do trunfo entra aqui
                if carta_jogador.value > 3 and carta_jogador.category != trunfo.category: # o computador so considera gastar o trundo se a carta do jogador vale mais que 3 pontos
                    # Vale a pena usar trunfo para ganahr a carta
                    cartas_que_vence = [c for c in cartas_trunfo if c.value . carta_jogador.value] #lista com os trunfos que são capazes de vencar a carta 
                    if cartas_que_vence:
                        carta_jogada_computador = min(cartas_que_vence, key=lambda c: c.value) #menor trunfo que vence   
                    else:
                        carta_jogada_computador = min(cartas_hexteck, key=lambda c: c.value) if cartas_hexteck else min(cartas_trunfo, key=lambda c: c.value) # caso nenhum trunfo vença, tenta jogar uma carta sem valor, e se não tiver joga o trunfo
                else:
                    #carta que não vale a pena pegar, joga menor trunfo ou carta que não vale nada
                    if cartas_hexteck:
                        carta_jogada_computador = cartas_hexteck[0]
                    else: #junta todas as cartas que não são do naipe jogado nem trunfo(CARTAS_OUTRAS), com os trunfos e joga a menor carta possivel desse conjunto
                        carta_jogada_computador = min(cartas_outras + cartas_trunfo, key=lambda c: c.value)
            
            
            # 3. ---- Caso não tenha cartas do mesmo naipe nem trunfos -- 
            elif cartas_hexteck:
                carta_jogada_computador = cartas_hexteck[0] #joga carta que não vale nada
            
            #4. --- Ultima alternativa: joga a menor carta da mão
            else:
                carta_jogada_computador = min(mao_computador, key=lambda c: c.value)

            # Remove a carta da mão
            mao_computador.remove(carta_jogada_computador)
            print(f"- O computador jogou: {carta_jogada_computador.name} ({carta_jogada_computador.category}/valor:{carta_jogada_computador.value})\n") 
            
 
        else: #-----Quando o computador começa a rodada:-------
            # --- TURNO DO COMPUTADOR ---
            print("\nVez do computador...")
            cartas_trunfo_ia_namao = [carta for carta in mao_computador if carta.category == trunfo.category]
            if len(cartas_trunfo_ia_namao) > 0:
                carta_jogada_computador = random.choice(cartas_trunfo_ia_namao)
                mao_computador.remove(carta_jogada_computador)
                print(f"- O computador jogou: {carta_jogada_computador.name} ({carta_jogada_computador.category}/valor:{carta_jogada_computador.value})\n")
 
            else:
                carta_jogada_computador = random.choice(mao_computador)
                mao_computador.remove(carta_jogada_computador)
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
     
    else:
        # o jogo termina aqui
        print("\nFim do jogo!")
        if score_jogador > score_computador:
            print("---- PARABÉNS!! Você venceu!!! ----\n")
        elif score_computador > score_jogador:
            print("---- Vitória do oponente, tente novamente e domine a energia prismática!! ----\n")
        else:
            print("---- Empate! ----\n")
        rodando = False

    # 3. Lógica de renderização da tela
    # Preenche o fundo da tela com uma cor 
    tela.fill((255, 255, 0)) # código RGB 
    # Atualiza a tela para mostar oque foi desenhado
    pygame.display.flip()

 


# o jogo termina
pygame.quit()