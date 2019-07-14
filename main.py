import pgzrun as pgz
import pygame
import random
import time


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
        self.framecounter = 0
        self.WIDTH = WIDTH

gamestate = GameState()

class Bird(Actor):
    def __init__(self, *args):
        Actor.__init__(self, *args)
        self.dy = 0

class Pipe(Actor):
    def __init__(self, *args):
        Actor.__init__(self, *args)
        self.x = gamestate.WIDTH + 64
        self.y = random.randrange(3*HEIGHT/4, HEIGHT-10)
        self.spacing = 100
        #self.pipes = []

    # def spawn(self):
    #     if self.x < WIDTH - self.width - self.spacing:
    #         self.pipes.append(self)
# pipe = Pipe('pipe.png')
# print(f"pipe.x: {pipe.x}")
# pipes =[pipe]

pipes = []

def spawn_pipes(pipes):
    # number_of_pipes = int(WIDTH / (pipe.width + pipe.spacing))
    #print(f"framecount: {gamestate.framecounter}, pipes: {pipes}")
    #print(f"WIDTH - pipe.width - pipe.spacing: {WIDTH - pipe.width - pipe.spacing}")
    if len(pipes) == 0:
        pipes.append(Pipe('pipe.png'))

    if  pipes[-1].x < WIDTH - pipes[-1].width - pipes[-1].spacing:
        print("hello")
        # 
        pipes.append(Pipe('pipe.png'))

    if pipes[0].x < 0 - pipes[0].width - pipes[0].spacing:
        del pipes[0]
    #     print(f"len pipes: {len(pipes)}")
    #     print(f"first pipe x: {pipes[0].x}")
    #     print(f"last pipe x: {pipes[-1].x}")

    # if pipes[0].x < 0 - pipe.width - pipe.spacing:
    #     pipes.append(Pipe('pipe.png', (WIDTH+64, HEIGHT/2)))
    #     pipes.pop(0)

    #print(f"framecount: {gamestate.framecounter}, pipes: {pipes}")
    
    #print(f"framecount: {gamestate.framecounter}, pipes: {pipes}")    

    x = 0
    for pipe in pipes:
        #pipe.x -= gamestate.groundscroll
        #pipe.x -= 2
        print(f"framecount: {gamestate.framecounter}, pipe: {x}, pipe.x: {pipes[x].x}")
        x +=1
    #print(f"framecount: {gamestate.framecounter}, pipes: {pipes}")
    return pipes

def pipe_motion(pipes):
    for pipe in pipes:
        pipe.x -= GROUND_SCROLL_SPEED


# def draw_pipes(pipes):
#     for pipe in pipes:
#         pipe.draw()

def draw_pipes(pipes):
    for a in range(len(pipes)): pipes[a].draw()



bird = Bird('bird.png')
bird.x = WIDTH/2 - bird.width/2
bird.y = HEIGHT/2 - bird.height/2
bird.dy = PSEUDOGRAVITY




ground = pygame.image.load('images/ground.png')
ground = pygame.transform.scale(ground, (WIDTH, 7*ground.get_height()))
ground2 = ground




bg = pygame.image.load('images/background.png')
bg_height = bg.get_height()
bg_width = bg.get_width()
bg_size = bg.get_size()

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
timearray = []
def update():
    gamestate.framecounter += 1
    
    gamestate.backgroundscroll = (gamestate.backgroundscroll + BACKGROUND_SCROLL_SPEED) % BACKGROUND_LOOPING_POINT
    #print(gamestate.backgroundscroll)
    gamestate.groundscroll = (gamestate.groundscroll + GROUND_SCROLL_SPEED) % WIDTH
    # pipe.x -= GROUND_SCROLL_SPEED
    #pipe.spawn()
    bird_motion()
    pipe_motion(pipes)
    spawn_pipes(pipes)

def draw():
    screen.clear()
    screen.blit(bg, (0 - gamestate.backgroundscroll,0))
    screen.blit(bg2, (WIDTH - gamestate.backgroundscroll, 0))
    draw_pipes(pipes)
    screen.blit(ground, (0 - gamestate.groundscroll, HEIGHT-ground.get_height()))
    screen.blit(ground, (WIDTH - gamestate.groundscroll, HEIGHT-ground.get_height()))
    bird.draw()
    

pgz.go()
