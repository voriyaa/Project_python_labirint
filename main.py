import pygame
from src.Constants.Constants import *
from src.MazeGenerator.maze_generator import generate_maze

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(MAZE_SIZE)
pygame.display.set_caption('Maze Generator')
icon = pygame.image.load('images/maze_icon.png')
pygame.display.set_icon(icon)

generate_maze(screen, clock)
