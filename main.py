import pgzrun as pgz
import pygame
import random


WIDTH = 1280
HEIGHT = 720

music.play('all_decked_out.mp3')

BACKGROUND_SCROLL_SPEED = 5
GROUND_SCROLL_SPEED = 10
BACKGROUND_LOOPING_POINT = WIDTH
PSEUDOGRAVITY = 15
PIPE_IMAGE='pipe.png'
PIPE_SCROLL = -5

class GameState():
    def __init__(self):
        self.groundscroll = 0
        self.backgroundscroll = 0

class Bird(Actor):
    def __init__(self, *args):
        Actor.__init__(self, *args)
        self.dy = 0

class Pipe(Actor):
    def __init__(self, *args):
        Actor.__init__(self, *args)
        self.x = WIDTH
        self.y = random.randrange(3*HEIGHT/4, HEIGHT-10)

pipe = Pipe('pipe.png')
bird = Bird('bird.png')
bird.x = WIDTH/2 - bird.width/2
bird.y = HEIGHT/2 - bird.height/2
bird.dy = PSEUDOGRAVITY


gamestate = GameState()

ground = pygame.image.load('images/ground.png')
ground = pygame.transform.scale(ground, (WIDTH, 7*ground.get_height()))
ground2 = ground




bg = pygame.image.load('images/background.png')
bg_height = bg.get_height()
bg_width = bg.get_width()
bg_size = bg.get_size()
print(type(bg_size))
bg = pygame.transform.scale(bg, (2*WIDTH, HEIGHT - ground.get_height()))
bg2 = bg


def bird_motion():
    
    if not keyboard.space:
        bird.y += PSEUDOGRAVITY
    elif keyboard.space:
        bird.y -= PSEUDOGRAVITY
    if keyboard.right:
        pass
    if keyboard.left:
        pass

def update():
    gamestate.backgroundscroll = (gamestate.backgroundscroll + BACKGROUND_SCROLL_SPEED) % BACKGROUND_LOOPING_POINT
    print(gamestate.backgroundscroll)
    gamestate.groundscroll = (gamestate.groundscroll + GROUND_SCROLL_SPEED) % WIDTH
    pipe.x -= GROUND_SCROLL_SPEED
    bird_motion()

def draw():
    screen.clear()
    screen.blit(bg, (0 - gamestate.backgroundscroll,0))
    screen.blit(bg2, (WIDTH - gamestate.backgroundscroll, 0))
    pipe.draw()
    screen.blit(ground, (0 - gamestate.groundscroll, HEIGHT-ground.get_height()))
    screen.blit(ground, (WIDTH - gamestate.groundscroll, HEIGHT-ground.get_height()))
    bird.draw()
    

pgz.go()
