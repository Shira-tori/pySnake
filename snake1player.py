import pygame, sys, random
from pygame.locals import *

class SnakeHead:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.Xs = 1
        self.Ys = 0
        self.headLastPosX = 0
        self.headLastPosY = 0

class SnakeBody:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, x, y):
        self.head = SnakeHead(x, y)
        self.length = 2
        self.size = 20
        self.body = []
        for i in range(self.length):
            self.body.append(SnakeBody(0, 0))

class Food:
    def __init__(self, x, y):
        self.fx = x
        self.fy = y 

def initialize():
    pygame.init()
    random.seed()
    pygame.font.init()

    global SCREEN
    global screen
    global black
    global red
    global snake
    global food
    global my_font

    SCREEN = 640, 480
    screen = pygame.display.set_mode(SCREEN)
    snake = Snake(20, 0)
    my_font = pygame.font.Font("Silverfinster-x3L2K.ttf", 30)
    food = Food(random.randrange(0, 620, 20), random.randrange(0, 460, 20))
    black = 0, 0, 0
    red = 255, 0 ,0

    if(screen == None):
        print("Failed to create screen. " + pygame.get_error())
        sys.exit(1)

    return True

def shutdown():
    pygame.quit()

def render_snake():
    snakeHeadImage = pygame.image.load("head.png")
    snakeBodyImage = pygame.image.load("body.png")
    snakeBody = []
    if snake.head.Xs == 1:
        snakeHead = pygame.transform.rotate(snakeHeadImage, 0)
    if snake.head.Xs == -1:
        snakeHead = pygame.transform.rotate(snakeHeadImage, 180)
    if snake.head.Ys == -1:
        snakeHead = pygame.transform.rotate(snakeHeadImage, 90)
    if snake.head.Ys == 1:
        snakeHead = pygame.transform.rotate(snakeHeadImage, -90)
    screen.blit(snakeHead, (snake.head.x, snake.head.y))
    for i in range(snake.length):
        if snake.head.Xs == 1:
            snakeBody.append(pygame.transform.rotate(snakeBodyImage, 0))
        if snake.head.Xs == -1:
            snakeBody.append(pygame.transform.rotate(snakeBodyImage, 180))
        if snake.head.Ys == -1:
            snakeBody.append(pygame.transform.rotate(snakeBodyImage, 90))
        if snake.head.Ys == 1:
            snakeBody.append(pygame.transform.rotate(snakeBodyImage, -90))
        screen.blit(snakeBody[i], (snake.body[i].x, snake.body[i].y))
        


def move():
    for i in reversed(range(snake.length)):
        if i == 0:
            snake.body[i].x = snake.head.headLastPosX
            snake.body[i].y = snake.head.headLastPosY
            break
        snake.body[i].x = snake.body[i-1].x
        snake.body[i].y = snake.body[i-1].y

    snake.head.x += snake.head.Xs*snake.size
    snake.head.y += snake.head.Ys*snake.size
    if snake.head.x > SCREEN[0]-snake.size:
        snake.head.x = 0
    if snake.head.x < 0:
        snake.head.x = SCREEN[0]-snake.size
    if snake.head.y > SCREEN[1]-snake.size:
        snake.head.y = 0
    if snake.head.y < 0:
        snake.head.y = SCREEN[1]-snake.size
    snake.head.headLastPosX = snake.head.x
    snake.head.headLastPosY = snake.head.y

def render_food():
    foodImage = pygame.image.load('food.png')
    screen.blit(foodImage, (food.fx, food.fy))
    if snake.head.x == food.fx and snake.head.y == food.fy:
        food.fx = random.randrange(0, 620, 20)
        food.fy = random.randrange(0, 460, 20)
        for i in range(snake.length):
            while food.fx == snake.body[i].x and food.fy == snake.body[i].y:
                food.fx = random.randrange(0, 620, 20)
                food.fy = random.randrange(0, 460, 20)
        snake.length+=1
        snake.body.append(SnakeBody(snake.body[snake.length-2].x, snake.body[snake.length-2].y))            

