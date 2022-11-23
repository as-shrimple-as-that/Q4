# Section of crap I don't understand, copied from https://sites.google.com/ocsb.ca/ics2o/units/unit-5/unit-5-01

import pygame
from pygame import Color, Rect
from pygame import draw
from pygame import display
from math import pi #I understand this one, i put it in myself
SCREEN_SIZE = (500, 500)
pygame.init()
gameDisplay = display.set_mode(SCREEN_SIZE)

# Section of crap I do undedrstand
# Decided not to do transparency since my brain is melting

gameDisplay.fill(Color('teal'))
draw.arc(gameDisplay, (255,0,255), [200,200,250,200], pi/2, 7, 50)
draw.circle(gameDisplay, Color(0, 200, 177), (70, 200), (75))
draw.circle(gameDisplay, Color(255, 255, 50), (320, 250), (75))
draw.rect(gameDisplay, (255, 0, 0), [(500/2), (500/2), (500/3), (500/4)])
draw.rect(gameDisplay, (0, 255, 0), [(500/2), (500/2), (500/4), (500/5)])
draw.rect(gameDisplay, (0, 0, 255), [(500/2), (500/2), (500/5), (500/6)])
pygame.draw.polygon(gameDisplay, (200,60,25), ((75,0), (125,40), (175,0), (250, 100), (125,275), (0,100)))


# Two lines I don't understand, copied from https://sites.google.com/ocsb.ca/ics2o/units/unit-5/unit-5-01
display.flip()
input("Press enter to exit")