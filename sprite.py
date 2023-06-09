from pygame import*

class Vehicle(sprite.Sprite):
    def __init__(self, image_name, x ,y):
        super().__init__()

        self.image = image.load(image_name)
        self.rect = self.image.get_rect()
        
        #scale image
        image_scale = 45 / self.rect.width
        new_width = self.rect.width * round(image_scale)
        new_height = self.rect.height * round(image_scale)
        self.image = transform.scale(self.image, (new_width, new_height))

        self.rect.center = [x, y]

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Vehicle):
    def __init__(self, image_name, x, y):
        super().__init__(image_name, x, y)

