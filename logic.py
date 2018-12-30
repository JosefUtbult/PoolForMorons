import pygame
from math import cos, sin, sqrt, atan2, radians

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

        self.angle = 0.0

        self.direction = [0.0, 0.0]

        self.mass = mass

        self.fric_coeff = fric_coeff

        self.colliding = False


    def apply_force(self, magnitude: float, angle: float):

        if self.acceleration == 0.0 and self.velocity == 0.0:
            global MOVING_PARTICLES
            MOVING_PARTICLES.append(self)

        self.angle = angle

        self.acceleration = magnitude / self.mass

        self.direction[0] = sin(angle)
        self.direction[1] = cos(angle)

    def apply_acceleration(self, magnitude: float, angle: float):

        if self.acceleration == 0.0 and self.velocity == 0.0:
            global MOVING_PARTICLES
            MOVING_PARTICLES.append(self)

        self.acceleration = magnitude

        self.direction[0] = sin(angle)
        self.direction[1] = cos(angle)

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

    def check_collision(self, other):
        if self.position == other.position:
            self.collide_with(
                    other,
                    atan2(
                        (self.position[0] - other.position[0]),
                        (self.position[1] - other.position[1])
                    )
            )

    def collide_with(self, other, collision_angle, master=True):
#        if collision_angle is None:
#            collision_angle = atan2(point[0] - self.position[0], point[1] - self.position[1])

        velocity_x  = other.velocity * cos(other.angle - collision_angle) * cos(collision_angle) \
                    + self.velocity * sin(self.angle - collision_angle) * cos(collision_angle + radians(90))

        velocity_y  = other.velocity * cos(other.angle - collision_angle) * sin(collision_angle) \
                    + self.velocity * sin(self.angle - collision_angle) * sin(collision_angle + radians(90))

        self.angle = atan2(velocity_x, velocity_y)
        self.velocity = sqrt( velocity_x ** 2 + velocity_y ** 2 )

        if master:
            other.collide_with(self, collision_angle, False)


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

    def check_collision(self, other):
        if self is other:
            return
        distance = sqrt(
                (self.fys_pos[0] - other.fys_pos[0]) ** 2 \
                + (self.fys_pos[1] - other.fys_pos[1]) ** 2
            )

        if distance <= Pool_ball.radius:
            print(self.number, other.number)
            self.collide_with(
                    other,
                    atan2(
                        (self.position[0] - other.position[0]),
                        (self.position[1] - other.position[1])
                    )
            )

    def collide_with(self, other, collision_angle, master=True):

        velocity_x  = other.velocity * cos(other.angle - collision_angle) * cos(collision_angle) \
                    + self.velocity * sin(self.angle - collision_angle) * cos(collision_angle + radians(90))

        velocity_y  = other.velocity * cos(other.angle - collision_angle) * sin(collision_angle) \
                    + self.velocity * sin(self.angle - collision_angle) * sin(collision_angle + radians(90))

        if master:
            other.collide_with(self, collision_angle, False)

        self.angle = atan2(velocity_x, velocity_y)
        self.direction[0] = sin(self.angle)
        self.direction[1] = cos(self.angle)
        self.velocity = sqrt( velocity_x ** 2 + velocity_y ** 2 )

        if self.acceleration == 0.0 and self.velocity == 0.0:
            global MOVING_PARTICLES
            MOVING_PARTICLES.append(self)

