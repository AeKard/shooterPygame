from entity.bullet import Bullet

class BulletManager:
    def __init__(self):
        self.bullets = []

    def spawnBullet(self, pos, targerPos):
        self.bullets.append(Bullet(pos, targerPos))
    
    def update(self, dt, screen_width, screen_height):
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if bullet.is_offscreen(screen_width, screen_height): 
                    self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.display(screen)
