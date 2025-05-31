import pygame
from random import randint

from bulletManager import BulletManager
from entity.player import Player
from entity.enemy import Enemy
"""
    TODO: CREATE ENEMY WITH BULLET COLLISION 
        : CONE SHAPE RANDOM BULLET SPREAD
"""
class Main():
    def __init__(self):
        pygame.init()      
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 720, 480

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialzie Classes
        self.player = Player((self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2))
        self.bullets = BulletManager()
        self.enemies = []
        # random place
        for i in range(5):
            x = randint(100, self.WINDOW_WIDTH - 100)   
            y = randint(100, self.WINDOW_HEIGHT - 100)
            self.enemies.append(Enemy((x,y)))
        self.fire_rate = 0.2 
        self.time_since_last_shot = 0

    def gameLoop(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  
            self.time_since_last_shot += dt  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if pygame.mouse.get_pressed()[0]: 
                if self.time_since_last_shot >= self.fire_rate:
                    mouse_pos = pygame.mouse.get_pos()
                    player_pos = self.player.characterRect.center
                    self.bullets.spawnBullet(player_pos, mouse_pos)
                    self.time_since_last_shot = 0  

            self.bullets.update(dt, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

            for bullet in self.bullets.bullets[:]:
                for enemy in self.enemies[:]:
                    if bullet.bulletRect.colliderect(enemy.enemyRect):
                        print("hit")
                        self.bullets.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        #---
                        x = randint(100, self.WINDOW_WIDTH - 100)   
                        y = randint(100, self.WINDOW_HEIGHT - 100)
                        self.enemies.append(Enemy((x,y)))
                        break

            if(self.time_since_last_shot > 10):
                self.time_since_last_shot = 0
            self.screen.fill("black")
            self.player.display(self.screen, dt)

            self.bullets.draw(self.screen)
            for enemy in self.enemies:
                enemy.display(self.screen)
            pygame.display.flip()
        
        pygame.quit()
if __name__ == "__main__":
    game = Main()   
    game.gameLoop()
