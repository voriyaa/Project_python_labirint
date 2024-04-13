import pygame
from src.Constants.Constants import *
from src.Cell.Cell import *
from src.Cell.remove_walls import remove_walls


def generate_maze(screen, clock):
    screen.fill(GRID_COLOR)

    board = [Cell(col * CELL_SIZE, row * CELL_SIZE) for row in range(rows) for col in range(cols)]
    current_cell = board[0]
    stack = []

    running = True
    maze_generated = False

    while running:
        [cell.draw_cell(screen) for cell in board]
        current_cell.visit = True
        current_cell.draw_current_cell(screen)
        next_cell = current_cell.get_neighbors(board)
        if next_cell:
            current_cell.visit = True
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()
        else:
            maze_generated = True
        if maze_generated:
            pass

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        clock.tick(100)

    if maze_generated:
        print("Done")

