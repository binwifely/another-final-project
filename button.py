from pygame import*

class Button():
    def __init__(self, x, y, width, height, button_image_name):
        self.image = transform.scale(image.load(button_image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self, window):
        pos = mouse.get_pos()
        action = False
        window.blit(self.image, (self.rect.x, self.rect.y))
        
        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
            
            if mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        return action
    