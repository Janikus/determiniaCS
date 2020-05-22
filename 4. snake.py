# import libraries
import pygame
import time
import random


cells = int(input("Introduce size of window: "))


# draw a square function
def draw(x, y):
    poly = [(x * dim_cw, y * dim_ch),
            ((x + 1) * dim_cw, y * dim_ch),
            ((x + 1) * dim_cw, (y + 1) * dim_ch),
            (x * dim_cw, (y + 1) * dim_ch)]

    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)


# initialize pygame and screen
pygame.init()

width, height = 1000, 1000

screen = pygame.display.set_mode((width, height))

bg = 0, 0, 0
dead = 255, 0, 0
win = 255, 255, 0

screen.fill(bg)

nx_c = cells
ny_c = cells

dim_cw = width / nx_c
dim_ch = height / ny_c

# initialize variables and lists
time_step = 0.12
positions = [[0, 0]]
running = True
direction = "right"
food = []
new_food = True
length = 1
size = int(cells * 0.8)
sub_time = 0.05 / size

# main game execution loop
while running:
    screen.fill(bg)

    # detect key presses
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # detect arrows or WASD
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not direction == "left":
                direction = "right"
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not direction == "right":
                direction = "left"
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and not direction == "down":
                direction = "up"
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not direction == "up":
                direction = "down"
            # detect ESC key
            if event.key == pygame.K_ESCAPE:
                running = False

    # generate food
    if new_food:
        food = positions[0]
        while food in positions:
            food = [random.randrange(0, nx_c), random.randrange(0, ny_c)]
        new_food = False

    if positions[-1] == food:
        new_food = True
        if length < size:
            length += 1
            time_step -= sub_time
        else:
            # after 40 foods eaten, the player wins
            print("YOU WON!")
            screen.fill(win)
            pygame.display.flip()
            running = False
            time.sleep(2)
            break

    # only draw food if it has not been gotten
    if not new_food:
        draw(food[0], food[1])

    # player looses if the snake eats his own tail
    if positions[-1] in positions[-length:-1]:
        print("GAME OVER")
        screen.fill(dead)
        pygame.display.flip()
        running = False
        time.sleep(2)
        break

    # wait a given time
    time.sleep(time_step)

    # append new position to list depending on the current direction of the snake
    if direction == "right":
        positions.append([(positions[-1][0] + 1) % nx_c, positions[-1][1]])
    if direction == "left":
        positions.append([(positions[-1][0] - 1) % nx_c, positions[-1][1]])
    if direction == "up":
        positions.append([positions[-1][0], (positions[-1][1] - 1) % ny_c])
    if direction == "down":
        positions.append([positions[-1][0], (positions[-1][1] + 1) % ny_c])

    # do not save more than 40 positions, as it is unnecessary, at 40 you win
    if len(positions) > size:
        positions = positions[1:]

    # draw the corresponding positions depending on snake length
    for pos in positions[-length:]:
        draw(pos[0], pos[1])

    # update screen with changes
    pygame.display.flip()
