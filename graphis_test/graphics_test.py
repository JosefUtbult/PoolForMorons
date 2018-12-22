import pygame
from math import pi, sin, cos, tan, radians, sqrt, floor, atan
from time import sleep
screen = None
overall_radius = 200
instance_ratio = 0.02
nr_of_layers = 20

triangle_length = 10

origin = (400, 400, 400)


def main():
    global screen
    init_graphics()
    
    spheres = [Sphere((origin[0] + i * 500, origin[1], origin[2]), pygame.Color(0, int(255 * i / 3), 255 - int(255 * i / 3))) for i in range(1)] 

    print("Done")

    #spheres[0].move((1, 0, 0))
    while check_quit():
      
        screen.fill(pygame.Color(0, 0, 0))
        for sphere in spheres:
            sphere.render(screen)

        pygame.draw.circle(screen, pygame.Color(255, 0, 0), (400, 400), 3)
        pygame.display.flip()
        sleep(1)
        

class Sphere:

    def __init__(self, origin, color):
        temp = generate_sphere(origin, color)
        self.nodes = temp[0]
        self.polygons = temp[1]
        self.position = origin[:]

    def render(self, screen):
        
        for polygon in self.polygons:

            color_data = []

            for i in range(3):
                color_data.append(int((polygon.nodes[0].position[i] - self.position[i] + overall_radius) * 255 / (overall_radius * 2)) % 255)
            pygame.draw.polygon(screen, pygame.Color(color_data[0], color_data[1], color_data[2]), [node.position[:2] for node in polygon.nodes], 1)
    
    def move(self, new_position):
        global overall_radius

        for node_list in self.nodes:
            for node in node_list:
                node.angle = (cos(radians(360 * new_position[0] / (overall_radius * 2 * pi)) + node.angle[0]), node.angle[1])
                node.position = (node.angle[0] * overall_radius * sin(node.position[1] - self.position[0]) + node.position[0], node.position[1], node.position[2]) 
                 


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


def generate_sphere(origin, color):
    global overall_radius, nr_of_layers

    overall_circumference = overall_radius * 2 * pi

    nodes = []

    position = [origin[0], origin[1] - overall_radius, origin[2]]
    nodes.append([Node(position, calculate_angle(position, origin))])

    for y in range(1, nr_of_layers):
        
        nodes.append([])
        radius = (overall_radius * (nr_of_layers - 2) / nr_of_layers) - abs((nr_of_layers / 2) - y) * overall_radius * 2 / nr_of_layers
        
        for instance in range(nr_of_layers):
            position = [cos(instance * radius * 2 * pi / nr_of_layers)]
            print(position, radius)

    nodes = []
    polygons = []


def generate_sphere_1(origin, color):
    global nr_of_layers, overall_radius, instance_ratio

    overall_circumference = overall_radius * 2 * pi
    nodes = []
    polygons = []

    position = (origin[0], origin[1] - overall_radius, origin[2])

    nodes.append([Node(position, calculate_angle(origin, position))])

    for i in range(1, nr_of_layers):

        pos_y = floor(origin[1] + i * (overall_radius * 2 / nr_of_layers) - overall_radius) 
        radius = calculate_radius(overall_radius, nr_of_layers, i if i < nr_of_layers // 2 else i - 1)
        
        nodes.append(generate_circle_xz((origin[0], pos_y, origin[2]),
                                        origin,
                                        radius,
                                        instance_ratio))
    
    
    nodes.append([Node((origin[0], origin[1] + overall_radius, origin[2]), calculate_angle(origin, (origin[0], origin[1] + overall_radius, origin[2])))])



    for y in range(len(nodes) - 1):
        for i in range(max(len(nodes[y]), len(nodes[y + 1]))):
            
            polygons.append(Polygon(calculate_polygon(nodes, y, i, True), color))
            polygons.append(Polygon(calculate_polygon(nodes, y, i, False), color))
            
    return (nodes, polygons)


def calculate_angle(origin, position):

    angle = []

    for i in [0, 2]:
        
        if position[i] - origin[i] != 0:
            angle.append(atan((position[1] - origin[1]) / (position[i] - origin[i])))

        else:
            angle.append(pi / 2)

    return angle


def calculate_polygon(nodes, y, i, mode=True):
    out = []

    if len(nodes[y]) > len(nodes[y + 1]):
        layer_max = nodes[y]
        layer_min = nodes[y + 1]

    else:
        layer_max = nodes[y + 1]
        layer_min = nodes[y]


    out.append(layer_max[i])
    
    if mode:
        out.append(layer_max[(i + 1) % len(nodes[y])])

    else:
        out.append(layer_min[int(i * len(layer_min) / len(layer_max))])

    out.append(layer_min[(int(i * len(layer_min) / len(layer_max)) + 1) % len(layer_min)])
    
    return out


def calculate_radius(overall_radius, nr_of_layers, i):

    return sqrt(pow(overall_radius, 2) - pow((( abs(i - ((nr_of_layers - 1) / 2))) * overall_radius * 4) / ((nr_of_layers - 1) * 2), 2))

def generate_circle_xz(position, origin, radius, instance_ratio):
    nodes = []
    circumference = int(radius * 2 * pi)

    for n in range(int(circumference * instance_ratio)):
      
        posz = calculate_position(sin, n / (instance_ratio * circumference), radius, position[2])
        posx = calculate_position(cos, n / (instance_ratio * circumference), radius, position[0])
        
        # print((n * 3600) / circumference)

        nodes.append(Node((posx, position[1], posz), calculate_angle(origin, (posx, position[1], posz))))
    
    return nodes

def calculate_position(function, turnratio, radius, origin):

    return int(function(radians(360 * turnratio)) * radius) + origin


def check_quit():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True



if __name__ == "__main__":
    main()
