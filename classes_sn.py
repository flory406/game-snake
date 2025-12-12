import random
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

CELL_SIZE = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        cols = SCREEN_WIDTH // CELL_SIZE
        rows = SCREEN_HEIGHT // CELL_SIZE
        self.position = (random.randint (0, cols - 1) * CELL_SIZE,
                         random.randint (0, rows - 1) * CELL_SIZE)
        
    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.alive = True

    def draw(self, surface):
        for segment in self.body:
            x = segment[0]
            y = segment[1]
            pygame.draw.rect(surface, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    def memory_move(self, food_position):
        if not self.alive:
            return False
        
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
            new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            self.alive = False
            return False
        
        if new_head in self.body:
            self.alive = False
            return False
        
        self.body.insert(0, new_head)
        eaten = (new_head == food_position)
        if not eaten:
            self.body.pop()
        return eaten
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.direction != (CELL_SIZE, 0):
            self.direction = (-CELL_SIZE, 0)
        if keys[pygame.K_RIGHT] and self.direction != (-CELL_SIZE, 0):
            self.direction = (CELL_SIZE, 0)
        if keys[pygame.K_UP] and self.direction != (0, CELL_SIZE):
            self.direction = (0, -CELL_SIZE)
        if keys[pygame.K_DOWN] and self.direction != (0, -CELL_SIZE):
            self.direction = (0, CELL_SIZE)