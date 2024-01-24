# coding:utf-8

import math
import pygame_sdl2 as pg

def get_display_center():
    info = pg.display.Info()
    return (info.current_w/2, info.current_h/2)


def vc_get_angle(center, pos):
    """
    @param pos: posição do mouse
    @return: ângulo em raidanos da posição do mouse em relação ao centro informado.
    Controle Virtual é dividido em três partes.
    Para o eixo-y :
    1) above the center of the controller
    2) below the center of the controller
    3) at the same height of the center of the controller
    If the mouse point is above the center of the controller, than check
    for one of three conditions:
    1) x is to the right of the controller
    2) x is to the left of the controller
    3) x is at the same point as the centerx of the controller
    """
    x,y = pos
    rad = 0.0
    if y < center[1]:

        if x > center[0]:
            opposite = float(center[1] - y)
            adjacent = float(x - center[0])
            rad = math.atan(opposite/adjacent)
        elif x < center[0]:
            opposite = float(center[0] - x)
            adjacent = float(center[1] - y)
            rad = .5 * math.pi + (math.atan(opposite/adjacent))
        else:
            rad = 0.5 * math.pi

    elif y > center[1]:
        if x < center[0]:
            opposite = float(y - center[1])
            adjacent = float(center[0] - x)
            rad = math.pi + (math.atan(opposite/adjacent))
        elif x > center[0]:
            adjacent = float(y - center[1])
            opposite = float(x - center[0])
            rad = (1.5 * math.pi) + math.atan(opposite/adjacent)
        else:
            rad = 1.5 * math.pi
    else:
        if x < center[0]:
            rad = math.pi
    return rad