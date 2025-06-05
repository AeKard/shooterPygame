import pygame
from random import choice
from entity.enemy import Enemy
class LevelManager:
    def __init__(self, floorPos, playableArea):
        self.playableArea = pygame.math.Vector2(playableArea)
        self.displaySurface = pygame.display.get_surface()
        self.restrictedAreaSpawn = pygame.Rect((self.displaySurface.get_size()[0]/2)/2, (self.displaySurface.get_size()[1]/2)/2, 720, 720)
        self.floor = pygame.Surface(self.playableArea)
        self.floorRect = self.floor.get_rect(center = floorPos)
        self.floor.fill((30, 141, 28))
        self.tileMap = self.createTileMap()
        self.tileWalls = self.generate_wall_rects()
    
    def createTileMap(self): # Tile map created "create logic here for random generation"
        self.tilemap = []
        playableAreaY = int(self.playableArea.y // 40) # do the tile setup for sizes
        playableAreaX = int(self.playableArea.x // 30)
        for x in range(playableAreaX):
            row = []
            for y in range(playableAreaY):
                if x == 0 or x == playableAreaX - 1 or y == 0 or y == playableAreaY - 1:
                    row.append(1)
                else:
                    row.append(0)
            self.tilemap.append(row)
        return self.tilemap 
    
    def drawWall(self, offset, viewport):
        tileSize = pygame.math.Vector2((30,40))
        tilemap = self.tileMap
        for y, row in enumerate(tilemap):
            for x, tile in enumerate(row):
               if(tile == 1):
                    # print(self.floorRect.left, self.floorRect.top)
                    world_x = self.floorRect.left + x * tileSize[0]
                    world_y = self.floorRect.top + y * tileSize[1]
                    world_rect = pygame.Rect(world_x, world_y, tileSize[0], tileSize[1])
                    if viewport.colliderect(world_rect):
                        screen_pos = (world_rect.x - offset.x, world_rect.y - offset.y)
                        pygame.draw.rect(self.displaySurface, "orange", pygame.Rect(screen_pos, (tileSize.x, tileSize.y)))
    
    def generate_wall_rects(self):
        tileSize = (30, 40)
        wall_rects = []
        for y, row in enumerate(self.tileMap):
            for x, tile in enumerate(row):
                if tile == 1:  # Wall tile
                    world_x = self.floorRect.left + x * tileSize[0]
                    world_y = self.floorRect.top + y * tileSize[1]
                    wall_rect = pygame.Rect(world_x, world_y, tileSize[0], tileSize[1])
                    wall_rects.append(wall_rect)
        return wall_rects
    def setupEnemy(self):
        tileSize = (30, 40)
        valid_tiles = []

        for y, row in enumerate(self.tileMap):
            for x, tile in enumerate(row):
                if tile == 0:
                    world_x = self.floorRect.left + x * tileSize[0]
                    world_y = self.floorRect.top + y * tileSize[1]
                    spawn_rect = pygame.Rect(world_x, world_y, 50, 50) 
                    if not self.restrictedAreaSpawn.colliderect(spawn_rect):
                        valid_tiles.append((world_x, world_y))
        enemies = []
        placed_rects = []
        for _ in range(200):
            if not valid_tiles:
                break

            x, y = choice(valid_tiles)
            new_rect = pygame.Rect(x, y, 50, 50)

            collision = any(new_rect.colliderect(r) for r in placed_rects)
            if collision:
                valid_tiles.remove((x, y))
                continue

            enemies.append(Enemy((x, y)))
            placed_rects.append(new_rect)
            valid_tiles.remove((x, y))  

        return enemies
    
    def displayLevel(self,offset, viewport):
        self.displaySurface.blit(self.floor,self.floorRect.topleft - offset)
        self.drawWall(offset,viewport)
