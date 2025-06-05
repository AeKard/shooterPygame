import pygame

from setting import *
from bulletManager import BulletManager
from entity.player import Player

from camera import Camera
from ui import PlayerUI
from levelManager import LevelManager 
"""
    TODO: CONE SHAPE RANDOM BULLET SPREAD
    TODO: UI TIME Health and bullet reload
    FIXME: do the tile Area 
         : fix the setting, setup for easy navigation 
    
    About this game is protecting the center using powerups
"""
class Main():
    def __init__(self):
        pygame.init()      

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # Initialzie Object
        self.player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.playerUi = PlayerUI((10, 10))
        self.bullets = BulletManager()
        
        self.camera = Camera()
        self.enemySpawnArea = pygame.math.Vector2((1500, 2000))
        self.level = LevelManager((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), self.enemySpawnArea)
        self.enemies = self.level.setupEnemy()

        self.fire_rate = 0.2 
        self.time_since_last_shot = 0
        self.time_since_damage = 0.1

        
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  
            self.time_since_last_shot += dt  
            self.time_since_damage += dt
            print(round(self.clock.get_fps()))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # GameSetup ---
            if pygame.mouse.get_pressed()[0]: 
                if self.time_since_last_shot >= self.fire_rate:
                    mouse_pos = pygame.mouse.get_pos() + self.camera.offset
                    player_pos = self.player.characterRect.center
                    self.bullets.spawnBullet(player_pos, mouse_pos)
                    self.time_since_last_shot = 0  

            self.bullets.update(dt,self.camera.offset, WINDOW_WIDTH, WINDOW_HEIGHT)

            #Enemy bullet collider 
            for bullet in self.bullets.bullets[:]:
                for enemy in self.enemies[:]:
                    if bullet.bulletRect.colliderect(enemy.enemyRect):
                        self.bullets.bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        #---
                        # while True:
                        #     x = randint(-100, 1400)
                        #     y = randint(-500, 1500)
                        #     spawn_rect = pygame.Rect(x, y, 50, 50) 
                        #     if not self.level.restrictedAreaSpawn.colliderect(spawn_rect):
                        #         break 
                        # self.enemies.append(Enemy((x, y)))
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
            self.level.displayLevel(self.camera.offset, self.camera.viewport_rect)
            # Display Objects
            self.camera.display_objects(self.enemies, self.bullets, self.player, self.playerUi, self.level.tileWalls, dt)
            pygame.display.flip()
        
        pygame.quit()
if __name__ == "__main__":
    game = Main()   
    game.run()
