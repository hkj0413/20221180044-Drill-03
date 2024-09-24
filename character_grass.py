from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    r, cx, cy = 300, 800 // 2, 600 // 2

    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy

        draw_character(x, y)
        
def run_top():
    for x in range(50, 750, 10):
        draw_character(x, 550)

def run_right():
    for y in range(550, 50, -10):
        draw_character(750, y)

def run_bottom():
    for x in range(750, 50, -10):
        draw_character(x, 50)

def run_left():
    for y in range(50, 550, 10):
        draw_character(50, y)
   
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

    
