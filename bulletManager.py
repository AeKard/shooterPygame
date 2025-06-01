from entity.bullet import Bullet

class BulletManager:
    def __init__(self):
        self.bullets = []

    def spawnBullet(self, pos, targerPos):
        self.bullets.append(Bullet(pos, targerPos))
    
    def update(self, dt, offset, screen_width, screen_height):
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if bullet.is_offscreen(offset, screen_width, screen_height): 
                    self.bullets.remove(bullet)

    def draw(self, offset):
        for bullet in self.bullets:
            bullet.display(offset)
