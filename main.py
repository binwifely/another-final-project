from pygame import*
from random import randint, shuffle
from button import Button
from sprite import Vehicle
from sprite import Player

bg_width = 800
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
scroll_speed = 2
enemy_speed = 3
score = 0

#road markers size

marker_width = 10
marker_height = 50

road = (200, 0, road_width, road_height)
left_edge_marker = (190, 0, marker_width, road_height)
right_edge_marker = (600, 0, marker_width, road_height)

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
            r.y += scroll_speed
            if r.y >= 680:
                r.y = -230


lane1 = 250
lane2 = 350
lane3 = 450
lane4 = 550

lanes = [lane1, lane2, lane3, lane4]

line_a = Line(lane1 + 50, -80)
line_b = Line(lane2 + 50, -80)
line_c = Line(lane3 + 50, -80)

#loading other cars

image_names = ['car1.png', 'car2.png']
car_images = []
for q in image_names:
    images = image.load(q)
    car_images.append(images)




crash = image.load('crash.png')
crash_rect = crash.get_rect()
#creating player

player_x_list = [210, 310, 410, 510]
x_list = [220, 320, 420, 520]
choose_x = [0, 1, 2, 3]
choose_xx = shuffle(choose_x)
player_y = 400

player = Player('car.png', player_x_list[choose_x[0]], player_y, 70, 120, 3)

#creating enemies


average_width = round((80+80+80+90) / 4)
average_height = round((150+150+200+170) / 4)
cars = sprite.Group()
car = Vehicle(image_names[randint(0, 1)], x_list[randint(0, 3)], -100, average_width, average_height, enemy_speed)
cars.add(car) 

#font initialization

font.init()
font = font.SysFont('Times New Roman', 40)

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


    #collision check

    for car in cars:
        if sprite.collide_rect(player, car):
            gameover = True
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:           
            crash_rect.center = [player.rect.left, (player.rect.center[1] + car.rect.center[1] / 2)]
        elif keys_pressed[K_d]:           
            crash_rect.center = [player.rect.right, (player.rect.center[1] + car.rect.center[1] / 2)]  

    #draw the background

    screen.fill(green)
    draw.rect(screen, gray, road)
    draw.rect(screen, yellow, left_edge_marker)
    draw.rect(screen, yellow, right_edge_marker)

    #add up vehicles

    #cars move initialization

    for car in cars:
        if car.rect.top >= bg_height:
            car.kill()
            car = Vehicle(image_names[randint(0, 1)], x_list[randint(0, 3)], randint(-200, -50), average_width, average_height, enemy_speed)
            cars.add(car)

            score += 1


    text = font.render('score:' + str(score), True, white)
    screen.blit(text, (20, 50))

    if sprite.spritecollide(player, cars, False):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
    #draw lane markers

    if gameover:
        draw.rect(screen, red, (0, 50, bg_width, 100))
        text1 = font.render('Game Over', True, white)
        screen.blit(text1, (300, 70))
        player.speed = 0
        enemy_speed = 0
        scroll_speed = 0
        screen.blit(crash, crash_rect)


    player.draw(screen)
    player.move()

    cars.draw(screen)
    cars.update()
    
    line_a.draw()
    line_b.draw()
    line_c.draw()



    display.update()