import pygame
from random import randrange
import time
import os
import imageio
from collections import Counter

SCREEN_SIZE = 255

class Grid:
    current_grid = [0 for i in range(SCREEN_SIZE**2)]
    next_grid = [0 for i in range(SCREEN_SIZE**2)]
    active_cell_indexes = set()

    def __init__(self):
        for i in range(50000):
            index = randrange(SCREEN_SIZE ** 2)
            self.current_grid[index] = 1
            self.active_cell_indexes.add(index)


    def cycle(self):
        start_time_only_cycle = time.time()
        candidate_indexes = []

        for cell in self.active_cell_indexes:
            # Top
            top_index = cell - SCREEN_SIZE
            if 0 < top_index:
                candidate_indexes.append(top_index)

            # Top Right
            top_right_index = cell - SCREEN_SIZE + 1
            if 0 < top_right_index:
                candidate_indexes.append(top_right_index)

            # right
            right_index = cell + 1
            if right_index < SCREEN_SIZE ** 2 and (cell % SCREEN_SIZE) != 254:
                candidate_indexes.append(right_index)

            # Bottom right
            bottom_right_index = cell + SCREEN_SIZE + 1
            if bottom_right_index < SCREEN_SIZE**2 and (cell % SCREEN_SIZE) != 254:
                candidate_indexes.append(bottom_right_index)

            # Bottom
            bottom_index = cell + SCREEN_SIZE
            if bottom_index < SCREEN_SIZE**2:
                candidate_indexes.append(bottom_index)

            # Bottom Left
            bottom_left_index = cell + SCREEN_SIZE - 1
            if bottom_left_index < SCREEN_SIZE**2 and (cell % SCREEN_SIZE) != 0:
                candidate_indexes.append(bottom_left_index)

            # Left
            left_index = cell - 1
            if 0 < left_index and (cell % SCREEN_SIZE) != 0:
                candidate_indexes.append(left_index)

            # Top Left
            top_left_index = cell - SCREEN_SIZE - 1
            if 0 < top_left_index and (cell % SCREEN_SIZE) != 0:
                candidate_indexes.append(top_left_index)

        tallied_cells = Counter(candidate_indexes)
        next_active_cell_indexes = set()

        for cell_index in tallied_cells:
            neighbours = tallied_cells[cell_index]
            if self.current_grid[cell_index] and 1 < neighbours < 4:
                self.next_grid[cell_index] = 1
                next_active_cell_indexes.add(cell_index)

            elif self.current_grid[cell_index] == 0 and neighbours == 3 :
                self.next_grid[cell_index] = 1
                next_active_cell_indexes.add(cell_index)

        end_time_only_cycle = time.time()
        print("Elapsed exclusive cycle time was %g seconds" % (end_time_only_cycle - start_time_only_cycle))

        clear_time_start = time.time()
        self.current_grid, self.next_grid = self.next_grid, self.current_grid


        for cell in self.active_cell_indexes:
            self.next_grid[cell] = 0

        self.active_cell_indexes = next_active_cell_indexes

        clear_time_end = time.time()
        print("Clear time was %g seconds" % (clear_time_end - clear_time_start))
        d = "bug"


def draw_grid(grid, screen):
    for cell in grid.active_cell_indexes:
        pixel = pygame.Rect(cell % SCREEN_SIZE, cell / SCREEN_SIZE, 1, 1)
        pygame.draw.rect(screen, (0,0,0), pixel, 0)

def main():
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    screen = pygame.display.set_mode((255, 255))
    running = True

    grid = Grid()


    dir_name = "Captures/Life/" + str(int(time.time()))
    os.mkdir(dir_name)
    frame_num = 0
    filenames = []


    while running:
        #input()
        loop_start_time = time.time()

        screen.fill((255, 255, 255))
        draw_grid(grid, screen)
        #filename = dir_name + "/" + str(frame_num) + ".png"
        #filenames.append(filename)
        #pygame.image.save(screen, filename)
        frame_num += 1

        cycle_start_time = time.time()
        grid.cycle()
        cycle_end_time = time.time()
        print("Elapsed cycle time was %g seconds" % (cycle_end_time - cycle_start_time))

        update_start_time = time.time()
        pygame.display.update()
        update_end_time = time.time()
        print("Screen Update time was %g seconds" % (update_end_time - update_start_time))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        loop_end_time = time.time()

        print("Elapsed loop time was %g seconds" % (loop_end_time - loop_start_time))


    images = []
    for filename in filenames[10:]:
        images.append(imageio.imread(filename))
    imageio.mimsave(dir_name + '/movie.gif', images)

if __name__ == "__main__":
    main()