import food
import pygame 
import random
import snake

DISPLAY = (1280, 720)
PLAY_AREA_SIZE = (1000, 600)
PLAY_AREA = (DISPLAY[0]/2 - PLAY_AREA_SIZE[0]/2, 
             DISPLAY[1]/2 - PLAY_AREA_SIZE[1]/2)
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
                              PLAY_AREA,
                              PLAY_AREA_SIZE)


    def checkEvents(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()


    def quit(self) -> None:
        pygame.quit()
        exit()

    def handleInput(self, keys_: list[str]) -> str:
        if len(keys_) > 2:
            return ''
        keys_pressed = str()
        keys = pygame.key.get_pressed()
        if ((keys[pygame.K_d] or keys[pygame.K_RIGHT]) and
            self.snake1.speed != [-20, 0]):
            keys_pressed = 'right'
        if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) and
            self.snake1.speed != [20, 0]):
            keys_pressed = 'left'
        if ((keys[pygame.K_w] or keys[pygame.K_UP]) and 
            self.snake1.speed != [0, 20]):
            keys_pressed = 'up'
        if ((keys[pygame.K_s] or keys[pygame.K_DOWN]) and
            self.snake1.speed != [0, -20]):
            keys_pressed = 'down'

        return keys_pressed


    def run(self) -> None:
        miliseconds = int()
        keys_pressed = list()
        while self.running:
            self.checkEvents()
            keys = self.handleInput(keys_pressed)
            if keys and keys not in keys_pressed: keys_pressed.append(keys)
            if len(keys_pressed) > 2: keys_pressed.pop()
            print(keys_pressed)
            self.screen.fill(color='grey')
            play_area = pygame.Rect(PLAY_AREA[0], 
                                    PLAY_AREA[1], 
                                    PLAY_AREA_SIZE[0], 
                                    PLAY_AREA_SIZE[1])
            pygame.draw.rect(self.screen, 'black', play_area)            
            self.snake1.renderSnake(self.screen)
            self.food.renderFood(self.screen)
            pygame.display.flip()
            self.snake1.handleInput(keys_pressed)
            if miliseconds >= 100:
                self.snake1.moveSnake(self.food)
                miliseconds = 0
                continue
            miliseconds += self.clock.tick()
        

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()
