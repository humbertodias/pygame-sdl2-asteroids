# coding:utf-8

import pygame_sdl2 as pg
pg.import_as_pygame()

from asteroid import *
from bullet import *
from ship import *
from star_field import *
from controller import *
from touch_buttons import *

def main():
    print('pg.get_sdl_version()', pg.get_sdl_version())

    FPS = 60
    SIZE = (800,600)
    # screen = pg.display.set_mode(SIZE, pg.FULLSCREEN)
    screen = pg.display.set_mode(SIZE, pg.RESIZABLE)
    icon =  pg.image.load('resource/img/icon.png')
    pg.display.set_caption("AsteroidsPresentation", icon)

    background = pg.surface.Surface(SIZE)

    font = pg.font.Font('resource/font/hyperspace.ttf', 40)
    text = font.render("by Humberto Dias", 1, Color.WHITE)

    star_field = StarField(screen)
    ship = Ship('resource/img/ship.png', angle=0)
    asteroids = Asteroid.create_asteroids()

    all_sprites = pg.sprite.Group(asteroids, ship)

    center = get_display_center()

    actions = TouchButtons.create_empty_actions()
    actions["left"]=actions["right"]=actions["accelerate"]=actions["shoot"]=None


    width, height = ship.get_screen_size()

    button_size = height/5
    touch_buttons = TouchButtons(screen, button_size)


    clock = pg.time.Clock()
    keep_going = True
    while keep_going:

        clock.tick(FPS)
        time = clock.get_time()

        screen.fill((0, 0, 0, 255))
        # screen.blit(background, (0,0))
        star_field.draw()

        mouse_pos = pg.mouse.get_pos()

        events = pg.event.get()
        for event in events:

            if event.type==pg.QUIT:
                keep_going = False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    keep_going = False

            # Android back key.
            elif event.type == pg.KEYDOWN and event.key == pg.K_AC_BACK:
                break



            if event.type == ( pg.FINGERMOTION ):
                print(event)
                mouse_pos = (event.x * width, event.y * height)

                if actions['left'] != None:
                    if touch_buttons.left_rect.collidepoint(mouse_pos):
                        actions['left'] = event.fingerId
                    elif actions['left'] == event.fingerId:
                        actions['left'] = None
                elif touch_buttons.left_rect.collidepoint(mouse_pos):
                    actions['left'] = event.fingerId


                if actions['right'] != None:
                    if touch_buttons.right_rect.collidepoint(mouse_pos):
                        actions['right'] = event.fingerId
                    elif actions['right'] == event.fingerId:
                        actions['right'] = None
                elif touch_buttons.right_rect.collidepoint(mouse_pos):
                    actions['right'] = event.fingerId


                if actions['accelerate'] != None:
                    if touch_buttons.power_rect.collidepoint(mouse_pos):
                        actions['accelerate'] = event.fingerId
                    elif actions['accelerate'] == event.fingerId:
                        actions['accelerate'] = None
                elif touch_buttons.power_rect.collidepoint(mouse_pos):
                    actions['accelerate'] = event.fingerId


                if actions['shoot'] != None:
                    if touch_buttons.shot_rect.collidepoint(mouse_pos):
                        actions['shoot'] = event.fingerId
                    elif actions['shoot'] == event.fingerId:
                        actions['shoot'] = None
                elif touch_buttons.shot_rect.collidepoint(mouse_pos):
                    actions['shoot'] = event.fingerId


            if event.type == (pg.FINGERUP):

                if actions["left"] != None:
                    actions["left"]=None
                if actions["right"] != None:
                    actions["right"]=None
                if actions["accelerate"] != None:
                    actions["accelerate"]=None
                if actions["shoot"] != None:
                    actions["shoot"]=None

            if event.type == (pg.MOUSEBUTTONDOWN):
                fingerId = 0

                ## Check if the mouse_pos is within the rectangle
                if touch_buttons.left_rect.collidepoint(mouse_pos):
                    actions["left"]=fingerId

                if touch_buttons.right_rect.collidepoint(mouse_pos):
                    actions["right"]=fingerId

                if touch_buttons.power_rect.collidepoint(mouse_pos):
                    actions["accelerate"]=fingerId

                if touch_buttons.shot_rect.collidepoint(mouse_pos):
                    actions["shoot"]=fingerId

            if event.type == (pg.MOUSEBUTTONUP):

                if touch_buttons.left_rect.collidepoint(mouse_pos):
                    actions["left"]=None
                if touch_buttons.right_rect.collidepoint(mouse_pos):
                    actions["right"]=None
                if touch_buttons.power_rect.collidepoint(mouse_pos):
                    actions["accelerate"]=None
                if touch_buttons.shot_rect.collidepoint(mouse_pos):
                    actions["shoot"]=None





        # pg.event.pump()
        # print('actions', actions)

        # key_pressed = pg.key.get_pressed()
        # if key_pressed[pg.K_ESCAPE] or pg.event.get(pg.QUIT):
        #     keep_going = False
        # if key_pressed[pg.K_LEFT] or key_pressed[pg.K_a]:
        #     ship.left()
        # if key_pressed[pg.K_RIGHT] or key_pressed[pg.K_d]:
        #     ship.right()
        # if key_pressed[pg.K_UP]  or key_pressed[pg.K_w]:
        #     ship.up()
        # if key_pressed[pg.K_SPACE]:
        #     all_sprites.add(ship.shoot())

#         mpos = pg.mouse.get_pos()
#         rad = vc_get_angle(center, mpos)
#
#         # +90 graus por conta do bico da nave na vertical
#         angle = math.degrees(rad) + 90
#         ship.rotate(angle)
#
#         buttons = pg.mouse.get_pressed()
# #        print('buttons', buttons)
#         # first/left button
#         if buttons[0]:
#             actions["shoot"]
#             # all_sprites.add(ship.shoot())
#         # third/right button
#         if buttons[2]:
#             actions["up"]
#             # ship.up()


        # 7 = left
        if actions['left'] != None:
            ship.left()
        # 5 = right
        if actions['right'] != None:
            ship.right()
        # 15 = Quadrado
        if actions['shoot'] != None:
            all_sprites.add(ship.shoot())
        # 14 = X
        if actions['accelerate'] != None:
            ship.up()


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
        #         ship = Ship('resource/img/ship.png', angle=0)
        #         all_sprites.add ( ship )

        if len(asteroids.sprites()) == 0 :
            asteroids.add ( Asteroid.create_asteroids() )
            all_sprites.add( asteroids )
        # colisao



        caption = "Angle %d FPS %d/%d Q%d" % (ship.angle, clock.get_fps(), FPS, ship.get_quadrant())
        # text = font.render("by Humberto Lino", 1, Color.WHITE)
        text = font.render(caption, 1, Color.WHITE)
        screen.blit(text, (0,0))
        pg.display.set_caption(caption)


        touch_buttons.draw()

        pg.display.flip()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
