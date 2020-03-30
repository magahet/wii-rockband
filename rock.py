import pygame
from pygame.locals import *

EVENTS = []

FREQ = 22100  # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 1  # 1 == mono, 2 == stereo
BUFFER = 16  # audio buffer size in no. of samples


def main():
    pygame.mixer.pre_init(FREQ, BITSIZE, CHANNELS, BUFFER)
    pygame.init()

    if pygame.joystick.get_count() > 1:
        print("You didn't plug in a joystick. FORSHAME!")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    sounds = {
        (0, 10): {"name": "blue", "sample": "sounds/drum_tom_mid_hard.wav"},
        (0, 11): {"name": "blue cymbal", "sample": "sounds/drum_cymbal_hard.wav"},
        (1, 10): {"name": "green", "sample": "sounds/drum_tom_lo_hard.wav"},
        (1, 11): {"name": "green cymbal", "sample": "sounds/drum_cymbal_open.wav"},
        (2, 10): {"name": "red", "sample": "sounds/drum_snare_hard.wav"},
        (3, 10): {"name": "yellow", "sample": "sounds/drum_tom_hi_hard.wav"},
        (3, 11): {"name": "yellow cymbal", "sample": "sounds/drum_cymbal_closed.wav"},
        (4, 4): {"name": "pedal", "sample": "sounds/drum_heavy_kick2.wav"},
    }

    for k, v in sounds.items():
        print(sounds[k].get("sample"))
        sounds[k]["sound"] = pygame.mixer.Sound(sounds[k].get("sample"))

    # The main game loop
    current_sound = None
    last_button_down = None
    while True:
        for event in pygame.event.get():
            if event.type == JOYBUTTONDOWN:
                if current_sound != None:
                    # current_sound.stop()
                    pass
                print("Button down: ", event.button)

                if event.button == 4:
                    sound = sounds[(4, 4)].get("sound")
                    sound.play()
                    continue

                buttons = (last_button_down, event.button)
                if buttons in sounds:
                    sound = sounds[buttons].get("sound")
                    sound.play()

                last_button_down = event.button

            if event.type == JOYBUTTONUP:
                print("Button up: ", event.button)
            if event.type == JOYHATMOTION:
                print("Hat: ", event.value)


main()
