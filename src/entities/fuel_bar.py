# entities/fuel_bar.py
import pygame

class FuelBar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fuel = 100  # Combustível inicial (em porcentagem)
        self.color = (0, 255, 0)

    def update(self, dt):
        # Reduz o combustível com base no tempo (dt = delta time)
        self.fuel -= dt * 5  # Ajuste a velocidade de consumo
        if self.fuel < 0:
            self.fuel = 0

        # Atualiza a cor com base no nível de combustível
        if self.fuel < 30:
            self.color = (255, 0, 0)  # Vermelho se estiver baixo
        elif self.fuel < 60:
            self.color = (255, 165, 0)  # Laranja

    def draw(self, screen):
        # Calcula a largura da barra com base no combustível restante
        current_width = (self.fuel / 100) * self.width
        pygame.draw.rect(screen, self.color, (self.x, self.y, current_width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)  # Borda
