import pygame

from entity.player import Player
from entity.bullet import Bullet
"""
    TODO: CREATE BULLET MANAGER
        : CREATE ENEMY WITH BULLET COLLISION 
        : CONE SHAPE RANDOM BULLET SPREAD
"""
class Main():
    def __init__(self):
        pygame.init()      
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 720, 480
        
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Init character
        self.player = Player((self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2))
        
        self.bullets = []
        self.fire_rate = 0.5  
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
                    self.bullets.append(Bullet(player_pos, mouse_pos))
                    self.time_since_last_shot = 0  

            for bullet in self.bullets[:]:  
                bullet.update(dt)
                if bullet.is_offscreen(self.WINDOW_WIDTH, self.WINDOW_HEIGHT): 
                    self.bullets.remove(bullet)
            if(self.time_since_last_shot > 10):
                self.time_since_last_shot = 0

            self.screen.fill("white")
            self.player.display(self.screen, dt)
            for bullet in self.bullets:
                bullet.display(self.screen)
            pygame.display.flip()
        
        pygame.quit()
