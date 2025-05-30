import pygame

class Player:
    def __init__(self,pos):
        self.character = pygame.Surface((50, 50))
        self.character.fill("red")
        self.characterRect = self.character.get_rect(center = pos)

        self.newPos = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def getPlayerPos(self):
        return self.newPos

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
    
    def update(self, dt):
        if(self.direction.length() != 0):
            self.direction = self.direction.normalize()
        
        movement = self.direction * self.speed * dt
        self.new_pos = pygame.math.Vector2(self.characterRect.center) + movement
        self.characterRect.center = (round(self.new_pos.x),round(self.new_pos.y))

    def display(self, screen, dt):
        self.movement()
        self.update(dt)
        screen.blit(self.character, self.characterRect)