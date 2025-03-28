
import pygame

def deer_noises(detected):
    pygame.mixer.init()
    pygame.mixer.music.load("INSERT_FILE_NAME") # Load audio file
    pygame.mixer.set_volume(0.7) # Arbitary volume control
    # Play sound when specified condition met
    if (detected == 1):
        pygame.mixer.music.play()