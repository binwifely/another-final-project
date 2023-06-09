from pygame import*
from random import random, shuffle
from button import Button
from sprite import Vehicle
from sprite import Player

markers_move_change = 20
markers_move_y = 0
bg_width = 600
bg_height = 600
road_width = 400
road_height = 600
screen_size = (bg_width, bg_height)
screen = display.set_mode(screen_size)
display.set_caption('race')

#colors

gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
yellow = (255, 232, 0)
white = (255, 255, 255)
black = (0, 0, 0)

colors = [gray, green, yellow, white, black, red]

#game

gameover = False
speed = 2
score = 0

#road markers size

marker_width = 10
marker_height = 50

road = (100, 0, road_width, road_height)
left_edge_marker = (90, 0, marker_width, road_height)
right_edge_marker = (500, 0, marker_width, road_height)

#road lanes
class Line:
    def __init__(self, x, start_y):
        self.rects = []
        self.start_y = start_y 

        for i in range(14):
            rect = Rect(x, self.start_y, 10, 50)
            self.start_y += 150
            self.rects.append(rect)

    def draw(self):
        for r in self.rects:
            draw.rect(screen, white, r)
            r.y += 0
            if r.y >= 680:
                r.y = -230


lane1 = 150
lane2 = 250
lane3 = 350
lane4 = 450

lanes = [lane1, lane2, lane3, lane4]

line_a = Line(lane1 + 50, -80)
line_b = Line(lane2 + 50, -80)
line_c = Line(lane3 + 50, -80)

'''lines = sprite.Group()
lines.add(line_a, line_b, line_c)'''
#creating player

x_list = [150, 250, 350, 450]
choose_x = [0, 1, 2, 3]
shuffle(choose_x)
player_y = 400

player = Player('car.png', x_list[choose_x[0]], player_y)

#game initialization

clock = time.Clock()
fps = 120
run = True


#ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
#ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss


while run:

    clock.tick(fps)

    for i in event.get():
        if i.type == QUIT:
            run = False

    #draw the background

    screen.fill(green)
    draw.rect(screen, gray, road)
    draw.rect(screen, yellow, left_edge_marker)
    draw.rect(screen, yellow, right_edge_marker)

    #draw lane markers


    line_a.draw()
    line_b.draw()
    line_c.draw()

    player.draw(screen)

    display.update()