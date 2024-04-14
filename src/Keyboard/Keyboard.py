import pygame


def keyboard(walking_left, walking_right, walking_up, walking_down, walk_index, running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return walking_left, walking_right, walking_up, walking_down, walk_index, False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return True, False, False, False, 0, True
            elif event.key == pygame.K_RIGHT:
                return False, True, False, False, 0, True
            elif event.key == pygame.K_UP:
                return False, False, True, False, 0, True
            elif event.key == pygame.K_DOWN:
                return False, False, False, True, 0, True

    return walking_left, walking_right, walking_up, walking_down, walk_index, running
