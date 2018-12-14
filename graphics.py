import pygame
import logic

screen = None
font = None
RUNNING = True

BALL_RADIUS = 10
FONT_SIZE = 20

def init_graphics(screen_size: tuple):
    global screen, font, FONT_SIZE

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
  
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

def render():
    check_quit()
    pygame.display.flip()
    
    for pool_ball in logic.pool_balls:
        render_pool_ball(pool_ball)

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
                        pygame.Color(0, 100, 100))
    
    screen.blit(text, 
                (
                    pool_ball.position[0] - text.get_width() // 2,
                    pool_ball.position[1] - text.get_height() // 2)
               )


def check_quit():
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            return

