import pygame, math, sys
from pygame.locals import *

pygame.init()

size = w, h = 500, 500
disp = pygame.display.set_mode(size)
pygame.display.set_caption('plastic mania')
started = False

point, length, last = (5,5), 250, 0
rot = False
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
count, current_minigame = 0, None

class minigame():
    def __init__(self):
        pass

    def check_inp(self, keycode):
        return pygame.key.get_pressed()[keycode]

class fishing_minigame(minigame):
    def __init__(self):
        self.point, self.length, self.last = (5,5), 250, 0
        self.rot, self.count, self.running = False, 0, False
        self.point = (self.x, self.y) = 0, 0
        self.cx, self.cy = w/2, h/2

        self.states = ["rotate", "guage", "reel"]
        self.state_index = 0
        self.state_dict = {
            "rotate" : self.rotate,
            "guage" : self.guage,
            "reel" : self.reel,
        }

    def get_endv(self):
        self.count += 0.1
        x = math.sin(self.count) * length
        y = math.cos(self.count) * length 
        return x, y
    
    def render_bg(self):
        global w, h
        disp.fill((0,0,200))
        p_rect = pygame.Rect(self.cx-5, self.cy-5, 10, 10)
        pygame.draw.rect(disp, (255,255,255), p_rect)

    def rotate(self):
        tick = pygame.time.get_ticks()
        if tick - self.last <= 50: return
        self.last = tick
        vx, vy = self.get_endv()
        self.point = (self.x + vx, self.y + vy)
        pygame.draw.line(disp, (255,255,255), (self.cx, self.cy), point, 3)

        if self.check_inp(pygame.K_RETURN):
            self.state_index = 1

    def guage(self):
        pass

    def reel(self):
        pass

    def update(self):
        self.render_bg()
        self.state_dict[self.states[self.state_index]]()
        pygame.display.update()

current_minigame = fishing_minigame()

def show_title():
    disp.fill((0,0,0))
    text = font.render("press enter to play", True, (255,255,255))
    t_rect = text.get_rect()
    t_rect.center = w // 2, h // 2
    disp.blit(text, t_rect)
    pygame.display.update()

while True:
    clock.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if not started:
        if keys[pygame.K_RETURN]: started = True
        show_title()
    else:
        current_minigame.update()

        
        
    