# To use the test:
#   Run the pygame program and type inputs in the terminal
#
# Inputs are:
#   Angle (degrees)
#   Magnitude of force
#   x of impact (on circle)
#   y of impact (on cirlce)
#
# Input all three before result is visible.

import pygame
from math import cos, sin, atan2, radians

SCREEN = None
FONT = None
RUNNING = True

BALL_VARS = {
        "vel" : 0.0,
        "ang" : 0.0
}

RADIUS = 200
SCREEN_DIM = (1200, 600)

FONT_SIZE = 20

def main():
    global RUNNING

    init()

    while RUNNING:
        render()


def init():
    global  SCREEN, SCREEN_DIM, \
            FONT, FONT_SIZE

    pygame.init()

    SCREEN = pygame.display.set_mode(SCREEN_DIM)

    pygame.font.init()
    FONT = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)


def render():
    global SCREEN

    check_quit()

    SCREEN.fill(pygame.Color(0, 0, 0))

    main_ball()

    pygame.display.flip()


def main_ball():
    global  SCREEN, SCREEN_DIM, \
            RADIUS, BALL_VARS

    ball_point = (SCREEN_DIM[0] // 2, SCREEN_DIM[1] // 2)

    pygame.draw.circle(
            SCREEN,
            pygame.Color(150, 150, 150),
            ball_point,
            RADIUS,
            3
    )


    pygame.draw.line(
            SCREEN,
            pygame.Color(50, 150, 50),
            ball_point,
            (
                ball_point[0] + round(RADIUS * cos(BALL_VARS["ang"])),
                ball_point[1] + round(RADIUS * sin(BALL_VARS["ang"]))
            ),
            5
    )


def check_quit():
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            return



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Keyboard Interrupt")
        print()
