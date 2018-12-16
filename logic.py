import pygame


class Pool_ball:

    pool_balls = []

    def __init__(   self,
                    position: tuple,
                    color: pygame.Color,
                    number: int
                 ):

        self.position = position
        self.color = color
        self.number = number

        Pool_ball.pool_balls.append(self)

