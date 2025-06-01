import pygame

class PlayerUI:
    def __init__(self, pos):
        self.displaySurface = pygame.display.get_surface()
        self.hearts = pygame.Surface((20,20))
        self.hearts.fill("red")
        print(pos)
        self.heartsRect = self.hearts.get_rect(topleft = pos)

    def drawUI(self, margin):
        # print(healthMargin.x , healthMargin.y + 10, self.heartsRect.topleft)
        self.displaySurface.blit(self.hearts, self.heartsRect.topleft + margin)
