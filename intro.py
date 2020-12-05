DEBUG = False

WIDTH = 400
HEIGHT = 400

snake = Actor('snake_head.png') # an array of actors
direction = 2 # 0=left 1=up 2=right 3=down

def draw():
    screen.clear()
    snake.draw()

def update():
    move_snake()
    
def move_snake():
    if direction == 0:    # left
        snake.right -= 2 
    elif direction == 1:  # up
        snake.top -= 2
    elif direction == 2:  # right
        snake.right += 2
    else:                 # down
        snake.top += 2


def on_key_down(key):
    global direction
    
    if key == keys.LEFT:     # left
        direction = 0
        dprint("pressed key: LEFT")
    elif key == keys.UP:     # up
        direction = 1
        dprint("pressed key: UP")
    elif key == keys.RIGHT:  # right
        direction = 2
        dprint("pressed key: RIGHT")
    elif key == keys.DOWN:   # down
        direction = 3
        dprint("pressed key: DOWN")
    
    dprint(direction)

# print msg in debug mode
def dprint(msg):
    if DEBUG :
        print(msg)

