# Welcome to the begining of the file

from logic import Pool_ball
import pygame
import logic
import graphics

SCREENHEIGHT = 800
SCREENWIDTH = 1000

def main():
    
    # det_ballar_ur = Pool_ball((0, 0), pygame.Color(255, 0, 0))
    graphics.init_graphics((SCREENWIDTH, SCREENHEIGHT))

    while graphics.RUNNING:
        graphics.render()

if __name__ == "__main__":
    main()
