import food
import pygame 
import random
import snake

DISPLAY = (1280, 720)
SNAKE_SIZE = 20
STARTING_LENGTH = 4

class SnakeGame:


    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY)
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake1 = snake.Snake(0, 0, 
                                  SNAKE_SIZE, 
                                  STARTING_LENGTH,
                                  [20, 0]
                                  )
        self.food = food.Food(SNAKE_SIZE, 
                              self.snake1,
                              DISPLAY)


    def checkEvents(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


    def quit(self) -> None:
        pygame.quit()
        exit()

    # Fix snake can turn into itself and going out of bounds.
    def handleInput(self) -> None:
        keys = pygame.key.get_pressed()
        if ((keys[pygame.K_d] or keys[pygame.K_RIGHT]) and
            self.snake1.speed != [-20, 0]):
            self.snake1.speed = [20, 0]
        elif ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and
            self.snake1.speed != [20, 0]):
            self.snake1.speed = [-20, 0]
        elif ((keys[pygame.K_w] or keys[pygame.K_UP]) and 
            self.snake1.speed != [0, 20]):
            self.snake1.speed = [0, -20]
        elif ((keys[pygame.K_s] or keys[pygame.K_DOWN]) and
            self.snake1.speed != [0, -20]):
            self.snake1.speed = [0, 20]


    def run(self) -> None:
        miliseconds = int()
        while self.running:
            self.checkEvents()
            self.handleInput()
            self.screen.fill(color='black')
            self.snake1.renderSnake(self.screen)
            self.food.renderFood(self.screen)
            pygame.display.flip()
            if miliseconds >= 100:
                self.snake1.moveSnake(self.food)
                miliseconds = 0
                continue
            miliseconds += self.clock.tick()
        

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
