import pygame
from math import cos, sin, degrees

PHYS_TABLE_DIM = (2.70, 1.35) # TODO necessary?
MOVING_PARTICLES = []

class Particle:

    def __init__(   self,
                    position: list,
                    mass: float,
                    fric_coeff: float
                ):

        self.position = position

        # TODO remove this
        self.fys_pos = [float(position[0]), float(position[1])]
        self.velocity = 0.0
        self.acceleration = 0.0

        self.direction = [0.0, 0.0]

        self.mass = mass

        self.fric_coeff = fric_coeff


    def apply_force(self, magnitude: float, angle: float):

        if self.acceleration == 0.0 and self.velocity == 0.0:
            global MOVING_PARTICLES
            MOVING_PARTICLES.append(self)

        self.acceleration = magnitude / self.mass

        self.direction[0] = sin(degrees(angle))
        self.direction[1] = cos(degrees(angle))

    def apply_acceleration(self, magnitude: float, angle: float):

        if self.acceleration == 0.0 and self.velocity == 0.0:
            global MOVING_PARTICLES
            MOVING_PARTICLES.append(self)

        self.acceleration = magnitude

        self.direction[0] = sin(degrees(angle))
        self.direction[1] = cos(degrees(angle))

    def move(self):
        self.velocity += self.acceleration
        self.fys_pos[0] += self.direction[0] * self.velocity
        self.fys_pos[1] += self.direction[1] * self.velocity

        self.position[0] = round(self.fys_pos[0])
        self.position[1] = round(self.fys_pos[1])

        self.acceleration = -(self.mass * self.fric_coeff)

        if self.velocity <= 0.0:
            MOVING_PARTICLES.remove(self)
            self.velocity = 0.0
            self.acceleration = 0.0


class Pool_ball(Particle):
    pool_balls = []

    # static stuff TODO variables perhaps?
    mass = 0.3
    fric_coeff = 0.26

    def __init__(   self,
                    position: list,
                    color: pygame.Color,
                    number: int
                 ):

        self.position = position
        self.color = color
        self.number = number

        super().__init__(position, Pool_ball.mass, Pool_ball.fric_coeff)

        Pool_ball.pool_balls.append(self)

