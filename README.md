Jogo para trabalho final de INE5402-01208B (20242) - Programação Orientada a Objetos I.

Desenvolvido por Nicolas Kotelak Junges, Tiago Augusto Raimundi e Rogério Batisti Junior


### **Relatório do Jogo: "Olha o Aviãozinho"**

---

#### **1. Introdução**
O jogo "Olha o Aviãozinho" é inspirado em clássicos de navegação vertical, como *River Raid*. Foi desenvolvido utilizando a biblioteca Pygame e tem como objetivo testar a habilidade do jogador em desviar de obstáculos, abater inimigos e gerenciar recursos como combustível. O jogo oferece uma experiência desafiadora com elementos progressivos que aumentam a dificuldade conforme o tempo.

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
   - Execute o arquivo principal do jogo usando `python`.
   - Um menu inicial será exibido, permitindo o início do jogo.
2. **Durante o Jogo:**
   - Use as teclas de movimentação para controlar o avião e desviar de obstáculos.
   - Colete combustível para manter o avião em movimento.
   - Dispare projéteis para destruir inimigos e acumular pontos.
3. **Pausa e Saída:**
   - Pressione `Esc` para pausar o jogo a qualquer momento.
   - Para sair do jogo, feche a janela.

---

#### **4. Conceitos de Orientação a Objetos**
O jogo foi desenvolvido com forte uso de **programação orientada a objetos (POO)**, permitindo modularidade e reutilização de código. Abaixo estão os principais conceitos aplicados:

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
   - As propriedades e métodos de cada classe são bem organizados e encapsulados. Por exemplo, a barra de combustível (`FuelBar`) controla sua atualização e desenho na tela de forma isolada.
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

3. **Herança:**
   - Aparentemente não há herança explícita no código enviado, mas poderia ser aplicada para criar diferentes tipos de inimigos com uma classe base.

4. **Polimorfismo:**
   - As entidades usam métodos semelhantes (ex.: `movimentar` e `desenhar`), mas implementam comportamentos específicos, exemplificando o polimorfismo.

5. **Responsabilidade Única:**
   - Cada classe tem uma responsabilidade bem definida, promovendo um código modular.

---

#### **5. Trechos de Código**
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

#### **6. Como Executar**
1. Certifique-se de ter o Python 3.10+ e o Pygame instalados.
   - Instale o Pygame com:
     ```bash
     pip install pygame
     ```
2. Organize os arquivos e pastas conforme o projeto:
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
3. Execute o jogo:
   ```bash
   python main.py
   ```



