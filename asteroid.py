# coding:utf-8

from movable_sprite import *


class Asteroid(MovableSprite):
    SECTIONS = 2

    def __init__(self, image_file_name, size=1, angle=0, speed_rotate=8, speed_accelerate=5, initial_position=[320,240], color=Color.random_color()):
        MovableSprite.__init__(self, image_file_name, size, angle, speed_rotate, speed_accelerate, initial_position)
        self.change_color(Color.PINK, color)

    def update(self):
        MovableSprite.update(self)
        self.up()

    @staticmethod
    def create_asteroids():
        asteroids = pg.sprite.Group()

        for i in range(10):
            size = 1
            #par
            if i % 2 == 0:
                size = i // 2

            asteroid = Asteroid('img/asteroid.png'
                                     , size=size
                                     , angle=Asteroid.random_angle()
                                     , speed_rotate=2
                                     , speed_accelerate=1
                                     , initial_position=Asteroid.random_position()
                                     , color=Color.random_color())

            asteroids.add(asteroid)

        return asteroids


    def divide(self, angle = MovableSprite.random_angle()):
        parts = pg.sprite.Group()

        # > 1. Divida-o
        if self.size > 1:

            # asteroids maiores sao mais lentos
            speed_accelerate = ( 10 / self.size)
            speed_rotate = (10 / self.speed_rotate)

            for __ in range(0,self.SECTIONS):

                initial_position = [self.move_pos[0] + random.randint(0,self.image.get_width())
                                   ,self.move_pos[1] + random.randint(0,self.image.get_height()) ]

                asteroid = Asteroid('img/asteroid.png'
                         , size=self.size - 1
                         , angle=Asteroid.random_angle()
                         , speed_rotate = speed_rotate
                         , speed_accelerate = speed_accelerate
                         , initial_position=initial_position
                         , color=self.color)

                parts.add(asteroid)

        self.kill()
        return parts