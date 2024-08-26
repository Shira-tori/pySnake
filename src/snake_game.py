import pygame 
import snake

DISPLAY = (1280, 720)
SNAKE_SIZE = 20
STARTING_LENGTH = 3

class SnakeGame:


    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY)
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake1 = snake.Snake(0, 0, 
                                  SNAKE_SIZE, STARTING_LENGTH,
                                  [20, 0]
                                  )


    def checkEvents(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


    def quit(self) -> None:
        pygame.quit()
        exit()


    def run(self) -> None:
        while self.running:
            self.checkEvents()
            self.screen.fill(color='black')
            self.snake1.renderSnake(self.screen)
            pygame.display.flip()
            print(self.clock.tick(10))
            self.snake1.moveSnake()
        

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
