import pygame


class SnakeHead:

    
    def __init__(self, x: int, y: int, size: int) -> None:
        self.pos_x = x
        self.pos_y = y
        self.size = size


class SnakeBody:


    def __init__(self, length: int, size: int, head: SnakeHead):
        self.length = length
        self.size = size
        self.head = head


class Snake:
    

    def __init__(self, x: int, y: int, size: int, length: int) -> None:
        self.head = SnakeHead(x, y, size)
        self.body = SnakeBody(length, size, self.head)


    def renderSnake(self, screen: pygame.Surface):
        snake_rect = pygame.Rect(
                self.head.size, self.head.size, 
                self.head.size, self.head.size
                )
        pygame.draw.rect(screen, 'green', snake_rect, 20)

