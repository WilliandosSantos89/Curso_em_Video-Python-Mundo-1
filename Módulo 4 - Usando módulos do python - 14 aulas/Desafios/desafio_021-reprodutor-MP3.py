print('=' *20, end=' ')
print('Desafio 021 - Reprodutor MP3', end=' ')
print('=' *20)

"""from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3('TÁ CHORANDO POR QUÊ_ Jeyzer Maia.mp3')
play(song)"""

import pygame

pygame.init()
pygame.mixer.music.load('TÁ CHORANDO POR QUÊ_ Jeyzer Maia.mp3')
pygame.mixer.music.play()