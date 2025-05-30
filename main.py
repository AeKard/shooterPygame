import pygame

from entity.player import Player

class main():
    def __init__(self):
        pygame.init()      
        self.WINDOW_HEIGHT, self.WINDOW_WIDTH = 720, 480
        
        self.screen = pygame.display.set_mode((self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        self.clock = pygame.time.Clock()
        self.running = True
        #Init characeter
        self.player = Player((self.WINDOW_HEIGHT / 2, self.WINDOW_WIDTH / 2))
    def gameLoop(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill("white")
            #display character
            self.player.display(self.screen,dt)
            pygame.display.flip()
        pygame.quit


if __name__ == "__main__":
    game = main()   
    game.gameLoop()
