from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():

    r, cx, cy = 300, 800 // 2, 600 // 2

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        clear_canvas_now()
        character.draw_now(x, y)
        delay(0.01)

def run_top():
    print('Top')
    pass

def run_right():
    print('Right')
    pass

def run_bottom():
    print('bottom')
    pass

def run_left():
    print('Left')
    pass
   
def run_rectangle():
    
    run_top()
    run_right()
    run_bottom()
    run_left()

while True:
    #run_circle()
    run_rectangle()
    break;

close_canvas()

    
