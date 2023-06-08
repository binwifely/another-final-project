from pygame import*
from random import random, shuffle
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

#road lines

lane1 = 150
lane2 = 250
lane3 = 350
lane4 = 450

lanes = [lane1, lane2, lane3, lane4]

#creating player

players = sprite.Group()

x_list = [150, 250, 350, 450]
choose_x = [0, 1, 2, 3]
shuffle(choose_x)
player_y = 500

player = Player(x_list[choose_x[0]], player_y)
players.add(player)
#game initialization

clock = time.Clock()
fps = 120
run = True
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
    markers_move_y += speed * 2
    if markers_move_y >= marker_height * 14:
        markers_move_y = 30
    for y in range(-marker_height + markers_move_change, marker_height - markers_move_change):

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y, marker_width, marker_height))
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y + 150, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y + 150, marker_width, marker_height))
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y + 150, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y + 300, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y + 300, marker_width, marker_height)) 
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y + 300, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y + 450, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y + 450, marker_width, marker_height)) 
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y + 450, marker_width, marker_height))  

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y + 600, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y + 600, marker_width, marker_height)) 
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y + 600, marker_width, marker_height))               

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y - 150, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y - 150, marker_width, marker_height))
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y - 150, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y - 300, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y - 300, marker_width, marker_height)) 
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y - 300, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y - 450, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y - 450, marker_width, marker_height)) 
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y - 450, marker_width, marker_height))

        draw.rect(screen, white, (lane1 + 45, y + markers_move_y - 600, marker_width, marker_height))
        draw.rect(screen, white, (lane2 + 45, y + markers_move_y - 600, marker_width, marker_height))
        draw.rect(screen, white, (lane3 + 45, y + markers_move_y - 600, marker_width, marker_height))


        players.draw(screen)
        
    display.update()