import pygame

class Grid:
    grid = []

    width = 1
    height = 1
    color = (0,0,0)
    thickness = 0

    def __init__(self):
        for i in range(255):
            l = []
            for j in range(255):
                l.append(0)
            self.grid.append(l)
        self.grid[150][150] = 1
        self.activeSet = {(150,150)}

    def fill_update_naive(self, screen):
        updates = []
        for i in range(255):
            for j in range(255):
                if(self.grid[i][j] == 1):
                    if(i != 0):
                        updates.append((i-1, j))
                    if(i != 254):
                        updates.append((i+1, j))
                    if(j != 0):
                        updates.append((i, j-1))
                    if(j != 254):
                        updates.append((i, j+1))
        for u in updates:
            self.grid[u[0]][u[1]] = 1


    def fill_update_activeSet(self, screen):
        updates = set()
        for pos in list(self.activeSet):
            left = (pos[0]-1, pos[1])
            if(left[0] != 0 and self.grid[left[0]][left[1]] == 0):
                updates.add(left)

            right = (pos[0] + 1, pos[1])
            if(right[0] != 254 and self.grid[right[0]][right[1]] == 0):
                updates.add(right)

            up = (pos[0], pos[1] - 1)
            if(up[1] != 0 and self.grid[up[0]][up[1]] == 0):
                updates.add(up)

            down = (pos[0], pos[1] + 1)
            if(down[1] != 254 and self.grid[down[0]][down[1]] == 0):
                updates.add(down)

        for u in updates:
            self.grid[u[0]][u[1]] = 1
        
        self.activeSet = updates

    def display(self, screen):
        for i in range(255):
            for j in range(255):
                if(self.grid[i][j] == 1):
                    visual = pygame.Rect(i, j, self.width, self.height)
                    pygame.draw.rect(screen, self.color, visual, self.thickness)

def main():
    pygame.init()
    pygame.display.set_caption("Life2025")
    screen = pygame.display.set_mode((255, 255))
    running = True
    
    grid = Grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        grid.fill_update_activeSet(screen)
        grid.display(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()