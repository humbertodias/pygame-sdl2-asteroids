# coding:utf-8

import pygame_sdl2 as pg

from asteroid import *
from bullet import *
from ship import *
from star_field import *


def main():
    print('pg.get_sdl_version()', pg.get_sdl_version())

    pg.init()
    FPS = 60
    SIZE = (300,400)
    # screen = pg.display.set_mode(SIZE, pg.FULLSCREEN)
    screen = pg.display.set_mode(SIZE, pg.RESIZABLE)
    pg.display.set_caption("AsteroidsPresentation")

    background = pg.surface.Surface(SIZE)

    font = pg.font.Font(None, 20)
    text = font.render("by Humberto Lino", 1, Color.WHITE)

    star_field = StarField(screen)
    ship = Ship('img/ship.png', angle=0)
    asteroids = Asteroid.create_asteroids()

    all_sprites = pg.sprite.Group(asteroids, ship)

    clock = pg.time.Clock()
    keep_going = True
    while keep_going:
        clock.tick(FPS)
        time = clock.get_time()

        pg.event.pump()

        key_pressed = pg.key.get_pressed()
        if key_pressed[pg.K_ESCAPE] or pg.event.get(pg.QUIT):
            keep_going = False
        if key_pressed[pg.K_LEFT] or key_pressed[pg.K_a]:
            ship.left()
        if key_pressed[pg.K_RIGHT] or key_pressed[pg.K_d]:
            ship.right()
        if key_pressed[pg.K_UP]  or key_pressed[pg.K_w]:
            ship.up()
        if key_pressed[pg.K_SPACE]:
            all_sprites.add(ship.shoot())

        screen.blit(background, (0,0))
        star_field.draw()

        all_sprites.update()
        all_sprites.draw(screen)

        # colisao

        # bala acertou asteroide?
        for bullet in ship.bullets:
            for asteroid in asteroids:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroids.add (asteroid.divide())
                    all_sprites.add ( asteroids )

        # gameover
        # nave acertou asteroide?
        # for asteroid in asteroids:
        #     if ship.collision(asteroid):
        #         ship.kill()
        #         ship = Ship('img/ship.png', angle=0)
        #         all_sprites.add ( ship )

        if len(asteroids.sprites()) == 0 :
            asteroids.add (Asteroid.create_asteroids() )
            all_sprites.add( asteroids )
        # colisao


        background.blit(text, (0,0))

        pg.display.flip()
        caption = "Angle %d FPS %d/%d Q%d" % (ship.angle, clock.get_fps(), FPS, ship.get_quadrant())
        pg.display.set_caption(caption)


if __name__ == "__main__":
    main()