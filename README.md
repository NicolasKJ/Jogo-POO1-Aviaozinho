Jogo para trabalho final de INE5402-01208B (20242) - Programação Orientada a Objetos I.

Desenvolvido por Nicolas Kotelak Junges, Tiago Augusto Raimundi e Rogério Batisti Junior


### **Relatório do Jogo: "Olha o Aviãozinho"**

---

#### **1. Introdução**
O jogo "Olha o Aviãozinho" é inspirado em clássicos de navegação vertical, como *River Raid*. Foi desenvolvido utilizando a biblioteca Pygame e tem como objetivo testar a habilidade do jogador em desviar de obstáculos, abater inimigos e gerenciar combustível. A velocidade e a frequência de geração de inimigos aumenta conforme o tempo, deixando o jogo cada vez mais desafiador.

---

#### **2. Regras do Jogo**
1. **Objetivo:**
   - Acumular a maior pontuação possível ao longo do jogo.
2. **Movimentação:**
   - O jogador controla o avião com as teclas:
     - **W / S / A / D** ou setas direcionais: Movimentação do avião.
     - **Espaço**: Disparo de projéteis.
3. **Recursos:**
   - O jogador deve coletar itens de combustível para continuar jogando.
4. **Inimigos:**
   - Diferentes tipos de inimigos aparecem na tela, cada um com resistência e pontos específicos ao serem destruídos.
5. **Fim de Jogo:**
   - O jogo termina se o avião colidir com um inimigo ou se o combustível acabar.

---

#### **3. Modo de Jogar**
1. **Iniciar o Jogo:**
   - Execute o main.py do jogo usando `python`.
   - Um menu inicial será exibido, com as opções sair ou jogar.
2. **Durante o Jogo:**
   - Use as teclas de movimentação para controlar o avião e desviar de obstáculos.
   - Colete combustível para manter o avião em movimento.
   - Dispare projéteis para destruir inimigos e acumular pontos.
3. **Pausa e Saída:**
   - Pressione `Esc` para pausar o jogo a qualquer momento.
   - Para sair do jogo, feche a janela.

---

#### **4. Conceitos de Orientação a Objetos**
O jogo foi desenvolvido com programação orientada a objetos, abaixo estão os principais conceitos aplicados:

1. **Classes e Objetos:**
   - Cada elemento do jogo, como o avião, inimigos, balas e combustível, é representado por uma classe dedicada:
     - Classe `Aviao`: Controla o jogador.
     - Classe `Inimigos`: Define o comportamento dos inimigos.
     - Classe `Bullet`: Representa os projéteis disparados.
     - Classe `Fuel` e `FuelBar`: Gerenciam o sistema de combustível.
   - **Exemplo de código:**
     ```python
     class Aviao:
         def __init__(self):
             self.x = 300
             self.y = 600
             self.morreu = False
     ```

2. #### **Encapsulamento:**
   - As propriedades de cada classe são organizadas e encapsuladas. Por exemplo, a barra de combustível (`FuelBar`) controla sua atualização e desenho na tela de forma isolada.
     ```python
     class FuelBar:
         def __init__(self, x, y, width, height):
             self.x = x
             self.y = y
             self.width = width
             self.height = height
             self.fuel = 100
         def update(self, dt):
             self.fuel -= dt * 10
         def draw(self, tela):
             # Desenha a barra de combustível na tela
     ```
---

#### **3. Trechos de Código**
- **Criação e Atualização de Inimigos:**
  ```python
  x_random = random.randint(0, tamanho_tela[0] - imagem_nave1.get_width())
  novo_inimigo = Inimigos(x_random, 35, 1)
  inimigos.append(novo_inimigo)

  for inimigo in inimigos[:]:
      inimigo.movimentar(velocidade)
      if inimigo.y > tamanho_tela[1]:
          inimigos.remove(inimigo)
  ```
  - *Descrição:* Os inimigos são gerados em posições aleatórias e removidos da lista ao sair da tela.

- **Detecção de Colisões:**
  ```python
  bala_rect = pygame.Rect(bala.x, bala.y, 5, 10)
  inimigo_rect = pygame.Rect(inimigo.x, inimigo.y, largura, altura)
  if bala_rect.colliderect(inimigo_rect):
      inimigo.vida -= 1
      if inimigo.vida <= 0:
          inimigos.remove(inimigo)
  ```
  - *Descrição:* Colisões entre balas e inimigos são detectadas e processadas.

---

#### **4. Como Executar**
1. Certifique-se de ter o Python 3.10+ e o Pygame instalados.
    - Instale o Python:
       -Acesse o site oficial do Python: https://www.python.org/downloads/.
       -Faça o download da versão mais recente (recomendada para o seu sistema operacional).
       -Durante a instalação, marque a opção "Add Python to PATH".
    - Instale o Pygame com:
     ```bash
     pip install pygame
     ```
3. Organize os arquivos e pastas conforme o projeto:
   ```
   projeto/
   ├── src/
   │   ├── entities/
   │   │   ├── aviao.py
   │   │   ├── bullet.py
   │   │   ├── ...
   ├── assets/
   │   ├── sounds/
   │   ├── images/
   ├── main.py
   ```
4. Execute o jogo:
   ```bash
   python main.py
   ```



