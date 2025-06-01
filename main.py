import pygame
from random import randint

from bulletManager import BulletManager
from entity.player import Player
from entity.enemy import Enemy
from camera import Camera
"""
    TODO: CONE SHAPE RANDOM BULLET SPREAD
        : Camera 
"""
class Main():
    def __init__(self):
        pygame.init()      
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 720, 480

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialzie Object
        self.player = Player((self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
        self.bullets = BulletManager()
        self.enemies = []
        self.camera = Camera()
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
                    mouse_pos = pygame.mouse.get_pos() + self.camera.offset
                    player_pos = self.player.characterRect.center
                    self.bullets.spawnBullet(player_pos, mouse_pos)
                    self.time_since_last_shot = 0  

            self.bullets.update(dt,self.camera.offset, self.WINDOW_WIDTH , self.WINDOW_HEIGHT)


            #Enemy bullet collider 
            for bullet in self.bullets.bullets[:]:
                for enemy in self.enemies[:]:
                    if bullet.bulletRect.colliderect(enemy.enemyRect):
                        self.bullets.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        #---
                        x = randint(100, self.WINDOW_WIDTH - 100)   
                        y = randint(100, self.WINDOW_HEIGHT - 100)
                        self.enemies.append(Enemy((x,y)))
                        break

            #checks if the last shot is not infintly adding on
            if(self.time_since_last_shot > 10):
                self.time_since_last_shot = 0
            # DIPLAY ALaL OBJECT
            self.screen.fill("black")

            self.camera.display_objects(self.enemies, self.bullets, self.player)
            pygame.display.flip()
        
        pygame.quit()
if __name__ == "__main__":
    game = Main()   
    game.gameLoop()
