from src.Constants.Constants import *


def remove_walls(current_cell, next_cell):
    dx = current_cell.x - next_cell.x
    dy = current_cell.y - next_cell.y
    if dx == CELL_SIZE:
        current_cell.walls['left'] = False
        next_cell.walls['right'] = False
    elif dx == -CELL_SIZE:
        current_cell.walls['right'] = False
        next_cell.walls['left'] = False

    elif dy == CELL_SIZE:
        current_cell.walls['top'] = False
        next_cell.walls['bottom'] = False
    elif dy == -CELL_SIZE:
        current_cell.walls['bottom'] = False
        next_cell.walls['top'] = False
