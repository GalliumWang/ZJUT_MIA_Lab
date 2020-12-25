import musicalbeeps
import sys
import pygame


player = musicalbeeps.Player(volume = 0.3,mute_output = False)


noteToPlay=sys.argv[1]
player.play_note(noteToPlay,100)

