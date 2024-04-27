from src.Cell.Cell import Cell
from src.Cell.remove_walls import remove_walls
from src.Wall.wall import create_wall_rects
from src.Keyboard.Keyboard import keyboard
from src.Constants.Constants import *
import pygame


def generate_maze(screen, clock, walk_right, walk_left, walk_up_down):
    screen.fill(GRID_COLOR)
    board = [Cell(col * CELL_SIZE, row * CELL_SIZE) for row in range(rows) for col in range(cols)]
    current_cell = board[0]
    stack = []
    player_x = 15
    player_y = 12
    player_speed = 5
    walking_left = False
    walking_right = False
    walking_up = False
    walking_down = False
    walk_index = 0
    running = True
    maze_generated = False
    previous_player_x, previous_player_y = player_x, player_y

    while running:
        if maze_generated:
            board[cols * rows - 1].walls['right'] = False
        [cell.draw_cell(screen) for cell in board]
        current_cell.visit = True
        if not maze_generated:
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
            if walking_left or walking_right or walking_up or walking_down:
                if walking_left:
                    player_x -= player_speed
                    screen.blit(walk_left[walk_index % 5], (player_x, player_y))
                    walk_index += 1
                elif walking_right:
                    player_x += player_speed
                    screen.blit(walk_right[walk_index % 5], (player_x, player_y))
                    walk_index += 1
                elif walking_up:
                    player_y -= player_speed
                    screen.blit(walk_up_down[0], (player_x, player_y))
                    walk_index += 1
                elif walking_down:
                    player_y += player_speed
                    screen.blit(walk_up_down[0], (player_x, player_y))
                    walk_index += 1
            else:
                screen.blit(walk_up_down[0], (player_x, player_y))

        pygame.display.flip()

        wall_rects = create_wall_rects(board)

        player_rect = pygame.Rect(player_x - 1, player_y - 1, 26, 37)
        last_cell = board[cols * rows - 1]

        if player_rect.colliderect(pygame.Rect(last_cell.x + CELL_SIZE - 2, last_cell.y, 2, CELL_SIZE)):
            player_x = 15
            player_y = 12

        for wall_rect in wall_rects:
            if player_rect.colliderect(wall_rect):
                player_x, player_y = previous_player_x, previous_player_y
                break

        (walking_left, walking_right, walking_up,
         walking_down, walk_index, running) = keyboard(walking_left, walking_right, walking_up,
                                                       walking_down, walk_index, running)
        if not running:
            pygame.quit()

        previous_player_x, previous_player_y = player_x, player_y

        if maze_generated:
            clock.tick(50)
        else:
            clock.tick(200)
