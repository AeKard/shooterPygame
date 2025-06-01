import pygame
class Camera:
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()

        self.half_w = self.displaySurface.get_size()[0] // 2
        self.half_h = self.displaySurface.get_size()[1] // 2

    def center_target_camera(self, target):
        self.offset.x = target.characterRect.centerx - self.half_w
        self.offset.y = target.characterRect.centery - self.half_h

    def display_objects(self, enemies, bullets, player):
        self.center_target_camera(player)
        # self.displaySurface.blit(player.character, player.characterRect)
        player.display(self.offset)
        bullets.draw(self.offset)
        # print(self.offset.x , self.offset.y)
        for enemy in enemies:
            enemy.display(self.offset)

    #Create a way to diplay everything here    

