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
        self.extremities = []

        # TODO remove this
        self.fys_pos = [float(position[0]), float(position[1])]
        self.velocity = 0.0
        self.acceleration = 0.0

        self.direction = [0.0, 0.0]

        self.mass = mass

        self.fric_coeff = fric_coeff

        self.init_extremities()

        self.colliding = False


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

        self.set_extremities()

        self.acceleration = -(self.mass * self.fric_coeff)

        if self.velocity <= 0.0:
            MOVING_PARTICLES.remove(self)
            self.velocity = 0.0
            self.acceleration = 0.0

    def collide_with(self, other):
        #TODO
        pass

    def set_extremities(self):
        self.extremities[0] = self.position

    def init_extremities(self):
        self.extremities = [self.position]


class Pool_ball(Particle):
    pool_balls = []

    # static stuff TODO variables perhaps?
    mass = 0.3
    fric_coeff = 0.26
    radius = 10

    def __init__(   self,
                    position: list,
                    color: pygame.Color,
                    number: int
                 ):

        self.color = color
        self.number = number

        super().__init__(position, Pool_ball.mass, Pool_ball.fric_coeff)

        Pool_ball.pool_balls.append(self)

    def collide_with(self, other):

        if self.velocity > 0.0 and other.velocity > 0.0:
            other_pre_v = other.velocity
            #TODO
            #Pool_ball.
        
        if self.velocity > 0.0:
            other.velocity = self.velocity * 1
        pass

    def init_extremities(self):
        self.extremities = [
                [self.position[0] - Pool_ball.radius, self.position[1]],
                [self.position[0] + Pool_ball.radius, self.position[1]],
                [self.position[0], self.position[1] - Pool_ball.radius],
                [self.position[0], self.position[1] + Pool_ball.radius]
        ]

    def set_extremities(self):
        self.extremities[0][0] = self.position[0] - Pool_ball.radius
        self.extremities[0][1] = self.position[1]

        self.extremities[1][0] = self.position[0] + Pool_ball.radius
        self.extremities[1][1] = self.position[1]  

        self.extremities[2][0] = self.position[0] 
        self.extremities[2][1] = self.position[1] - Pool_ball.radius 
        self.extremities[3][0] = self.position[0] 
        self.extremities[3][1] = self.position[1] + Pool_ball.radius

