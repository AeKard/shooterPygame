import pygame

# TODO: random position enemy, "Spawn may be?"

class Enemy:
    def __init__(self, pos): # make pos random for now
        self.displaySurface = pygame.display.get_surface()
        self.enemy = pygame.Surface((50, 50))
        self.enemy.fill("blue")
        self.enemyRect = self.enemy.get_rect(center = pos)

    def display(self, offset):
        # print(self.enemyRect.x,self.enemyRect.y)
        off_set = self.enemyRect.topleft - offset
        self.displaySurface.blit(self.enemy, off_set)