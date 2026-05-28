import pygame
import random

class Pipe:
    GAP = 100
    SPEED = 3

    def __init__(self, x, pipe_img):
        self.x = x
        self.pipe_img = pipe_img
        self.height = random.randint(50, 250)
        self.top_rect = pipe_img.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = pipe_img.get_rect(midtop=(self.x, self.height + self.GAP))

    def move(self):
        self.top_rect.x -= self.SPEED
        self.bottom_rect.x -= self.SPEED

    def draw(self, surface):
        surface.blit(pygame.transform.flip(self.pipe_img, False, True), self.top_rect)
        surface.blit(self.pipe_img, self.bottom_rect)

    def collide(self, bird):
        return bird.get_rect().colliderect(self.top_rect) or bird.get_rect().colliderect(self.bottom_rect)
