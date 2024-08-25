import pygame 
import snake

DISPLAY = (1280, 720)
SNAKE_SIZE = 20
STARTING_LENGTH = 3

class SnakeGame:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY)
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake1 = snake.Snake(20, 20, SNAKE_SIZE, STARTING_LENGTH)


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
            self.snake1.renderSnake(self.screen)
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000
        

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
