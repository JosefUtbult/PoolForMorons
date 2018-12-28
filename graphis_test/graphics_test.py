import pygame
from math import pi, sin, cos, tan, atan2, radians, degrees, sqrt, floor, atan
from time import sleep
screen = None
overall_radius = 50
nr_of_layers = 20

origin = [200, 200]
solid = True

ivory = pygame.Color(238, 238, 224)
def main():
    global screen
    init_graphics()
    
    spheres = [Sphere(origin, pygame.Color(0, int(255 * i / 3), 255 - int(255 * i / 3))) for i in range(1)] 
    
    spheres[0].polygons[len(spheres[0].polygons) // 2].color = pygame.Color(255, 0, 0)

    print("Done")
    
    temp = sort_layers(spheres[0].polygons)

    #for polygon in spheres[0].polygons:
    #    print(min([node.position[2] for node in polygon.nodes]))
    
    #print('--------------------------------------------------')

    #for polygon in temp:
    #    print(min([node.position[2] for node in polygon.nodes]))

    delta = 1

    while check_quit():
      
        screen.fill(pygame.Color(0, 0, 0))
        for sphere in spheres:
            sphere.render(screen)

        #pygame.draw.circle(screen, pygame.Color(255, 0, 0), spheres[0].position[:2], 3)
        pygame.display.flip()
    
        spheres[0].move([delta, delta])

        if spheres[0].position[0] >= 500 or spheres[0].position[0] <= 200:
            delta = delta * -1
        
        print(spheres[0].polygons[0].nodes[0].position[2], spheres[0].polygons[-1].nodes[0].position[2])
        #sleep(0.1)


class Sphere:

    def __init__(self, origin, color):
        temp = generate_sphere(color)
        self.nodes = temp[0]
        self.polygons = temp[1]
        self.position = origin[:]
        self.origin = origin[:]
    
    def render(self, screen):
       
        temp = sort_layers(self.polygons)
        
        for polygon in temp:
            
            #polygon.color = pygame.Color(0, 0, int(255 * (min([node.position[2] for node in polygon.nodes]) + overall_radius) / (overall_radius * 2)))

            if not solid:
                pygame.draw.polygon(screen, polygon.color, [(int(polygon.nodes[i].position[0] + self.position[0]), int(polygon.nodes[i].position[1] + self.position[1])) for i in range(len(polygon.nodes))], 1)
            else:
                pygame.draw.polygon(screen, polygon.color, [(int(polygon.nodes[i].position[0] + self.position[0]), int(polygon.nodes[i].position[1] + self.position[1])) for i in range(len(polygon.nodes))])
            

    def move(self, distance):
        global overall_radius

        self.position[0] += distance[0]
        self.position[1] += distance[1]
            
        if self.position[0] == self.origin[0] and self.position[1] == self.origin[1]:
            for node_list in self.nodes:
                for node in node_list:
                    node.position = node.origin[:]

        else:

            #angle_z = atan2(self.origin[1] - self.position[1], self.origin[0] - self.origin[0])
            #angle_y = sqrt(pow(self.origin[1] - self.position[1], 2) + pow(self.origin[0] - self.origin[0], 2)) / overall_radius
             
            angle_y = (self.position[0] - self.origin[0]) / overall_radius
            angle_x = (self.position[1] - self.origin[1]) / overall_radius

            a = cos(angle_x)
            b = sin(angle_x)
            c = cos(angle_y)
            d = sin(angle_y)

            for node_list in self.nodes:

                for node in node_list:

                    node.position[0] = c * node.origin[0] + d * node.origin[2]
                    node.position[1] = -b * d * node.origin[0] -  a * node.origin[1] + b * c * node.origin[2]
                    node.position[2] = -a * d * node.origin[0] + b * node.origin[1] + a * c * node.origin[2]


class Polygon:

    def __init__(self, nodes, color):
        self.nodes = nodes
        self.color = color

class Node:

    all_nodes = []

    def __init__(self, position, angle):

        self.position = position
        self.origin = position[:]
        self.angle = angle
        Node.all_nodes.append(self)

def init_graphics():
    global screen, origin
   
    pygame.init() 

    dimension = (1000, 800)

    #try:
    #    dimension = pygame.display.list_modes()[0]
    #
    #except:
    #    pass

    screen = pygame.display.set_mode(dimension)


def generate_sphere(color):
    global overall_radius, nr_of_layers, ivory

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
                polygons.append(Polygon([nodes[y][0], nodes[y + 1][i], nodes[y + 1][(i + 1) % len(nodes[y + 1])]], pygame.Color(255, 0, 0)))
            
            elif len(nodes[y + 1]) <= 1:
                polygons.append(Polygon([nodes[y][i], nodes[y][(i + 1) % len(nodes[y])], nodes[y + 1][0]], pygame.Color(255, 0, 0)))
            
            else:
                polygons.append(Polygon([nodes[y][i], nodes[y + 1][i], nodes[y + 1][(i + 1) % len(nodes[y + 1])], nodes[y][(i + 1) % len(nodes[y])]], pygame.Color(0, 255 - int(255 * y / nr_of_layers), int(255 * y / nr_of_layers))))#ivory if y > int(nr_of_layers * 0.35) and y < int(nr_of_layers * 0.6) else color)) 

    return (nodes, polygons)


def calculate_angle(position):

    angle = []

    for i in [0, 2]:
        if position[i] != 0:
            angle.append(atan(position[2] / position[i]))
        else:
            angle.append(pi / 2)

    return angle


def sort_layers(polygons):
    
    return sorted(polygons, key = lambda i: min([node.position[2] for node in i.nodes]))

def check_quit():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True



if __name__ == "__main__":
    main()
