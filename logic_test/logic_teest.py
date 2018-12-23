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
from math import cos, sin, radians

screen = None
font = None
RUNNING = True
IMPACT_POINT = None

center_x = 600
center_y = 250

angle_text = ""
magn_text = ""
impact_point_x = ""
impact_point_y = ""

old_angle = ""
old_magn = ""
old_impact_x = ""
old_impact_y = ""

RADIUS = 200
SCREEN_DIM = (1200, 600)

FONT_SIZE = 20

LINE_POINTS = [[center_x, center_y], [center_x + RADIUS, center_y]]
IMPACT_POINT = None

def init():
    global screen, FONT_SIZE, SCREEN_DIM, RADIUS, font, angle_text, old_angle, magn_text, old_magn, impact_point_x, impact_point_y, old_impact_x, old_impact_y, IMPACT_POINT

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_DIM)

    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

    angle_text = ""
    magn_text = ""

    while RUNNING:
        render()

        old_angle = angle_text
        old_magn = magn_text
        old_impact_x = impact_point_x
        old_impact_y = impact_point_y

        angle_text = ""
        magn_text = ""
        impact_point_x = ""
        impact_point_y = ""

        angle_text = input("Angle:")
        magn_text = input("Magnitude:")
        impact_point_x = input("Impact x:")
        impact_point_y = input("Impact y:")

        try:
#           print(radians(float(angle_text)))
#           print(radians(float(angle_text)))
            LINE_POINTS[1][0] = center_x + \
                    RADIUS * cos(radians(float(angle_text)))
            LINE_POINTS[1][1] = center_y - \
                    RADIUS * sin(radians(float(angle_text)))
            IMPACT_POINT = [int(impact_point_x), int(impact_point_y)]

            if (IMPACT_POINT[0] - center_x) ** 2 + (IMPACT_POINT[1] - center_y) ** 2 != RADIUS ** 2 and (IMPACT_POINT[0] != center_x or IMPACT_POINT[1] != center_y):
                print((IMPACT_POINT[0] - center_x) ** 2 + (IMPACT_POINT[1] - center_y) ** 2,
                        "==", RADIUS ** 2)
                print(IMPACT_POINT[0], "==", center_x)
                print(IMPACT_POINT[1], "==", center_y)
                raise ValueError

        except ValueError:
            print("INVALID INPUT")

def render():
    global screen, center_x, center_y

    check_quit()

    screen.fill(pygame.Color(0, 0, 0))

    pygame.draw.circle(
            screen,
            pygame.Color(240, 240, 240),
            (center_x, center_y),
            RADIUS,
            3
    )
    pygame.draw.line(
            screen,
            pygame.Color(50, 255, 50),
            LINE_POINTS[0],
            LINE_POINTS[1],
            5
    )

    try:
        render_impact()
    except TypeError as e:
        print("FAILED IMPACT")
        print(e)
    render_text()

    pygame.display.flip()

def render_impact():
    global screen, IMPACT_POINT, RADIUS, angle_text

    imp_point = (
            IMPACT_POINT[0] + round(
                RADIUS * cos(radians(float(angle_text)))
                ),
            IMPACT_POINT[1] + round(
                RADIUS * sin(radians(float(angle_text)))
                )
    )

    pygame.draw.line(
            screen,
            pygame.Color(255, 50, 50),
            tuple(IMPACT_POINT),
            imp_point,
            5
    )

def render_text():
    global screen, font, angle_text, old_angle, magn_text, old_magn, impact_point_x, impact_point_y, old_impact_x, old_impact_y

    # NOW
    screen.blit(
            font.render(
                "Angle: " + angle_text,
                1,
                (255, 255, 255)
            ),
            (20, 20)
    )
    screen.blit(
            font.render(
                "Magnitude: " + magn_text,
                1,
                (255, 255, 255)
            ),
            (20, 40)
    )
    screen.blit(
            font.render(
                "Impact: [" + impact_point_x + ", " + impact_point_y + "]",
                1,
                (255, 255, 255)
            ),
            (20, 60)
    )

    # PREVIOUS
    screen.blit(
            font.render(
                "Angle: " + old_angle,
                1,
                (255, 255, 255)
            ),
            (820, 20)
    )
    screen.blit(
            font.render(
                "Magnitude: " + old_magn,
                1,
                (255, 255, 255)
            ),
            (820, 40)
    )
    screen.blit(
            font.render(
                "Impact: [" + old_impact_x + ", " + old_impact_y + "]",
                1,
                (255, 255, 255)
            ),
            (820, 60)
    )

def check_quit():
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            return


if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        print()
        print("Keyboard Interrupt")
