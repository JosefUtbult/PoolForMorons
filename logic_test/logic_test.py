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
from math import cos, sin, atan2, tan, radians, degrees, sqrt

SCREEN = None
FONT = None
RUNNING = True

RADIUS = 50
SCREEN_DIM = (600, 300)

FONT_SIZE = 20

COLLIDED = False

BALL_VARS = {
        "vel" : 0.0,
        "ang" : 0.0,
        "pos" : (SCREEN_DIM[0] // 2, SCREEN_DIM[1] // 2)
}

COLL_VARS = {
        "vel" : 0.0,
        "ang" : 0.0,
        "rel_ang" : 0.0,
        "pos" : (BALL_VARS["pos"][0] + RADIUS * 2, BALL_VARS["pos"][1])
}


# TODO TEMP
HIT_TEMP = (424, 242)
ANG_TEMP = 120

def main():
    global RUNNING

    init()
    print("{: <12} {: <12} {: <12} {: <12} {: <12} {: <12}".format(
            "REL_ANG", "COLL_ANG", "COLL_VEL", "MAIN_ANG", "MAIN_VEL", "HIT_ANG"
        )
    )

    while RUNNING:

        get_collision()

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

    balls()

    pygame.display.flip()


def balls():
    global  SCREEN, SCREEN_DIM, \
            RADIUS, BALL_VARS, COLL_VARS

    pygame.draw.circle(
            SCREEN,
            pygame.Color(150, 150, 150),
            BALL_VARS["pos"],
            RADIUS,
            3
    )


    pygame.draw.line(
            SCREEN,
            pygame.Color(50, 150, 50),
            BALL_VARS["pos"],
            (
                BALL_VARS["pos"][0] + round(RADIUS * cos(BALL_VARS["ang"])),
                BALL_VARS["pos"][1] + round(RADIUS * sin(BALL_VARS["ang"]))
            ),
            5
    )

    # TODO TEMP
    pygame.draw.line(
            SCREEN,
            pygame.Color(50, 50, 50),
            BALL_VARS["pos"],
            (
                BALL_VARS["pos"][0] + round(RADIUS * cos(radians(COLL_VARS["rel_ang"]))),
                BALL_VARS["pos"][1] + round(RADIUS * sin(radians(COLL_VARS["rel_ang"])))
            ),
            3
    )

    COLL_VARS["pos"] = (
            round(2 * RADIUS * cos(radians(COLL_VARS["rel_ang"]))) + BALL_VARS["pos"][0],
            round(2 * RADIUS * sin(radians(COLL_VARS["rel_ang"]))) + BALL_VARS["pos"][1]
    )

    pygame.draw.circle(
            SCREEN,
            pygame.Color(150, 50, 50),
            COLL_VARS["pos"],
            RADIUS,
            3
    )

    pygame.draw.line(
            SCREEN,
            pygame.Color(150, 50, 50),
            COLL_VARS["pos"],
            (
                COLL_VARS["pos"][0] + round(RADIUS * cos(radians(COLL_VARS["ang"]))),
                COLL_VARS["pos"][1] + round(RADIUS * sin(radians(COLL_VARS["ang"])))
            ),
            5
    )

def get_collision():
    global SCREEN_DIM, COLLIDED

    mouse_pos = pygame.mouse.get_pos()

    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        COLL_VARS["rel_ang"] = 90 - degrees(atan2(
            mouse_pos[0] - BALL_VARS["pos"][0],
            mouse_pos[1] - BALL_VARS["pos"][1]
        ))

    else:
        COLL_VARS["ang"] = 90 - degrees(atan2(
            mouse_pos[0] - COLL_VARS["pos"][0],
            mouse_pos[1] - COLL_VARS["pos"][1]
        ))

        if mouse_pressed[2] and not COLLIDED:
            COLL_VARS["vel"] = sqrt(
                        (mouse_pos[0] - COLL_VARS["pos"][0]) ** 2 + \
                        (mouse_pos[1] - COLL_VARS["pos"][1]) ** 2
                    )

            COLLIDED = True

            ball_vx = COLL_VARS["vel"] * \
                    cos(radians(COLL_VARS["ang"] - COLL_VARS["rel_ang"])) * \
                    cos(radians(COLL_VARS["rel_ang"])) + \
                    BALL_VARS["vel"] * \
                    sin(radians(BALL_VARS["ang"] - COLL_VARS["rel_ang"])) * \
                    cos(radians(COLL_VARS["rel_ang"] + 90))

            ball_vy = COLL_VARS["vel"] * \
                    cos(radians(COLL_VARS["ang"] - COLL_VARS["rel_ang"])) * \
                    sin(radians(COLL_VARS["rel_ang"])) + \
                    BALL_VARS["vel"] * \
                    sin(radians(BALL_VARS["ang"] - COLL_VARS["rel_ang"])) * \
                    sin(radians(COLL_VARS["rel_ang"] + 90))

            BALL_VARS["ang"] = degrees(atan2(ball_vx, ball_vy))

            BALL_VARS["vel"] = sqrt( ball_vx ** 2 + ball_vy ** 2 )

        elif not mouse_pressed[2]:
            COLLIDED = False

    print("{: <12.5f} {: <12.5f} {: <12.5f} {: <12.5f} {: <12.5f}".format(
            COLL_VARS["rel_ang"],
            COLL_VARS["ang"],
            COLL_VARS["vel"],
            BALL_VARS["ang"],
            BALL_VARS["vel"]
        ),
        end="\r"
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
