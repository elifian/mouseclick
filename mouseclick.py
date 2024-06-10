import pygame
import sys
import os
from pynput import mouse

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
pygame.mixer.init()

# Используем файлы mouse1.mp3, mouse2.mp3, mouse3.mp3
sounds = {
    mouse.Button.left: pygame.mixer.Sound(resource_path('mouse1.mp3')),
    mouse.Button.right: pygame.mixer.Sound(resource_path('mouse2.mp3')),
    mouse.Button.middle: pygame.mixer.Sound(resource_path('mouse3.mp3')),
}

for sound in sounds.values():
    sound.set_volume(0.5)

def on_click(x, y, button, pressed):
    if pressed:
        if button in sounds:
            sounds[button].play()
        else:
            pass

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()