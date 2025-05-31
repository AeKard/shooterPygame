import pygame

# TODO: random position enemy, "Spawn may be?"

class Enemy:
    def __init__(self, pos): # make pos random for now
        self.enemy = pygame.Surface((50, 50))
        self.enemy.fill("blue")
        self.enemyRect = self.enemy.get_rect(center = pos)

    def display(self, screen):
        screen.blit(self.enemy, self.enemyRect)