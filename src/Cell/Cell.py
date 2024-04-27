import pygame
from src.Constants.Constants import *
import random


def check_cell(x, y, board):
    if x < 0 or x > WIDTH - CELL_SIZE or y < 0 or y > HEIGHT - CELL_SIZE:
        return False
    index = x // CELL_SIZE + (y // CELL_SIZE) * cols
    if index < 0:
        return False
    return board[index]


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True,
                      'right': True,
                      'bottom': True,
                      'left': True
                      }
        self.visit = False

    def draw_current_cell(self, screen):
        pygame.draw.rect(screen, CELL_COLOR_CURRENT,
                         (self.x + 2, self.y + 2, CELL_SIZE - 2, CELL_SIZE - 2))

    def draw_cell(self, screen):
        if self.visit:
            pygame.draw.rect(screen, CELL_COLOR_VISITED,
                             (self.x + 2, self.y + 2, CELL_SIZE - 2, CELL_SIZE - 2))
        else:
            pygame.draw.rect(screen, CELL_COLOR_NOT_VISITED,
                             (self.x + 2, self.y + 2, CELL_SIZE - 2, CELL_SIZE - 2))
        if not self.walls['top']:
            pygame.draw.line(screen, CELL_COLOR_VISITED,
                             (self.x + 2, self.y),
                             (self.x + CELL_SIZE - 1, self.y), 2)
        if not self.walls['right']:
            pygame.draw.line(screen, CELL_COLOR_VISITED,
                             (self.x + CELL_SIZE, self.y + 2),
                             (self.x + CELL_SIZE, self.y + CELL_SIZE - 1), 2)
        if not self.walls['bottom']:
            pygame.draw.line(screen, CELL_COLOR_VISITED,
                             (self.x + 2, self.y + CELL_SIZE),
                             (self.x + CELL_SIZE - 1, self.y + CELL_SIZE), 2)
        if not self.walls['left']:
            pygame.draw.line(screen, CELL_COLOR_VISITED,
                             (self.x, self.y + 2),
                             (self.x, self.y + CELL_SIZE - 1), 2)

    def get_neighbors(self, board):
        top = check_cell(self.x, self.y - CELL_SIZE, board)
        right = check_cell(self.x + CELL_SIZE, self.y, board)
        bottom = check_cell(self.x, self.y + CELL_SIZE, board)
        left = check_cell(self.x - CELL_SIZE, self.y, board)
        neighbors = []
        if top and not top.visit:
            neighbors.append(top)
        if right and not right.visit:
            neighbors.append(right)
        if bottom and not bottom.visit:
            neighbors.append(bottom)
        if left and not left.visit:
            neighbors.append(left)

        if neighbors:
            return random.choice(neighbors)
        else:
            return False
