from pygame import*

class Vehicle(sprite.Sprite):
    def __init__(self, image, x ,y):

        #scale image
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Player(Vehicle):
    def __init__(self, x, y):
        image = image.load('images/car.png')
        super().__init__(image, x, y)

