import pygame

class LevelManager:
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()

        self.restrictedAreaSpawn = pygame.Rect((self.displaySurface.get_size()[0]/2)/2, (self.displaySurface.get_size()[1]/2)/2, (self.displaySurface.get_size()[1]/2)/2 * 3, (self.displaySurface.get_size()[0]/2)/2 * 2)
        print(self.restrictedAreaSpawn)
        self.verticalWall = pygame.Surface((40, self.displaySurface.get_size()[1]))
        self.horizontalWall = pygame.Surface((self.displaySurface.get_size()[0], 40))
        self.floor = pygame.Surface((1500, 2000) )
        self.vWallRect = self.verticalWall.get_rect(topleft = (-40,0))
        self.wWallRect = self.horizontalWall.get_rect(topleft = (0,0))
        self.floor.fill((30, 141, 28))
        self.verticalWall.fill("orange")
        self.horizontalWall.fill("orange")
    def displayLevel(self,offset):
        self.displaySurface.blit(self.floor,(-100,-500) - offset)
        self.displaySurface.blit(self.verticalWall, self.vWallRect.topleft - offset)
        self.displaySurface.blit(self.horizontalWall, self.wWallRect.topleft - offset)
