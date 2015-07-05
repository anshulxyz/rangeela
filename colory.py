import pygame as pg
from pygame.locals import *
import sys
from subprocess import call
from random import randint
import Tkinter as tk

root = tk.Tk()

pg.init()

displayx = root.winfo_screenwidth()
displayy = root.winfo_screenheight()

screen = pg.display.set_mode((displayx,displayy), 0, 0)

x = y = 0

while (x < displayx and y < displayy):
    pg.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x,y,20,20))
    x=x+20
    if(x >= displayx):
        y = y+20
        x = 0

pg.image.save(screen, 'pic.png')

call(["feh","--bg-center","pic.png"])

pg.quit()
sys.exit()
quit()
