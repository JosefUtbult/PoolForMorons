# Welcome to the begining of the file

import pygame

class Pool_ball:
    def __init__(self, position: tuple, color: pygame.Color):
        self.position = position
        self.color = color

def main():
    
    baluru = Pool_ball((0, 0), pygame.Color(255, 0, 0))

if __name__ == "__main__":
    main()
