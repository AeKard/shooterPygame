import pygame

class Player:
    def __init__(self,pos):
        self.displaySurface = pygame.display.get_surface()

        self.character = pygame.Surface((50, 50))
        self.character.fill("red")
        self.characterRect = self.character.get_rect(center = pos)
        # self.newPos = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.health = 3
    # def getPlayerPos(self):
    #     return self.newPos

    def movement(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.direction.y = -1
        elif(keys[pygame.K_s]):
            self.direction.y = 1
        else:
            self.direction.y = 0
        if(keys[pygame.K_a]):
            self.direction.x = -1
        elif(keys[pygame.K_d]):
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def update(self):
        self.movement()
        self.characterRect.center += self.direction * self.speed

    def takeDamage(self):
        self.health -= 1

    def display(self,offset):
        # self.movement()
        self.update()
        off_set = self.characterRect.topleft - offset
        # print(f"Direction: {off_set}, Position: {self.characterRect.center}") # but here its correctly divided
        self.displaySurface.blit(self.character, off_set)