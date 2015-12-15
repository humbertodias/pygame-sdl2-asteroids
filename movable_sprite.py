# coding:utf-8

import pygame_sdl2 as pg
import math
import random
from color import *


class MovableSprite(pg.sprite.Sprite):

    def __init__(self, image_file_name, size=1, angle=0, speed_rotate=8, speed_accelerate=5, initial_position=[320,240]):
        pg.sprite.Sprite.__init__(self)
        self.original_image = pg.image.load(image_file_name).convert_alpha()

        # tamanho mínimo
        if size < 1:
            size = 1

        self.size = size

        self.scale(size)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.move_pos = initial_position

        self.angle = angle
        self.speed_rotate = speed_rotate
        self.speed_accelerate = speed_accelerate

    def scale(self, size):
        width,height = self.original_image.get_width() * size, self.original_image.get_height() * size
        self.original_image = pg.transform.scale(self.original_image, (width, height))

    def update(self):
        self.rotate().move().screen_border()

    def rotate(self):
        old_center = self.rect.center
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect  = self.image.get_rect()
        self.rect.center = old_center
        return self

    def left(self):
        self.angle += self.speed_rotate
        self.fix_angle()
        return self
    
    def right(self):
        self.angle -= self.speed_rotate
        self.fix_angle()
        return self

    def fix_angle(self):
        if self.angle > 360:
            self.angle -= 360
        if self.angle < 0:
            self.angle = 360

    def get_quadrant(self):
        # http://www.youtube.com/watch?v=LUZH0kgug8M
        if self.angle >= 0 and self.angle <= 90:
            return 1
        elif self.angle <= 180:
            return 2
        elif self.angle <= 270:
            return 3
        else:
            return 4

    def screen_border(self):

        width,height = self.get_screen_size()
        x,y = self.move_pos
        if x > width:
            x -= width
        elif x < 0:
            x += width
        if y > height:
            y -= height
        elif y < 0:
            y += height

        self.move_pos=[x, y]
        self.rect.center=self.move_pos

        return self

    def is_out_of_screen(self):
        width,height = self.get_screen_size()
        x,y = self.move_pos
        if (x > width or x < 0) or (y > height or y < 0):
            return True
        return False

    def up(self):
        pos = self.accelerate(self.speed_accelerate)
        self.move_pos[0] += pos[0]
        self.move_pos[1] += pos[1]
        return self

    def move(self):
        self.rect.center = self.move_pos
        return self

    def accelerate(self, velocity):
        rad_angle = math.radians(self.angle)
        rad_x =  math.cos(rad_angle) * velocity
        rad_y = -math.sin(rad_angle) * velocity
        return (rad_x, rad_y)

    def collision(self, object):
        return self.rect.colliderect(object.rect)

    def change_color(self, from_color, to_color):
        self.original_image = Color.color_replace(self.original_image, from_color, to_color)
        self.color = to_color

    @staticmethod
    def random_angle():
        return random.randint(0,360)

    @staticmethod
    def random_position():
        w,y = MovableSprite.get_screen_size()
        x = random.randint(0,w)
        y = random.randint(0,y)
        return [x,y]

    @staticmethod
    def get_screen_size():
        info = pg.display.Info()
        return (info.current_w, info.current_h)
