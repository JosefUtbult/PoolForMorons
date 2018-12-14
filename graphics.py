import pygame
import logic

screen = None
font = None
RUNNING = True

SCREENHEIGHT = 800
SCREENWIDTH = 1000

BALL_RADIUS = 10
FONT_SIZE = 20

TABLE_HEIGHT = 400
TABLE_WIDTH = 800
TABLE_BORDER = 50

BALL_COLORS = [ pygame.Color(255, 250, 54), 
                pygame.Color(113, 47, 255),
                pygame.Color(255, 24, 8),
                pygame.Color(170, 0, 255),
                pygame.Color(255, 123, 7),
                pygame.Color(31, 138, 2), 
                pygame.Color(130, 38, 31),
                pygame.Color(50, 50, 50)]

def init_graphics():
    global screen, font, FONT_SIZE

    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
  
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

def render():
    global screen

    check_quit()
    
    screen.fill(pygame.Color(240, 240, 240))
    
    render_table()

    for pool_ball in logic.pool_balls:
        render_pool_ball(pool_ball)

    pygame.display.flip()


def render_pool_ball(pool_ball):

    global screen, font, BALL_RADIUS, FONT_SIZE
    
    pygame.draw.circle( screen,  
                        pool_ball.color, 
                        pool_ball.position, 
                        BALL_RADIUS
                      )

    if pool_ball.number > 8:
        pygame.draw.circle( screen,  
                            pygame.Color(255, 255, 255), 
                            pool_ball.position, 
                            int(BALL_RADIUS * 0.6)
                           )
    
    text = font.render( str(pool_ball.number), 
                        True, 
                        pygame.Color(61, 60, 59))
    
    screen.blit(text, ( pool_ball.position[0] - text.get_width() // 2,
                        pool_ball.position[1] - text.get_height() // 2))

def render_table():
    global screen, TABLE_WIDTH, TABLE_HEIGHT, TABLE_BORDER, SCREENWIDTH, SCREENHEIGHT

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(  (SCREENWIDTH - TABLE_WIDTH - TABLE_BORDER) // 2,
                                                                    (SCREENHEIGHT - TABLE_HEIGHT - TABLE_BORDER) // 2, 
                                                                    TABLE_WIDTH + TABLE_BORDER, 
                                                                    TABLE_HEIGHT + TABLE_BORDER))


    pygame.draw.rect(screen, pygame.Color(0, 255, 0), pygame.Rect(  (SCREENWIDTH - TABLE_WIDTH) // 2,
                                                                    (SCREENHEIGHT - TABLE_HEIGHT) // 2, 
                                                                    TABLE_WIDTH, 
                                                                    TABLE_HEIGHT))
    for instance in [   ((SCREENWIDTH - TABLE_WIDTH - (TABLE_BORDER // 2)) // 2, 
                         (SCREENHEIGHT - TABLE_HEIGHT - (TABLE_BORDER // 2)) // 2),
                        (SCREENWIDTH // 2,
                         (SCREENHEIGHT - TABLE_HEIGHT - (TABLE_BORDER // 2)) // 2),
                        ((SCREENWIDTH + TABLE_WIDTH + (TABLE_BORDER // 2)) // 2,
                         (SCREENHEIGHT - TABLE_HEIGHT - (TABLE_BORDER // 2)) // 2),
                        ((SCREENWIDTH - TABLE_WIDTH - (TABLE_BORDER // 2)) // 2, 
                         (SCREENHEIGHT + TABLE_HEIGHT + (TABLE_BORDER // 2)) // 2),
                        (SCREENWIDTH // 2,
                         (SCREENHEIGHT + TABLE_HEIGHT + (TABLE_BORDER // 2)) // 2),
                       ((SCREENWIDTH + TABLE_WIDTH + (TABLE_BORDER // 2)) // 2,
                        (SCREENHEIGHT + TABLE_HEIGHT + (TABLE_BORDER // 2)) // 2),
                       



                        ]:
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), instance, int(TABLE_BORDER * 0.3))



def check_quit():
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            return

