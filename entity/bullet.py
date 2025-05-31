import pygame

class Bullet:
    def __init__(self, pos, target_pos):
        self.bullet = pygame.Surface((10,10))
        self.bullet.fill("yellow")
        self.bulletRect = self.bullet.get_rect(center = pos)

        direction_vector = pygame.math.Vector2(target_pos) - pygame.math.Vector2(pos)
        if direction_vector.length() != 0:
            self.direction = direction_vector.normalize()
        else:
            self.direction = pygame.math.Vector2(1, 0)
        
        self.speed = 500

    def update(self, dt):
        movement = self.direction * self.speed * dt
        self.bulletRect.center += movement
        
    def is_offscreen(self, screen_width, screen_height):
        return not self.bulletRect.colliderect(pygame.Rect(0, 0, screen_width, screen_height))
    
    def display(self, screen):
        screen.blit(self.bullet, self.bulletRect)
    
