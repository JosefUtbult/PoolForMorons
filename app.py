# Welcome to the begining of the file

from logic import Pool_ball
import pygame
import logic
import graphics
from random import seed, randint
from time import time

SCREENHEIGHT = 800
SCREENWIDTH = 1000

def main():
    
    seed(time())

    for i in range(1, 16):
        logic.generate_pool_ball((50 + 50 * i, 50), 
                pygame.Color(   randint(0, 255), 
                                randint(0, 255), 
                                randint(0, 255)
                            ), 
                i)
    graphics.init_graphics((SCREENWIDTH, SCREENHEIGHT))
    
    while graphics.RUNNING:
        graphics.render()

if __name__ == "__main__":
    main()
