import pygame
import sys
from bird import Bird
from pipe import Pipe
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird - Student Project")
        self.clock = pygame.time.Clock()

        # Load assets
        self.background = pygame.image.load("assets/background-day.png")
        self.base = pygame.image.load("assets/base.png")
        self.gameover_img = pygame.image.load("assets/gameover.png")
        self.message_img = pygame.image.load("assets/message.png")

        self.bird_frames = [
            pygame.image.load("assets/yellowbird-downflap.png"),
            pygame.image.load("assets/yellowbird-midflap.png"),
            pygame.image.load("assets/yellowbird-upflap.png")
        ]
        self.pipe_img = pygame.image.load("assets/pipe-green.png")

        # Load số điểm (0–9)
        self.digit_images = [pygame.image.load(f"assets/{i}.png") for i in range(10)]

        # Load sounds
        self.sound_hit = pygame.mixer.Sound("sound/hit.wav")
        self.sound_point = pygame.mixer.Sound("sound/point.wav")
        self.sound_wing = pygame.mixer.Sound("sound/wing.wav")
        self.sound_die = pygame.mixer.Sound("sound/die.wav")
        self.sound_swoosh = pygame.mixer.Sound("sound/swoosh.wav")

        self.reset()

    def reset(self):
        self.bird = Bird(50, SCREEN_HEIGHT//2, self.bird_frames)
        self.pipes = [Pipe(300, self.pipe_img)]
        self.score = 0
        self.running = True
        self.show_message = True

    def update(self):
        self.bird.move()
        for pipe in self.pipes:
            pipe.move()
            if pipe.collide(self.bird) or self.bird.y > SCREEN_HEIGHT-100:
                self.sound_hit.play()
                self.sound_die.play()
                self.running = False
            if pipe.top_rect.x + self.pipe_img.get_width() < 0:
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(SCREEN_WIDTH, self.pipe_img))
                self.score += 1
                self.sound_point.play()

    def draw_score(self):
        score_str = str(self.score)
        digits = [self.digit_images[int(ch)] for ch in score_str]
        total_width = sum(img.get_width() for img in digits)
        x = (SCREEN_WIDTH - total_width) // 2
        y = 50
        for img in digits:
            self.screen.blit(img, (x, y))
            x += img.get_width()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.bird.draw(self.screen)
        self.screen.blit(self.base, (0, SCREEN_HEIGHT-100))

        # Vẽ điểm bằng ảnh số
        self.draw_score()

        if self.show_message:
            self.screen.blit(self.message_img, (50, 150))

        if not self.running:
            self.screen.blit(self.gameover_img, (50, 200))

        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.running:
                        self.bird.jump(self.sound_wing, self.sound_swoosh)
                        self.show_message = False
                    else:
                        self.reset()

            if self.running and not self.show_message:
                self.update()
            self.draw()
            self.clock.tick(FPS)
