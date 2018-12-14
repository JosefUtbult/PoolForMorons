import pygame

screen = None
RUNNING = True

def init_graphics(screen_size: tuple):
    global screen

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
   

def render():
    check_quit()
    pygame.display.flip()


def check_quit():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            return

