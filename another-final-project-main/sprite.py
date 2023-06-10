from pygame import*

class Vehicle(sprite.Sprite):
    def __init__(self, image_name, x , y, width, height, speed):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = self.image.get_rect()
        self.image = transform.scale(self.image, (width, height))
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        #self.rect.center = [x, y]

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 120:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 420:
            self.rect.x += self.speed


class Player(Vehicle):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__(image_name, x, y, width, height, speed)

