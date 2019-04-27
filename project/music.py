import pygame


class Music():
    def __init__(self, x):
        pygame.mixer.init()
        pygame.mixer.music.load('music/'+x)
        pygame.mixer.music.set_volume(50)

    def update(self):
      # if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
