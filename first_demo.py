import pygame

class Block:
    width = 30
    height = 30
    color = (0,0,0)
    thickness = 0
    initial_position = (0,0)
    def __init__(self, initial_position):
        x, y = initial_position
        self.position = initial_position
        self.visual = pygame.Rect(x, y, self.width, self.height)

    def update(self, screen):
        x, y = self.position
        inBounds = pygame.Rect(0, 0, 255, 255).collidepoint(x + 1, y + 1)
        if inBounds:
            self.position = (x + 1, y + 1)
            self.visual = pygame.Rect(*self.position, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.visual, self.thickness)
        else:
            self.position = (0, 0)
            self.visual = pygame.Rect(*self.position, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.visual, self.thickness)







def main():
    pygame.init()
    pygame.display.set_caption("First Demo")
    screen = pygame.display.set_mode((255, 255))
    running = True

    block = Block((0,0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        block.update(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()