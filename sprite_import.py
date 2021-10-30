import pygame


# PLAYER

def initialize_player_sprites():

    # PLAYER IDLE
    player_idle_1 = pygame.image.load(
        "graphics/character/idle/player-idle-1.png").convert_alpha()
    player_idle_2 = pygame.image.load(
        "graphics/character/idle/player-idle-2.png").convert_alpha()
    player_idle_3 = pygame.image.load(
        "graphics/character/idle/player-idle-3.png").convert_alpha()
    player_idle_4 = pygame.image.load(
        "graphics/character/idle/player-idle-4.png").convert_alpha()

    player_idle = [player_idle_1, player_idle_2, player_idle_3, player_idle_4]

    # PLAYER RUN
    player_run_1 = pygame.image.load(
        "graphics/character/run/player-run-1.png").convert_alpha()
    player_run_2 = pygame.image.load(
        "graphics/character/run/player-run-2.png").convert_alpha()
    player_run_3 = pygame.image.load(
        "graphics/character/run/player-run-3.png").convert_alpha()
    player_run_4 = pygame.image.load(
        "graphics/character/run/player-run-4.png").convert_alpha()
    player_run_5 = pygame.image.load(
        "graphics/character/run/player-run-5.png").convert_alpha()
    player_run_6 = pygame.image.load(
        "graphics/character/run/player-run-6.png").convert_alpha()

    player_run = [player_run_1, player_run_2, player_run_3,
                  player_run_4, player_run_5, player_run_6]

    # PLAYER JUMP
    player_jump_1 = pygame.image.load(
        "graphics/character/jump/player-jump-1.png").convert_alpha()
    player_jump_2 = pygame.image.load(
        "graphics/character/jump/player-jump-2.png").convert_alpha()
    player_jump_3 = pygame.image.load(
        "graphics/character/jump/player-jump-3.png").convert_alpha()
    player_jump_4 = pygame.image.load(
        "graphics/character/jump/player-jump-4.png").convert_alpha()

    player_jump = [player_jump_1, player_jump_2, player_jump_3, player_jump_4]

    # PLAYER FALL
    player_fall_1 = pygame.image.load(
        "graphics/character/fall/player-fall-1.png").convert_alpha()
    player_fall_2 = pygame.image.load(
        "graphics/character/fall/player-fall-2.png").convert_alpha()

    player_fall = [player_fall_1, player_fall_2]

    player_animations = {'idle': player_idle,
                         'run': player_run, 'jump': player_jump, 'fall': player_fall}

    return player_animations
