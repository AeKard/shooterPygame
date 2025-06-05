import pygame

class Player:
    def __init__(self,pos):
        self.displaySurface = pygame.display.get_surface()

        self.character = pygame.Surface((50, 50))
        self.character.fill("red")
        self.characterRect = self.character.get_rect(center = pos)
        self.pos = pygame.math.Vector2(pos)
        self.direction = pygame.math.Vector2()
        self.speed = 300

        self.health = 3
    # def getPlayerPos(self):
    #     return self.newPos

    def input(self):
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
    
    def update(self, wallRects, dt):
        self.input()
        movement = self.direction * self.speed * dt

        self.pos.x += movement.x
        self.characterRect.centerx = round(self.pos.x)
        for wall in wallRects:
            if self.characterRect.colliderect(wall):
                if movement.x > 0:  
                    self.characterRect.right = wall.left
                elif movement.x < 0:
                    self.characterRect.left = wall.right
                self.pos.x = self.characterRect.centerx

        self.pos.y += movement.y
        self.characterRect.centery = round(self.pos.y)
        for wall in wallRects:
            if self.characterRect.colliderect(wall):
                if movement.y > 0:  
                    self.characterRect.bottom = wall.top
                elif movement.y < 0: 
                    self.characterRect.top = wall.bottom
                self.pos.y = self.characterRect.centery

    def takeDamage(self):
        self.health -= 1

    def display(self,offset, wallRects, dt):
        # self.movement()
        self.update(wallRects, dt)
        off_set = self.characterRect.topleft - offset
        # print(f"Direction: {off_set}, Position: {self.characterRect.center}") # but here its correctly divided
        self.displaySurface.blit(self.character, off_set)