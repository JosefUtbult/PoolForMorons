# Welcome to the begining of the file

from logic import Pool_ball, Particle, MOVING_PARTICLES
import pygame
import logic
import graphics
from random import seed, randint, random, choice
from time import time

from threading import Thread

def main():

    seed(time())

    for i in range(1, 16):
        Pool_ball([60 + 50 * i, graphics.SCREENHEIGHT // 2], graphics.BALL_COLORS[(i - 1) % 8], i)

    graphics.init_graphics()

    while graphics.RUNNING:
        graphics.render()

        # TODO TESTING
        i = 0
        while i < 1 and random() < 0.20:
            choice(Pool_ball.pool_balls).apply_force(random()*1.2, random()*360)
            i += 1
        
        threads = thread_movement()
        for thread in threads:
            thread.join()

def thread_movement():
    global MOVING_PARTICLES
    threads = []
    for particle in MOVING_PARTICLES:
        t = Thread(target=particle.move)
        threads.append(t)
        t.start()
    return threads


    

if __name__ == "__main__":
    main()
