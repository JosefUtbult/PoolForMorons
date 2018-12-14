# Welcome to the begining of the file

from logic import Pool_ball
import pygame
import logic
import graphics
from random import seed, randint
from time import time

def main():
    
    seed(time())

    for i in range(1, 16):
        logic.generate_pool_ball((60 + 50 * i, graphics.SCREENHEIGHT // 2), graphics.BALL_COLORS[(i - 1) % 8], i)

    graphics.init_graphics()
    
    while graphics.RUNNING:
        graphics.render()

if __name__ == "__main__":
    main()
