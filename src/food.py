import random
import pygame
import snake


class Food:
    

    def __init__(self,
                 size: int,
                 snake: snake.Snake,
                 DISPLAY: tuple
                 ) -> None:
        random.seed()
        x = random.randrange(0, DISPLAY[0], size)
        y = random.randrange(0, DISPLAY[1], size)
        self.display = DISPLAY
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)


    def renderFood(self, screen: pygame.Surface):
        pygame.draw.rect(screen, 'red', self.rect, self.rect.width)

    
    def changePos(self, snake: snake.Snake):
        self.rect.x = random.randrange(0, self.display[0], self.size)
        self.rect.y = random.randrange(0, self.display[1], self.size)
#        snake_pos_x = list()
#        snake_pos_y = list()
#        for i in snake.body.bodies:
#            snake_pos_x.append(i.rect.x)
#            snake_pos_y.append(i.rect.y)


        pass

