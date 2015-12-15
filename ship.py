from movable_sprite import *
from bullet import *


class Ship(MovableSprite):
    bullets = pg.sprite.Group()

    """
    Tempo para carregar
    """
    load = 0

    TIME_RELOAD_SHOT = 0

    """
    Tempo para carregar
    """

    def update(self):
        MovableSprite.update(self)
        self.load += 1

    def shoot(self):
        if self.load >= self.TIME_RELOAD_SHOT:

            self.load=0.0
            self.bullets.add(Bullet('img/bullet.png'
                                      , speed_rotate=10, speed_accelerate=10
                                      , angle=self.angle
                                      , initial_position=self.rect.center))

        return self.bullets