from src.Cell.Cell import *
from src.Cell.remove_walls import remove_walls
from src.Wall.wall import *


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
        for wall_rect in wall_rects:
            if player_rect.colliderect(wall_rect):
                player_x, player_y = previous_player_x, previous_player_y
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    walking_left = True
                    walking_right = False
                    walking_up = False
                    walking_down = False
                    walk_index = 0
                elif event.key == pygame.K_RIGHT:
                    walking_right = True
                    walking_left = False
                    walking_up = False
                    walking_down = False
                    walk_index = 0
                elif event.key == pygame.K_UP:
                    walking_up = True
                    walking_down = False
                    walking_left = False
                    walking_right = False
                    walk_index = 0
                elif event.key == pygame.K_DOWN:
                    walking_down = True
                    walking_up = False
                    walking_left = False
                    walking_right = False
                    walk_index = 0
        previous_player_x, previous_player_y = player_x, player_y

        if maze_generated:
            clock.tick(10)
        else:
            clock.tick(200)
