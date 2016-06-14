from PIL import Image, ImageDraw
import random
import gtk

# reading screen resolution
screen_width = gtk.gdk.screen_width()
screen_height = gtk.gdk.screen_height()

# create new image
image = Image.new("RGB",(screen_width, screen_height), "white")

# square size
square_size = (20, 20)

# open up the image for manipulation
draw = ImageDraw.Draw(image, mode="RGB")

for i in range(0, screen_width+square_size[0], square_size[0]):
    for j in range(0, screen_height+square_size[1], square_size[1]):
        colours = [random.randint(0,255) for _ in range(3)]
        red = (colours[0]+255)/2
        green = (colours[1]+255)/2
        blue = (colours[2]+255)/2
        draw.rectangle( (i,j,20+i,20+j), fill=(red,green,blue) )

# write to STDOUT
image.save("pic.png")
