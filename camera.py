import pygame

class Camera:
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.displaySurface.get_size()[0] // 2
        self.half_h = self.displaySurface.get_size()[1] // 2

        self.viewport_rect = pygame.Rect(
           self.offset.x,
           self.offset.y,
           self.displaySurface.get_size()[0],
           self.displaySurface.get_size()[1]
        )  

    def center_target_camera(self, target):
        self.offset.x = target.characterRect.centerx - self.half_w
        self.offset.y = target.characterRect.centery - self.half_h

    def display_objects(self, enemies, bullets, player, playerUi,levelWalls,dt):
        #updates the viewport offset
        self.center_target_camera(player)
        self.viewport_rect.topleft = self.offset
        # self.displaySurface.blit(player.character, player.characterRect)
        player.display(self.offset, levelWalls, dt)
        bullets.draw(self.offset)
        # print(player.characterRect)
        
        #display enemies if in the viewport
        for enemy in enemies:
            enemy.enemyMovement(player.characterRect.center, dt, enemies, levelWalls)
            if self.viewport_rect.colliderect(enemy.enemyRect):
                enemy.display(self.offset)
        #diplay health
        margin = pygame.math.Vector2()
        if player.health > 0:
            for i in range(player.health):
                playerUi.drawUI(margin)
                margin.x += 40


