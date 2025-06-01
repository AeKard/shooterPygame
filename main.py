import pygame
from random import randint

from bulletManager import BulletManager
from entity.player import Player
from entity.enemy import Enemy
from camera import Camera
from ui import PlayerUI
"""
    TODO: CONE SHAPE RANDOM BULLET SPREAD
    TODO: UI TIME !!!

"""
class Main():
    def __init__(self):
        pygame.init()      
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 1080, 720

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialzie Object
        self.player = Player((self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2))
        self.playerUi = PlayerUI((10, 10))
        self.bullets = BulletManager()
        
        self.enemies = []
        self.camera = Camera()
        # random place
        for i in range(20):
            x = randint(-100, self.WINDOW_WIDTH + 100)   
            y = randint(-100, self.WINDOW_HEIGHT + 100)
            self.enemies.append(Enemy((x,y)))
        
        self.fire_rate = 0.2 
        self.time_since_last_shot = 0
        self.time_since_damage = 0.1

        
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  
            self.time_since_last_shot += dt  
            self.time_since_damage += dt
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
            #playertakedamage
            for enemy in self.enemies[:]:
                if enemy.enemyRect.colliderect(self.player.characterRect) and self.time_since_damage >= 1:
                    print("Hit")
                    self.time_since_damage = 0
                    self.player.takeDamage()
            #checks if the last shot is not infintly adding on
            if(self.time_since_last_shot > 10 and self.time_since_damage > 10):
                self.time_since_last_shot = 0
            # DIPLAY ALaL OBJECT
            self.screen.fill("black")

            self.camera.display_objects(self.enemies, self.bullets, self.player, self.playerUi)
            pygame.display.flip()
        
        pygame.quit()
if __name__ == "__main__":
    game = Main()   
    game.run()
