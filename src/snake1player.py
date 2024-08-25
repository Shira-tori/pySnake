import pygame 


class SnakeGame:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True


    def checkEvents(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


    def quit(self):
        pygame.quit()
        exit()


    def run(self) -> None:
        while self.running:
            self.checkEvents()
            self.screen.fill(color='black')
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000
        

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
