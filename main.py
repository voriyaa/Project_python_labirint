import pygame
from src.Constants.Constants import *
from src.MazeGenerator.maze_generator import generate_maze

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(MAZE_SIZE)
pygame.display.set_caption('Maze Generator')
icon = pygame.image.load('images/maze_icon.png')
pygame.display.set_icon(icon)
walk_right = [
    pygame.image.load('images/walk_left/l1.png'),
    pygame.image.load('images/walk_left/l2.png'),
    pygame.image.load('images/walk_left/l3.png'),
    pygame.image.load('images/walk_left/l4.png'),
    pygame.image.load('images/walk_left/l5.png'),
]

walk_left = [
    pygame.image.load('images/walk_right/r1.png'),
    pygame.image.load('images/walk_right/r2.png'),
    pygame.image.load('images/walk_right/r3.png'),
    pygame.image.load('images/walk_right/r4.png'),
    pygame.image.load('images/walk_right/r5.png'),
]

walk_up_down = [
    pygame.image.load('images/walk_up_down/0.png')
]

generate_maze(screen, clock, walk_left, walk_right, walk_up_down)
