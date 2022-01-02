import pygame, sys, random

random.seed()

class SnakeHead:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakeBody:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, x, y, size, length):
        self.head = SnakeHead(x, y)
        self.Xs = 1
        self.Ys = 0
        self.size = size
        self.length = length
        self.body = []
        for i in range(length):
            self.body.append(SnakeBody(0, 0))
        self.headLastPosX = 0
        self.headLastPosY = 0

class Food:
    def __init__(self):
        self.x = random.randrange(0, 620, 20)
        self.y = random.randrange(0, 460, 20)

def move():
    for i in reversed(range(snake.length)):
        if(i == 0):
            snake.body[i].x = snake.headLastPosX
            snake.body[i].y = snake.headLastPosY
            break
        snake.body[i].x = snake.body[i-1].x
        snake.body[i].y = snake.body[i-1].y
    if(snake.head.x < 0):
        snake.head.x = SCREEN[0]-20
    if(snake.head.x > SCREEN[0]-20):
        snake.head.x = 0
    snake.head.x += snake.Xs*snake.size
    snake.head.y += snake.Ys*snake.size
    snake.headLastPosX = snake.head.x
    snake.headLastPosY = snake.head.y

def render_snake():
    snakeHead = pygame.Rect(snake.head.x, snake.head.y, snake.size, snake.size)
    pygame.draw.rect(screen, red, snakeHead)
    
    snakeBody = []
    for i in range(snake.length):
        snakeBody.append(pygame.Rect(snake.body[i].x, snake.body[i].y, snake.size, snake.size))
        pygame.draw.rect(screen, blue, snakeBody[i])

def render_food():
    foodRect = pygame.Rect(food.x, food.y, snake.size, snake.size)
    pygame.draw.rect(screen, green, foodRect)
    if(snake.head.x == food.x and snake.head.y == food.y):
        food.x = random.randrange(0, 621, 20)
        food.y = random.randrange(0, 461, 20)
        snake.length+=1
        snake.body.append(SnakeBody(snake.body[snake.length-2].x, snake.body[snake.length-2].y))
        for i in range(snake.length):            
            while(snake.body[i].x == food.x or snake.body[i].y == food.y):
                food.x = random.randrange(0, 621, 20)
                food.y = random.randrange(0, 461, 20)      

def game_over():
    for i in range(snake.length):
        if(snake.head.x == snake.body[i].x and snake.head.y == snake.body[i].y):
            print("GAME OVER!!")
            pygame.quit()
            sys.exit(0)


if __name__ == '__main__':
    pygame.init()

    SCREEN = 640, 480
    snake = Snake(20, 0, 20, 2)
    food = Food()
    screen = pygame.display.set_mode(SCREEN)

    red = 255, 0, 0
    black = 0, 0, 0
    blue = 0, 0, 255
    green = 0, 255, 0
    lasttick = pygame.time.get_ticks()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if(snake.head.x+20 == snake.body[0].x):
                        snake.Xs = -1
                        snake.Ys = 0
                        break
                    snake.Xs = 1
                    snake.Ys = 0
                if event.key == pygame.K_LEFT:
                    if(snake.head.x-20 == snake.body[0].x):
                        snake.Xs = 1
                        snake.Ys = 0
                        break
                    snake.Xs = -1
                    snake.Ys = 0
                if event.key == pygame.K_UP:
                    if(snake.head.y-20 == snake.body[0].y):
                        snake.Xs = 0
                        snake.Ys = 1
                        break
                    snake.Xs = 0
                    snake.Ys = -1
                if event.key == pygame.K_DOWN:
                    if(snake.head.y+20 == snake.body[0].y):
                        snake.Xs = 0
                        snake.Ys = -1
                        break
                    snake.Xs = 0
                    snake.Ys = 1
                if event.key == pygame.K_w:
                    snake.length+=1
                    snake.body.append(SnakeBody(snake.body[snake.length-2].x, snake.body[snake.length-2].y))


        
        screen.fill((0, 0, 0))
        
        curtick = pygame.time.get_ticks()
        if curtick > lasttick + 100:
            move()
            lasttick = curtick

        render_snake()
        render_food()
        game_over()

        pygame.display.update()


