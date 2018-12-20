import pygame
from math import pi, sin, cos, radians, sqrt, floor

screen = None

def main():

    init_graphics()

    render()

    print("Done")

    while check_quit():
        pass

class Pool_ball:

    def __init__(self, color, nodes, edges):
        self.color = color
        self.edges = edges
        self.nodes = nodes


class Edge:

    all_edges = []

    def __init__(self, nodes):
        self.nodes = nodes
        Edge.all_edges.append(self)


class Node:
    def __init__(self, position):

        self.position = position


def init_graphics():
    global screen
   
    pygame.init() 

    dimension = (1000, 800)

    try:
        dimension = pygame.display.list_modes()[0]
    
    except:
        pass

    screen = pygame.display.set_mode(dimension)


#    nodes = [   Node((100, 100, 0)), 
#                Node((200, 100, 0)), 
#                Node((200, 200, 0)), 
#                Node((100, 200, 0)),
#                Node((150, 150, 100)),
#                Node((250, 150, 100)),
#                Node((250, 250, 100)),
#                Node((150, 250, 100))]

#    edges = [   Edge((nodes[0], nodes[1])), 
#                Edge((nodes[1], nodes[2])), 
#                Edge((nodes[2], nodes[3])), 
#                Edge((nodes[3], nodes[0])),
#                Edge((nodes[4], nodes[5])),
#                Edge((nodes[5], nodes[6])),
#                Edge((nodes[6], nodes[7])),
#                Edge((nodes[7], nodes[4])),
#                Edge((nodes[0], nodes[4])),
#                Edge((nodes[1], nodes[5])),
#                Edge((nodes[2], nodes[6])),
#                Edge((nodes[3], nodes[7]))] 


    # pool_ball = Pool_ball(pygame.Color(255, 255, 255), nodes, edges)
    generate_sphere()


def render():
    global screen

    for edge in Edge.all_edges:

        temp = int((edge.nodes[0].position[2] - 200) * 255 / 400)
        pygame.draw.line(   screen, pygame.Color(temp, 255 - temp, int(255 * ((len(Edge.all_edges) - Edge.all_edges.index(edge) ) / len(Edge.all_edges)))), 
                            edge.nodes[0].position[:2], 
                            edge.nodes[1].position[:2],
                            1)
    
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), (400, 400), 3)
    pygame.display.flip() 
    

def generate_sphere():
    
    origin = (400, 400, 400)
    overall_radius = 200
    overall_circumference = overall_radius * 2 * pi
    instance_ratio = 0.02
    nr_of_layers = 20
    nodes = []
    edges = []


    nodes.append([Node((origin[0], origin[1] - overall_radius, origin[2]))])

    for i in range(1, nr_of_layers):

        pos_y = floor(origin[1] + i * (overall_radius * 2 / nr_of_layers) - overall_radius) 
        radius = calculate_radius(overall_radius, nr_of_layers, i if i < nr_of_layers // 2 else i - 1)
        
        nodes.append(generate_circle_xz((origin[0], pos_y, origin[2]), 
                                        radius,
                                        instance_ratio))
    
    
    nodes.append([Node((origin[0], origin[1] + overall_radius, origin[2]))])



    for y in range(len(nodes)):
        for i in range(len(nodes[y])):
            edges.append(Edge((nodes[y][i], nodes[y][(i + 1) % len(nodes[y])])))

            if y < len(nodes) - 1:
                
                if len(nodes[y]) > len(nodes[y + 1]):
                    append_edges(nodes[y], nodes[y + 1], edges)

                else:
                    append_edges(nodes[y + 1], nodes[y], edges)


def append_edges(layer_max, layer_min, edges):

    for i in range(len(layer_max)):
        
        try:
            edges.append(Edge((layer_max[i], layer_min[int(i * len(layer_min) / len(layer_max))])))
        except IndexError as e:
            print(len(layer_max), '\n', len(layer_min))

def calculate_radius(overall_radius, nr_of_layers, i):

    return sqrt(pow(overall_radius, 2) - pow((( abs(i - ((nr_of_layers - 1) / 2))) * overall_radius * 4) / ((nr_of_layers - 1) * 2), 2))

def generate_circle_xz(origin, radius, instance_ratio):
    nodes = []
    circumference = int(radius * 2 * pi)

    for n in range(int(circumference * instance_ratio)):
      
        posz = calculate_position(sin, n / (instance_ratio * circumference), radius, origin[2])
        posx = calculate_position(cos, n / (instance_ratio * circumference), radius, origin[0])
        
        # print((n * 3600) / circumference)

        nodes.append(Node((posx, origin[1], posz)))
    
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
