'''El código está hecho para una demostración en un vídeo. Es una simplificación y no puedo asegurar que sea correcto científicamente.'''

import numpy as np
import math
import matplotlib.pyplot as plt
import pygame
import random

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
bg = 0, 0, 0
dim_cw = 10
dim_ch = 10

n_sites = 100
state = np.zeros((n_sites, n_sites))
T = int(input("Introduce a temperature: "))

for i in range(n_sites):
    for j in range(n_sites):
        if random.randint(0,1) > 0.5: # dipole spin up
            state[i, j] = 1
        else:
            state[i, j] = -1 # dipole spin down

'''plt.matshow(state);
plt.colorbar()
plt.show()'''

running = True

while running:
    for loop in range(1):
        #screen.fill(bg)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # detect ESC key
                if event.key == pygame.K_ESCAPE:
                    running = False
            mouse_click = pygame.mouse.get_pressed()

            if sum(mouse_click) > 0:
                pos_x, pos_y = pygame.mouse.get_pos()
                neigh = state[(pos_x + 1) % n_sites, (pos_y) % n_sites]+\
                        state[(pos_x) % n_sites, (pos_y + 1) % n_sites]+\
                        state[(pos_x) % n_sites, (pos_y - 1) % n_sites]+\
                        state[(pos_x - 1) % n_sites, (pos_y) % n_sites]
                print(neigh)

        #new_state = np.copy(state)         
        for i in range(n_sites):
            for j in range(n_sites):
                neigh = state[(i + 1) % n_sites, (j) % n_sites]+\
                        state[(i) % n_sites, (j + 1) % n_sites]+\
                        state[(i) % n_sites, (j - 1) % n_sites]+\
                        state[(i - 1) % n_sites, (j) % n_sites]
                energy = -state[i, j]*neigh
                delta_energy = state[i, j]*neigh - energy
                if delta_energy < 0:
                    #new_state[i, j] = -state[i, j]
                    state[i, j] *= -1
                else:
                    prob = np.exp(-delta_energy/T)
                    if random.uniform(0, 1) < prob:
                        #new_state[i, j] = -state[i, j]
                        state[i, j] *= -1
                        
                #state = np.copy(new_state)
    for i in range(n_sites):
        for j in range(n_sites):
            poly = [(i * dim_cw, j * dim_ch),
                    ((i + 1) * dim_cw, j * dim_ch),
                    ((i + 1) * dim_cw, (j + 1) * dim_ch),
                    (i * dim_cw, (j + 1) * dim_ch)]

            if state[i, j] == 1:
                pygame.draw.polygon(screen, (0, 0, 0), poly, 0)
            elif state[i, j] == -1:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    pygame.display.flip()


