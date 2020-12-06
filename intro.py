import pgzrun
import random

DEBUG = False
WIDTH = 400
HEIGHT = 400

snake = []
walls = []
apples = []

COLOR_WALL = (0, 0, 0)
COLOR_BACKGROUND = (255, 255, 255)

extend_snake = False
snake_collision = False

direction = 2 # 0=left 1=up 2=right 3=down
snake_step = 20

cframe = 0  # global counter to count frames
speed = 10  # will be speed / 60

def add_apple():
    range_x = (WIDTH / 20) - 1
    range_y = (HEIGHT / 20) - 1
    
    apple = ''
    while(True):
        apple = Actor("apple", topleft=(random.randint(0, range_x) * 20, random.randint(0, range_y) * 20))
        
        # check if that collids with anything existing
        if apple.collidelist(walls) is not -1: continue
        if apple.collidelist(snake) is not -1: continue
        
        break
    
    apples.append(apple)

def init():
    global snake, walls, apples, extend_snake, snake_collision, direction
    
    snake = [Actor('snake_head.png', topleft=(40,20))] # an array of actors
    snake.append(Actor('snake_body.png', topleft=(20,20)))
    snake.append(Actor('snake_tail.png', topleft=(0,20)))

    walls = []
    walls.append(Rect((0, 0), (20, HEIGHT)))            # LEFT
    walls.append(Rect((0, 0), (WIDTH, 20)))             # TOP
    walls.append(Rect((WIDTH - 20, 0), (20, HEIGHT)))   # RIGHT
    walls.append(Rect((0, HEIGHT - 20), (WIDTH, 20)))   # BOTTOM
    
    apples.clear()
    add_apple()
    
    extend_snake = False
    snake_collision = False
    direction = 2 # 0=left 1=up 2=right 3=down

init() # must be called here after it is declared

def draw():
    global snake, walls

    # clear all from sceen
    screen.clear()
    
    screen.fill(COLOR_BACKGROUND)
    
    # draw walls
    for wall in walls:
        screen.draw.filled_rect(wall, COLOR_WALL)
        
    # draw apples
    for apple in apples:
        apple.draw()
    
    # draw snake ==> draw head last
    for i in range(len(snake) - 1, -1 , -1):
        snake[i].draw()

# this function is called 60 times a second
def update():
    global cframe, speed, snake_collision

    if snake_collision: return

    # adjust movement according to speed
    if cframe == speed:
        move_snake()
        cframe = 0
    else:
        cframe += 1
    
def move_snake():
    global snake_step, extend_snake
    
    snake_head = snake[0]
    
    # if snake needs to be extended, do not move the body,
    # extend it with one bodypart after the head
    
    # move tail and body if snake is not extending
    if not extend_snake:
        for i in range(len(snake)-1, 0, -1):
            bodypart = snake[i]
            bodypart_before = snake[i-1]
            bodypart.center = bodypart_before.center
            bodypart.angle = bodypart_before.angle
    
    # insert bodypart after the head at the current location of head
    if extend_snake:
        extend_snake = False
        new_bodypart = Actor('snake_body.png', center=snake_head.center)
        new_bodypart.angle = snake_head.angle
        snake.insert(1, new_bodypart)
    
    # move the head
    if direction == 0:    # left
        snake_head.right -= snake_step 
    elif direction == 1:  # up
        snake_head.top -= snake_step
    elif direction == 2:  # right
        snake_head.right += snake_step
    else:                 # down
        snake_head.top += snake_step
        
    check_collision()

def check_collision():
    global snake, snake_collision, extend_snake, apples
    
    snake_head = snake[0]
    
    # collison check with body and tail
    for i in range(1, len(snake)-1, 1):
        if snake_head.collidepoint(snake[i].center):
            snake_collision = True
            dprint('hit self')
            
    # collision check with the walls
    if snake_head.collidelist(walls) is not -1:
            snake_collision = True
            dprint('hit wall')

    # check if apple is catched
    apple_caught_idx = snake_head.collidelist(apples)
    if apple_caught_idx is not -1:
        extend_snake = True
        apples.pop(apple_caught_idx)
        add_apple()

def on_key_down(key):
    global direction, extend_snake, snake_collision
    
    if key == keys.LEFT:     # left
        if direction != 2:
            direction = 0
            snake[0].angle = 180
        dprint("pressed key: LEFT")
    elif key == keys.UP:     # up
        if direction != 3:
            direction = 1
            snake[0].angle = 90
        dprint("pressed key: UP")
    elif key == keys.RIGHT:  # right
        if direction != 0:
            direction = 2
            snake[0].angle = 0
        dprint("pressed key: RIGHT")
    elif key == keys.DOWN:   # down
        if direction != 1:
            direction = 3
            snake[0].angle = 270
        dprint("pressed key: DOWN")
    
    dprint(direction)
    
    if key == keys.R and snake_collision:
        init()
    
    # for debugging purpose
    if DEBUG:
        if key == keys.E:
            extend_snake = True
        
        if key == keys.A:
            add_apple()

# print msg in debug mode
def dprint(msg):
    if DEBUG :
        print(msg)

