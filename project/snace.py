import pygame
import random

# Initialiseren van Pygame
pygame.init()

# Instellen van het scherm
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snack Game")

# Kleuren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snelheid van de slang
SNAKE_SPEED = 5

# Lengte en breedte van de snacks en de slang
BLOCK_SIZE = 20

# Aantal extra levens
EXTRA_LIVES = 3

# Initialiseren van de klok en font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Functie om de tekst op het scherm te tekenen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Functie om de slang te tekenen
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(WIN, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie om de snacks te tekenen
def draw_snack(snack_list):
    for snack in snack_list:
        pygame.draw.rect(WIN, RED, [snack[0], snack[1], BLOCK_SIZE, BLOCK_SIZE])

# Functie om de grid te tekenen
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(WIN, BLACK, (0, y), (WIDTH, y))

# Functie om het spel te draaien
def game():
    game_over = False
    game_close = False

    # Startpositie van de slang
    snake_list = []
    length_of_snake = 1
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Startpositie van de snacks
    num_snacks = random.randint(2, 4)
    snacks = []
    for _ in range(num_snacks):
        snack_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        snack_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
        snacks.append([snack_x, snack_y])

    # Hoofd van de slang
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # Levens van de slang
    lives = 1

    while not game_over:

        while game_close == True:
            WIN.fill(WHITE)
            draw_text("Game Over! Druk op Q om te stoppen of op C om opnieuw te spelen", font, GREEN, WIN, WIDTH/2-300, HEIGHT/2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        # Teleporteer de slang naar de andere kant van het scherm als hij de rand raakt
        if snake_x >= WIDTH:
            snake_x = 0
        elif snake_x < 0:
            snake_x = WIDTH - BLOCK_SIZE
        elif snake_y >= HEIGHT:
            snake_y = 0
        elif snake_y < 0:
            snake_y = HEIGHT - BLOCK_SIZE
        
        WIN.fill(WHITE)
        draw_grid()
        pygame.draw.rect(WIN, GREEN, [snake_x, snake_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Controleer of de slang tegen zichzelf botst
        for segment in snake_list[:-1]:
            if segment == snake_head:
                lives -= 1
                if lives <= 0:
                    game_close = True

        draw_snake(snake_list)
        draw_snack(snacks)
        draw_text("Lives: {}".format(lives), font, GREEN, WIN, 10, 10)
        pygame.display.update()

        # Controleer of de slang een snack heeft gegeten
        for snack in snacks:
            if snake_x == snack[0] and snake_y == snack[1]:
                length_of_snake += 1 
                snacks.remove(snack)
                # Voeg nieuwe snacks toe als alle snacks zijn opgegeten
                if len(snacks) == 0:
                    num_snacks = random.randint(1, 4)
                    for _ in range(num_snacks):
                        snack_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
                        snack_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
                        snacks.append([snack_x, snack_y])
                        SNAKE_SPEED += 0.2
                # Verhoog het aantal levens
                # lives == EXTRA_LIVES
        # if length_of_snake += 1:
        #             SNAKE_SPEED += 0.2
                

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game()
