from movable_sprite import *

class Bullet(MovableSprite):
    def update(self):
        MovableSprite.update(self)
        self.up()

        if self.is_out_of_screen():
            self.kill()