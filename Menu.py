import pygame
import sys

red = 255, 0, 0
blue = 0, 0, 255
pygame.font.init()
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont('Helvetica', 24)



class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.surface = pygame.Surface((self.width, self.height))
        self.game_loop = False
        self.start_button = Button(red, 200, 200, 500, 500)
        self.exit_button = Button(blue, 200, 200, 1200, 500)
        self.button_group = [self.start_button, self.exit_button]

    def initialise(self):
        for t in self.button_group:
            t.draw(self.screen)
        if self.start_button.is_pressed:
            return True
        if self.exit_button.is_pressed:
            sys.exit()
        self.start_button.image.blit(self.start_button.img, (self.start_button.width / 2 + self.start_button.x -
                                                             pygame.font.Font.get_linesize(self.start_button.font),
                                                             self.start_button.height / 2 + self.start_button.y -
                                                             pygame.font.Font.get_height(self.start_button.font) / 2))

    def handle_mouse_interaction(self, is_pressed):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.button_group:
            t.check_click(mouse_x, mouse_y, is_pressed)


class Button(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.default_col = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.default_col)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect.center = [x, y]
        self.is_pressed = False
        self.is_hovered = False
        self.hover_col = 0, 191, 255
        self.pressed_col = 100, 150, 255
        self.font = pygame.font.SysFont('Helvetica', 24)
        self.img = font.render('START', True, blue)

    def check_click(self, x, y, is_pressed):
        if self.is_colliding(x, y):
            self.is_hovered = True
            if is_pressed:
                self.is_pressed = True
        else:
            self.is_hovered = False

    def is_colliding(self, x, y):
        if self.y < y < self.y + self.height:
            if self.x < x < self.x + self.width:
                return True

        return False

    def draw(self, surface):
        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image.fill(self.default_col)

        surface.blit(self.image, (self.x, self.y))

