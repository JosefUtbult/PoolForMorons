import pygame
from math import pi, sin, cos, tan, radians, degrees, sqrt, floor, atan
from time import sleep
screen = None
overall_radius = 200
nr_of_layers = 10

origin = [400, 400]
solid = False

def main():
    global screen
    init_graphics()
    
    spheres = [Sphere(origin, pygame.Color(0, int(255 * i / 3), 255 - int(255 * i / 3))) for i in range(1)] 

    print("Done")
    
    delta = 1

    while check_quit():
      
        screen.fill(pygame.Color(0, 0, 0))
        for sphere in spheres:
            sphere.render(screen)

        pygame.draw.circle(screen, pygame.Color(255, 0, 0), spheres[0].position[:2], 3)
        pygame.display.flip()
    
        spheres[0].move([delta * 2, delta])

        if spheres[0].position[0] >= 1000:
            delta = -1
        elif spheres[0].position[0] <= 400:
            delta = 1
        

class Sphere:

    def __init__(self, origin, color):
        temp = generate_sphere(color)
        self.nodes = temp[0]
        self.polygons = temp[1]
        self.position = origin[:]

    def render(self, screen):
        
        for polygon in self.polygons:

            if not solid:
                pygame.draw.polygon(screen, polygon.color, [(int(polygon.nodes[i].position[0] + self.position[0]), int(polygon.nodes[i].position[1] + self.position[1])) for i in range(len(polygon.nodes))], 1)
            else:
                pygame.draw.polygon(screen, polygon.color, [(polygon.nodes[i].position[0] + self.position[0], polygon.nodes[i].position[1] + self.position[1]) for i in range(len(polygon.nodes))])
            
            if polygon is self.polygons[0]:
                print(polygon.nodes[0].position[2])

    def move(self, distance):
        global overall_radius

        angle = [distance[i] / overall_radius for i in range(2)]
        
        for y in range(len(self.nodes)):

            for node in self.nodes[y]:
                node.position[0] = cos(angle[0]) * node.position[0] - sin(angle[0]) * node.position[1]
                
                node.position[1] = sin(angle[0]) * node.position[0] + cos(angle[0]) * node.position[1]
                node.position[1] = sin(angle[1]) * node.position[2] + cos(angle[1]) * node.position[1]
                
                node.position[2] = cos(angle[1]) * node.position[2] - sin(angle[1]) * node.position[1]
               
                #if sqrt(pow(node.position[0], 2) + pow(node.position[1], 2) + pow(node.position[2], 2)) < overall_radius:
                #
                #    temp = abs(node.position[0]) + abs(node.position[1]) + abs(node.position[2])
                #    
                #    for i in range(3):
                #        
                #        node.position[i] += node.position[i] / temp
                #
                #            self.position[0] += distance[0]
        

        self.position[0] += distance[0]
        self.position[1] += distance[1]
       



class Polygon:

    def __init__(self, nodes, color):
        self.nodes = nodes
        self.color = color

class Node:

    all_nodes = []

    def __init__(self, position, angle):

        self.position = position
        self.angle = angle
        Node.all_nodes.append(self)

def init_graphics():
    global screen, origin
   
    pygame.init() 

    dimension = (1000, 800)

    try:
        dimension = pygame.display.list_modes()[0]
    
    except:
        pass

    screen = pygame.display.set_mode(dimension)


def generate_sphere(color):
    global overall_radius, nr_of_layers

    overall_circumference = overall_radius * 2 * pi

    nodes = []
    polygons = []

    position = [0, overall_radius, 0]
    nodes.append([Node(position, calculate_angle(position))])

    for y in range(1, nr_of_layers):
        
        nodes.append([])
        radius = sin(((nr_of_layers / 2) - abs((nr_of_layers / 2) - y)) * pi / nr_of_layers) * overall_radius
        height = cos(y * pi / nr_of_layers) * overall_radius
        
        for instance in range(nr_of_layers):
            position = [cos(instance * 2 * pi / nr_of_layers) * radius, height, sin(instance * 2 * pi / nr_of_layers) * radius]
            nodes[-1].append(Node(position, calculate_angle(position)))

    position = [0, -1 * overall_radius, 0]
    nodes.append([Node(position, calculate_angle(position))])

    for y in range(nr_of_layers):
        for i in range(max(len(nodes[y]), len(nodes[y + 1]))):

            if len(nodes[y]) <= 1:
                polygons.append(Polygon([nodes[y][0], nodes[y + 1][i], nodes[y + 1][(i + 1) % len(nodes[y + 1])]], color))
            
            elif len(nodes[y + 1]) <= 1:
                polygons.append(Polygon([nodes[y][i], nodes[y][(i + 1) % len(nodes[y + 1])], nodes[y + 1][0]], color))
            
            else:
                polygons.append(Polygon([nodes[y][i], nodes[y + 1][i], nodes[y + 1][(i + 1) % len(nodes[y + 1])], nodes[y][(i + 1) % len(nodes[y])]], color)) 

    return (nodes, polygons)


def calculate_angle(position):

    angle = []

    for i in [0, 2]:
        if position[i] != 0:
            angle.append(atan(position[2] / position[i]))
        else:
            angle.append(pi / 2)

    return angle

def check_quit():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True



if __name__ == "__main__":
    main()
