# Vixterra: Duelo de Prismas

Um MVP de um card game por turnos, construído em Python e Pygame.

### 📜 Resumo do Projeto

O projeto é um duelo 1x1 contra a inteligência artificial, que adapta as regras do jogo de cartas **Bisca** para um universo original. A estética do jogo mistura a tecnologia e a magia de **League of Legends** com o ambiente de cavernas de **Slugterraneo**.

### 🗺️ Contexto e História

O mundo de **Vixterra** é uma vasta rede de cavernas e passagens subterrâneas. No coração desse mundo, a energia vital emana de gigantescos cristais conhecidos como **Prismas**, a fonte de todo o poder que movimenta vixterra.

Os mestres duelistas competem por honra em torneios chamados de **Confrontos de Prisma**. Eles não invocam monstros, mas sim **Lesmas Constructos** que são a manifestação da mente, da estratégia e da disciplina a que pertencem. Elas representam a união entre a criação abstrata da mente e a lógica de construção(união psieng), se tornando um campo de batalha onde as ideias se materializam.

Cada Lesma Constructo pertence a uma das três disciplinas de combate — **Targon, Piltover ou Zaun** —, que representam diferentes filosofias de duelo. Os personagens do seu jogo, como Solvix, Caityslug e Samira, são os campeões lendários de cada uma dessas disciplinas.

As categorias de cartas **Targon**, **Piltover** e **Zaun** representam uma filosofia de duelo diferente:

* **Targon:** A disciplina da ascensão e do poder espiritual.
* **Piltover:** A disciplina da precisão e da tecnologia.
* **Zaun:** A disciplina da adaptação e da força bruta.

A **pontuação** no jogo **simboliza o domínio dessa energia prismática**. O objetivo é aprimorar sua maestria e, ao final do duelo, demonstrar que seu controle sobre essa força é maior do que o do seu oponente.

### 🎮 Regras do Jogo

* **Baralho:** 30 cartas no total, divididas igualmente entre Targon, Piltover e Zaun.
* **Mão:** Cada jogador começa com 3 cartas.
* **Turno:** Joga-se uma carta de cada vez. A cada rodada, ambos os jogadores compram uma nova carta do baralho.
* **Vencendo a Rodada:**
    * A carta de maior valor na categoria **Trunfo** vence.
    * Se não houver carta Trunfo, a carta com maior valor de ponto vence.
* **Pontuação:** Quem vence a rodada pega as duas cartas e soma os pontos. O duelo termina quando todas as cartas acabam, e o jogador com mais pontos vence.

### 🃏 O Baralho Completo

O baralho é composto por 24 cartas com valores de ponto fixos, seguindo o padrão da Bisca.

#### **Targon**
* **Solvix** (Ás) - Ataque: **Algoritmo Instituinte** - **11 pontos**
* **Guardião da Ordem** (7) - **10 pontos**
* **Rei SlugPantheon** (Rei) - **4 pontos**
* **Cavaleiro SlugLeona** (Valete) - **3 pontos**
* **Rainha SlugDiana** (Dama) - **2 pontos**

* **Unidade Hexteck de Targon**  - **0 pontos**
* **Isca Hexteck de Targon**  - **0 pontos**
* **Condutor Prismatico de Targon** - **0 pontos**

#### **Piltover**
* **Caityslug** (Ás) - Ataque: **Disparo Calibrado** - **11 pontos**
* **Guardião da Tecnologia** (7) - **10 pontos**
* **Rei SlugHeimer** (Rei) - **4 pontos**
* **Cavaleiro Caveirslug** (Valete) - **3 pontos**
* **Rainha SlugJinx** (Dama) - **2 pontos**


* **Unidade Hexteck de Piltover**  - **0 pontos**
* **Isca Hexteck de Piltover** - **0 pontos**
* **Condutor Prismatico de Piltover** - **0 pontos**

#### **Zaun**
* **Samira** (Ás) - Ataque: **Estilo Desafiador** - **11 pontos**
* **Guardião da Mutação** (7) - **10 pontos**
* **Rei SlugSinged** (Rei) - **4 pontos**
* **Cavaleiro SlugEkk** (Valete) - **3 pontos**
* **Rainha SlugCamille** (Dama) - **2 pontos**

  
* **Unidade Hexteck de Zaun**  - **0 pontos**
* **Isca Hexteck de Zaun**  - **0 pontos**
* **Condutor Prismatico de Zaun** - **0 pontos**