def game_over():
    for i in range(snake.length):
        if snake.head.x == snake.body[i].x and snake.head.y == snake.body[i].y:
            lasttick = pygame.time.get_ticks()
            bgImage = pygame.image.load("bg.png")
            gameOver = my_font.render("GAME OVER", False, (0, 0, 0))
            gameOverScaled = pygame.transform.scale(gameOver, (300, 100))
            retry = my_font.render("RETRY", False, (0, 0, 0))
            retryButton = retry.get_rect()
            retryButton.x = SCREEN[0]/2 - retry.get_width()/2 - 2
            retryButton.y = 300
            exitB = my_font.render("EXIT", False, (0, 0, 0))
            exitButton = exitB.get_rect()
            exitButton.x = SCREEN[0]/2 - exitB.get_width()/2 - 2
            exitButton.y = 350
            score = my_font.render("SCORE: " + str(snake.length-2), False, (0, 0, 0))
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mousePos = pygame.mouse.get_pos()
                            if retryButton.collidepoint(mousePos):
                                initialize()
                                game_loop()
                            if exitButton.collidepoint(mousePos):
                                pygame.quit()
                                sys.exit(0)
                                

                curtick = pygame.time.get_ticks()
                if curtick == lasttick + 200:
                    screen.blit(bgImage, (0,0))
                    screen.blit(gameOverScaled, (SCREEN[0]/2 - gameOverScaled.get_width()/2, 50))
                    screen.blit(score, (SCREEN[0]/2 - score.get_width()/2, 200))
                    pygame.draw.rect(screen, (255, 255, 255), retryButton)
                    screen.blit(retry, (SCREEN[0]/2 - retry.get_width()/2, 300))
                    screen.blit(exitB, (SCREEN[0]/2 - exitB.get_width()/2, 350))
                    pygame.display.update()
                    


def game_loop():
    lasttick = pygame.time.get_ticks()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if snake.head.x+20 == snake.body[0].x:
                        snake.head.Xs = -1
                        snake.head.Ys = 0
                        break
                    snake.head.Xs = 1
                    snake.head.Ys = 0
                if event.key == K_LEFT:
                    if snake.head.x-20 == snake.body[0].x:
                        snake.head.Xs = 1
                        snake.head.Ys = 0
                        break
                    snake.head.Xs = -1
                    snake.head.Ys = 0
                if event.key == K_UP:
                    if snake.head.y-20 == snake.body[0].y:
                        snake.head.Xs = 0
                        snake.head.Ys = 1
                        break
                    snake.head.Xs = 0
                    snake.head.Ys = -1
                if event.key == K_DOWN:
                    if snake.head.y+20 == snake.body[0].y:
                        snake.head.Xs = 0
                        snake.head.Ys = -1
                        break
                    snake.head.Xs = 0
                    snake.head.Ys = 1
                if event.key == 27:
                    pause()
                    break

        bgImage = pygame.image.load("bg.png")
        screen.blit(bgImage, (0, 0))
        render_snake()
        render_food()
        curtick = pygame.time.get_ticks()
        if curtick > lasttick + 100:
            move()
            lasttick = curtick
        game_over()
        pygame.display.update()

def pause():
    running = True
    bgImage = pygame.image.load("bg.png")
    pausedImage = pygame.image.load("paused.png")
    pausedImageScaled = pygame.transform.scale(pausedImage, (300, 100))
    resumeImage = pygame.image.load("resume.png")
    resumeButton = resumeImage.get_rect()
    resumeButton.x = SCREEN[0]/2 - resumeImage.get_width()/2
    resumeButton.y = 200   
    exitImage = pygame.image.load("exit.png")
    exitButton = exitImage.get_rect()
    exitButton.x = 270
    exitButton.y = 300
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYDOWN:
                if event.key == 27:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if resumeButton.collidepoint(mousePos):
                        running = False
                        break
                    if exitButton.collidepoint(mousePos):
                        pygame.quit()
                        sys.exit(0)
                        break
        screen.fill((0,0,0))
        screen.blit(bgImage, (0,0))
        screen.blit(pausedImageScaled, ((SCREEN[0]/2)-(pausedImageScaled.get_width()/2), 50))
        pygame.draw.rect(screen, (255, 255, 255), resumeButton)
        screen.blit(resumeImage, (resumeButton.x, resumeButton.y))
        pygame.draw.rect(screen, (255, 255, 255), exitButton)
        screen.blit(exitImage, (exitButton.x, exitButton.y))
        pygame.display.update()
        
            

def main_menu():
    running = True
    playImage = pygame.image.load("play.png")
    snakeImage = pygame.image.load("snake.png")
    snakeImageScaled = pygame.transform.scale(snakeImage, (300, 100))
    bgImage = pygame.image.load("bg.png")
    playButton = playImage.get_rect()
    playButton.x = 270
    playButton.y = 200
    exitImage = pygame.image.load("exit.png")
    exitButton = exitImage.get_rect()
    exitButton.x = 270
    exitButton.y = 300
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if playButton.collidepoint(mousePos):
                        running = False
                    if exitButton.collidepoint(mousePos):
                        pygame.quit()
                        sys.exit(0)


        screen.blit(bgImage, (0, 0))
        screen.blit(snakeImageScaled, ((SCREEN[0]/2)-(snakeImageScaled.get_width()/2), 50))
        pygame.draw.rect(screen, (255, 255, 255), playButton)
        screen.blit(playImage, (270, 200))
        pygame.draw.rect(screen, (255, 255, 255), exitButton)
        screen.blit(exitImage, (exitButton.x, exitButton.y))
        pygame.display.update()

def main():
    if(initialize() == False):
        shutdown()
        sys.exit(1)
    
    main_menu()

    game_loop()

main()


    