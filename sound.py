#sound
import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.correct = pygame.mixer.Sound("correct.wav")
        self.gameover = pygame.mixer.Sound("gameover.wav")

    def play_correct(self):
        self.correct.play()

    def play_gameover(self):
        self.gameover.play()