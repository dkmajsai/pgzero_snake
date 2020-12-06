DEBUG = False

WIDTH = 400
HEIGHT = 400

snake = [Actor('snake_head.png', topleft=(40,20))] # an array of actors
snake.append(Actor('snake_body.png', topleft=(20,20)))
snake.append(Actor('snake_tail.png', topleft=(0,20)))

direction = 2 # 0=left 1=up 2=right 3=down
snake_step = 20

cframe = 0  # global counter to count frames
speed = 10  # will be speed / 60

def draw():
    screen.clear()
    
    # draw snake
    for actor in snake:
        actor.draw()

# this function is called 60 times a second
def update():
    global cframe
    global speed

    # adjust movement according to speed
    if cframe == speed:
        move_snake()
        cframe = 0
    else:
        cframe += 1
    
def move_snake():
    global snake_step
    
    # move tail and body
    for i in range(len(snake)-1, 0, -1):
        dprint(i)
        bodypart = snake[i]
        bodypart_before = snake[i-1]
        bodypart.center = bodypart_before.center
    
    # move the head
    if direction == 0:    # left
        snake[0].right -= snake_step 
    elif direction == 1:  # up
        snake[0].top -= snake_step
    elif direction == 2:  # right
        snake[0].right += snake_step
    else:                 # down
        snake[0].top += snake_step


def on_key_down(key):
    global direction
    
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

# print msg in debug mode
def dprint(msg):
    if DEBUG :
        print(msg)

