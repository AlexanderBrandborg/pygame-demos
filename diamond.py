from collections import namedtuple
import pygame

DIMENSION = 255
Position = namedtuple('Position', ['x', 'y'])

class Grid:
    grid = []

    width = 1
    height = 1
    color = (0,0,0)
    thickness = 0

    def __init__(self):
        for _ in range(DIMENSION):
            self.grid.append([0] * DIMENSION)
        self.active_set = {Position(DIMENSION // 2, DIMENSION // 2)} # By only considering the set of blocks we might expand from, we can run in linear time

    def __is_free(self, position):
        return self.grid[position.x][position.y] == 0
    
    def __is_in_bounds(self, position):
        return 0 <= position.x and position.x < DIMENSION and 0 <= position.y and position.y < DIMENSION

    def update(self):
        updates = set() # Use update set to avoid mutating the collection we are iterating over
        for position in list(self.active_set):
            left = Position(position.x - 1, position.y)
            if(self.__is_in_bounds(left) and self.__is_free(left)):
                updates.add(left)

            right = Position(position.x + 1, position.y)
            if(self.__is_in_bounds(right) and self.__is_free(right)):
                updates.add(right)

            up = Position(position.x, position.y - 1)
            if(self.__is_in_bounds(up) and self.__is_free(up)):
                updates.add(up)

            down = Position(position.x, position.y + 1)
            if(self.__is_in_bounds(down) and self.__is_free(down)):
                updates.add(down)

        for update in updates:
            self.grid[update.x][update.y] = 1
            
        self.active_set = updates

    def display(self, screen):
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.grid[i][j] == 1:
                    visual = pygame.Rect(i, j, self.width, self.height)
                    pygame.draw.rect(screen, self.color, visual, self.thickness)

def main():
    pygame.init()
    pygame.display.set_caption("diamond")
    screen = pygame.display.set_mode((DIMENSION, DIMENSION))
    running = True
    grid = Grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        grid.update()
        grid.display(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
