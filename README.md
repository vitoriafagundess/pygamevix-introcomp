---
# Vixterra: Duelo de Prismas

Um MVP de um card game por turnos, construído em Python e Pygame.

---

### 📜 Resumo do Projeto

O projeto é um duelo 1x1 contra a inteligência artificial, que adapta as regras do jogo de cartas **Bisca** para um universo original. A estética do jogo mistura a tecnologia e a magia de **League of Legends** com o ambiente de cavernas de **Slugterraneo**.

### 🗺️ Contexto e História

O mundo de **Vixterra** é uma vasta rede de cavernas e passagens subterrâneas, onde os mestres duelistas competem para aprimorar sua maestria. Eles não duelam por poder, mas por honra em uma série de torneios chamados de **Confrontos de Prisma**. A própria energia de Vixterra é prismática, e os duelistas lutam com essa força.

Os duelistas invocam **Lesmas Constructos** (um termo em psicologia e engenharia que se refere a uma ideia ou estrutura criada), que são a manifestação da sua própria mente e estratégia de combate (união PsiEng). As categorias das cartas que eles usam, como **Targon**, **Piltover** e **Zaun**, são **disciplinas de combate**. Cada disciplina representa uma filosofia de duelo diferente:

* **Targon:** A disciplina da ascensão e do poder espiritual.
* **Piltover:** A disciplina da precisão e da tecnologia.
* **Zaun:** A disciplina da adaptação e da força bruta.

### 🎮 Regras do Jogo

* **Baralho:** 30 cartas no total, divididas igualmente entre Targon, Piltover e Zaun.
* **Mão:** Cada jogador começa com 3 cartas.
* **Turno:** Joga-se uma carta de cada vez. A cada rodada, ambos os jogadores compram uma nova carta do baralho.
* **Vencendo a Rodada:**
    * A carta de maior valor na categoria **Trunfo** vence.
    * Se não houver carta Trunfo, a carta com maior valor de ponto vence.
* **Pontuação:** Quem vence a rodada pega as duas cartas e soma os pontos. O duelo termina quando todas as cartas acabam, e o jogador com mais pontos vence.

### 🃏 O Baralho Completo

O baralho é composto por 30 cartas com valores de ponto fixos, seguindo o padrão da Bisca.

#### **Targon**
* **Solvix** (Ás) - Ataque: **Algoritmo Instituinte** - **11 pontos**
* **Guardião da Ordem** (7) - **10 pontos**
* **Rei SlugPantheon** (Rei) - **4 pontos**
* **Rainha SlugDiana** (Rainha) - **4 pontos**
* **Cavaleiro SlugLeona** (Cavaleiro) - **3 pontos**
* **Unidade Hexteck de Targon** (3) - **0 pontos**
* **Isca Hexteck de Targon** (2) - **0 pontos**

#### **Piltover**
* **Caityslug** (Ás) - Ataque: **Disparo Calibrado** - **11 pontos**
* **Guardião da Tecnologia** (7) - **10 pontos**
* **Rei SlugHeimer** (Rei) - **4 pontos**
* **Rainha SlugJinx** (Rainha) - **4 pontos**
* **Cavaleiro Caveirslug** (Cavaleiro) - **3 pontos**
* **Unidade Hexteck de Piltover** (3) - **0 pontos**
* **Isca Hexteck de Piltover** (2) - **0 pontos**

#### **Zaun**
* **Samirae** (Ás) - Ataque: **Estilo Desafiador** - **11 pontos**
* **Guardião da Mutação** (7) - **10 pontos**
* **Rei SlugSinged** (Rei) - **4 pontos**
* **Rainha SlugCamille** (Rainha) - **4 pontos**
* **Cavaleiro SlugEkk** (Cavaleiro) - **3 pontos**
* **Unidade Hexteck de Zaun** (3) - **0 pontos**
* **Isca Hexteck de Zaun** (2) - **0 pontos**
