import pygame


class Body:


    def __init__(self, 
                x: int, 
                y: int, 
                size: int
               ) -> None:
        self.rect = pygame.Rect(x, y, size, size)


class SnakeHead:

    
    def __init__(self, 
                 x: int, 
                 y: int, 
                 size: int
                ) -> None:
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size

    def moveHead(self, speed: list[int]) -> None:
        self.rect = self.rect.move(speed[0], speed[1])


class SnakeBody:


    def __init__(self, 
                 length: int, 
                 size: int, 
                 head: SnakeHead
                ) -> None:
        self.length = length
        self.size = size
        self.head = head
        self.bodies = list()
        last_pos = list()
        for i in range(length):
            if i == 0:
                self.bodies.append(Body(head.rect.x - size, head.rect.y, size))
                last_pos = [self.bodies[i].rect.x, self.bodies[i].rect.y]
                continue
            self.bodies.append(Body(last_pos[0] - size, last_pos[1], size))


    def moveBody(self) -> None:
        last_pos = list()
        for i in range(self.length):
            if i == 0:
                last_pos = [self.bodies[i].rect.x, self.bodies[i].rect.y]
                self.bodies[i].rect.x = self.head.rect.x
                self.bodies[i].rect.y = self.head.rect.y
                continue
            self.bodies[i].rect.x = last_pos[0]
            self.bodies[i].rect.y = last_pos[1]


class Snake:
    

    def __init__(self, 
                 x: int, 
                 y: int, 
                 size: int, 
                 length: int, 
                 speed: list[int]
                ) -> None:
        self.head = SnakeHead(x, y, size)
        self.body = SnakeBody(length, size, self.head)
        self.speed = speed
        self.size = size


    def renderSnake(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, 'green', self.head.rect, self.size)
        for body in self.body.bodies:
            pygame.draw.rect(screen, 'green', body.rect, self.size)


    def moveSnake(self) -> None:
        self.body.moveBody()
        self.head.moveHead(self.speed)
        pass
