import pygame
from src.Constants.Constants import *


def create_wall_rects(board):
    # Создание прямоугольников стен на основе информации о стенах клеток
    wall_rects = []
    for cell in board:
        x, y = cell.x, cell.y
        if cell.walls['top']:
            wall_rects.append(pygame.Rect(x, y, CELL_SIZE, 5))
        if cell.walls['right']:
            wall_rects.append(pygame.Rect(x + CELL_SIZE - 2, y, 2, CELL_SIZE))
        if cell.walls['bottom']:
            wall_rects.append(pygame.Rect(x, y + CELL_SIZE - 2, CELL_SIZE, 2))
        if cell.walls['left']:
            wall_rects.append(pygame.Rect(x, y, 5, CELL_SIZE))
    return wall_rects
