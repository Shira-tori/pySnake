import random
import pygame
import snake


class Food:
    

    def __init__(self,
                 size: int,
                 snake: snake.Snake,
                 DISPLAY: tuple,
                 DISPLAY_SIZE: tuple
                 ) -> None:
        random.seed()
        x = random.randrange(DISPLAY[0], DISPLAY[0] + DISPLAY_SIZE[0], size)
        y = random.randrange(DISPLAY[1], DISPLAY[1] + DISPLAY_SIZE[1], size)
        self.display = DISPLAY
        self.display_size = DISPLAY_SIZE
        self.size = size
        self.rect = pygame.Rect(x, y, size, size)


    def renderFood(self, screen: pygame.Surface):
        pygame.draw.rect(screen, 'red', self.rect, self.rect.width)

    
    def changePos(self, snake: snake.Snake):
        self.rect.x = random.randrange(self.display[0], 
                                       self.display[0] + 
                                       self.display_size[0], self.size)
        self.rect.y = random.randrange(self.display[1], 
                                       self.display[1] + 
                                       self.display_size[1], self.size)
        for i in snake.body.bodies:
            if (i.rect.x == self.rect.x and i.rect.y == self.rect.y):
                self.changePos(snake)
