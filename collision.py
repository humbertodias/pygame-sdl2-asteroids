# coding: utf-8

"""
Funções para detectar colisão.
"""
__author__  = 'Humberto Lino'
__version__ = '1.0'


import math


class Collision:
    """
    Classe que aglomera funções de colisão.
    """

    @staticmethod
    def RectangleCollidedWithCircle1(circle, rect):
        """
        Identifica colisão entre um Círculo e Retângulo.

        Fonte:\012
        U{http://devmag.org.za/2009/04/13/basic-collision-detection-in-2d-part-1}\012
        U{http://stackoverflow.com/questions/21089959/detecting-collision-of-rectangle-with-circle-in-html5-canvas}\012
        U{http://jsfiddle.net/CDLwP/1}

        @param circle: Circulo
        @param rect:  Retângulo
        @return: True se colidiu, False caso contrário
        """
        #  compute a center-to-center vector
        distX = abs(circle.pos.x - rect.pos.x-rect.width/2)
        distY = abs(circle.pos.y - rect.pos.y-rect.height/2)

        if distX > (rect.width/2 + circle.radius): return False
        if distY > (rect.height/2 + circle.radius): return False

        if distX <= (rect.width/2): return True
        if distY <= (rect.height/2): return True

        dx=distX-rect.width/2
        dy=distY-rect.height/2
        return dx*dx+dy*dy <= (circle.radius*circle.radius)


    # @staticmethod
    # def RectangleCollidedWithCircle2(circle,rect):
    #     """
    #     Identifica colisão entre Retângulo entre Circulo e Retângulo.
    #
    #     Fonte:\012
    #     U{http://stackoverflow.com/questions/21089959/detecting-collision-of-rectangle-with-circle-in-html5-canvas}
    #     @param circle: Circulo
    #     @param rect: Retângulo
    #     @return: True se colidiu, caso contrário False
    #     """
    #
    #     # compute a center-to-center vector
    #     half = Point(rect.width/2, rect.height/2)
    #
    #     center = Point(circle.pos.x - (rect.pos.x + half.x)
    #                  , circle.pos.y - (rect.pos.y + half.y))
    #
    #     # check circle position inside the rectangle quadrant
    #     side = Point(abs (center.x) - half.x
    #                , abs (center.y) - half.y)
    #
    #     # outside
    #     if side.x > circle.radius or side.y > circle.radius: return False
    #
    #     # intersects side or corner
    #     if side.x < 0 or side.y < 0: return True
    #
    #     # circle is near the corner
    #     return side.x * side.x + side.y * side.y < circle.radius * circle.radius

    @staticmethod
    def RectangleCollidedWithCircle(circle,rect):
        """
        Identifica colisão entre Circulo e Retângulo.

        @param circle: Circulo
        @param rect: Retângulo
        @return: True se colidiu, caso contrário False
        """
        return Collision.RectangleCollidedWithCircle2(circle,rect)


    @staticmethod
    def CircleCollidedWithCircle(circ1, circ2):
        """
        Identifica colisão entre Retângulo entre Circulo e Retângulo.

        Passos:\012
        1) Calcula a distância D entre o centro dos circulos com o Teorema de Pitagoras.\012
        2) Se calcula a soma S dos radios dos circulos.\012
        3) Se D <= S significa que os circulos se chocaram.\012

        @param circ1: Circulo
        @param circ2: Retângulo
        @return: True se colidiu, caso contrário False
        """
        distX = circ1.pos.x - circ2.pos.x
        distY = circ1.pos.y - circ2.pos.y
        distC = math.sqrt( distX ** 2 + distY ** 2 )
        # Pitagoras
        sumR = circ1.radius + circ2.radius
        return distC <= sumR

    @staticmethod
    def RectangleCollidedWithRectangle(r1, r2):
        return (r1.pos.x + r1.width > r2.pos.x) and (r1.pos.x < r2.pos.x + r2.width) \
           and (r1.pos.y + r1.height > r2.pos.y) and (r1.pos.y < r2.pos.y + r2.height)

    @staticmethod
    def LineCollidedWithLine(l1, l2):
        """
        Identifica Colisão entre Linhas.

        Fonte:\012
        U{http://devmag.org.za/2009/04/13/basic-collision-detection-in-2d-part-1}\012
        @param l1: Linha 1
        @param l2: Linha 2
        @return: True se colidiram, caso contrário False
        """
        denom = ((l2.p2.y - l2.p1.y) * (l1.p2.x - l1.p1.x)) - ( (l2.p2.x - l2.p1.x) * (l1.p2.y - l1.p1.y) )
        return denom != 0