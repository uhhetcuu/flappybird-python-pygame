import pygame

class Bird:
    def __init__(self, x, y, frames):
        self.x, self.y = x, y
        self.velocity = 0
        self.gravity = 0.5

        self.frame = 0
        self.frames = frames

        self.animation_count = 0

    def jump(self, sound_wing, sound_swoosh):
        self.velocity = -7
        sound_wing.play()
        sound_swoosh.play()

    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

        self.animation_count += 1

        if self.animation_count >= 8:
            self.frame = (self.frame + 1) % len(self.frames)
            self.animation_count = 0

    def draw(self, surface):
        surface.blit(self.frames[self.frame], (self.x, self.y))

    def get_rect(self):
        return self.frames[0].get_rect(topleft=(self.x, self.y))