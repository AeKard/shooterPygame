import pygame

# TODO: random position enemy, "Spawn may be?"

class Enemy:
    def __init__(self, pos): # make pos random for now
        self.displaySurface = pygame.display.get_surface()
        self.enemy = pygame.Surface((50, 50))
        self.enemy.fill("blue")
        self.enemyRect = self.enemy.get_rect(center = pos)
        self.pos = pygame.Vector2(self.enemyRect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 100
        #Health of the Enemy
    
    def enemyMovement(self, playerPos, dt, other_enemies, wallRects):
        playerVec = pygame.Vector2(playerPos)
        self.direction = playerVec - self.pos
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        movement = self.direction * self.speed * dt

        self.pos.x += movement.x
        self.enemyRect.centerx = round(self.pos.x)

        for other in other_enemies:
            if other is self:
                continue
            if self.enemyRect.colliderect(other.enemyRect):
                self.pos.x -= movement.x
                self.enemyRect.centerx = round(self.pos.x)
                break

        for wall in wallRects:
            if self.enemyRect.colliderect(wall):
                self.pos.x -= movement.x
                self.enemyRect.centerx = round(self.pos.x)
                break

        # Move along Y axis
        self.pos.y += movement.y
        self.enemyRect.centery = round(self.pos.y)

        for other in other_enemies:
            if other is self:
                continue
            if self.enemyRect.colliderect(other.enemyRect):
                self.pos.y -= movement.y
                self.enemyRect.centery = round(self.pos.y)
                break

        for wall in wallRects:
            if self.enemyRect.colliderect(wall):
                self.pos.y -= movement.y
                self.enemyRect.centery = round(self.pos.y)
                break
    def display(self, offset):
        # print(self.enemyRect.x,self.enemyRect.y)
        off_set = self.enemyRect.topleft - offset
        self.displaySurface.blit(self.enemy, off_set)