import pygame

pool_balls = []

class Pool_ball:

    def __init__(   self, 
                    position: tuple, 
                    color: pygame.Color, 
                    number: int
                 ):

        self.position = position
        self.color = color
        self.number = number

def generate_pool_ball(position: tuple, color: pygame.Color, number: int):
    global pool_balls

    pool_balls.append(Pool_ball(position, color, number))
