import sys
import random
import subprocess
import pygame as pg


square_size = (20, 20)

pg.init()


display_w = pg.display.Info().current_w
display_h = pg.display.Info().current_h


image = pg.Surface((display_w,display_h))
for i in range(0, display_w+square_size[0], square_size[0]):
    for j in range(0, display_h+square_size[1], square_size[1]):
        color = [random.randint(0,255) for _ in range(3)]
        rect = pg.Rect((i,j), square_size)
        image.fill(color, rect)


pg.image.save(image, 'pic.png')
subprocess.call(["feh","--bg-center","pic.png"])

pg.quit()
sys.exit()
