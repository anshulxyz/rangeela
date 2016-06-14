# rangeela

## What is it?

**rangeela** in 'Hindi' means colourful. 
Rangeela is a little script to generate an image full of randomly coloured
squares, which you can set as your wallpaper or whatever you feel like.

## Quick Start

Installation requires [**`python2`**](https://docs.python.org/2/) obviously,
**gtk** for reading the screen resolution, and **PIL** ([Python Image Library](https://en.wikipedia.org/wiki/Python_Imaging_Library))

You can install all of them from your favorite package manager, if you are like
me using Arch(or Arch-like) then you can search your official repos using
```linux
sudo pacman -Ss
```

## Instructions

1. `$ git clone https://github.com/anshulc95/rangeela.git ~/rangeela`
2. `$ cd ~/rangeela`
3. `$ python2 rangeela.py`
4. Now your wallpaper is generated, you can use your preferred wallpaper manager
to set *this* as your wallpaper.

## Update in v1.1.0

I have replaced the *pygame* with *PIL(Python Image Library)* since it's better
maintained and is focused specially on image manipulation, thus giving me more
things to try with images.

I have faded the colours, tried to mute them down. By mixing them with the 'white'
colour, and then taking a average of them.

I have removed the feature of script setting the wallpaper for you, I realised
people have different application according to their taste which they use for
customizing their desktop, so setting wallpaper, I leave that to you.

You can find previous releases [here](https://github.com/anshulc95/rangeela/releases)

## Example 

This is what the wallpaper is going to look like:

![pic](https://raw.githubusercontent.com/anshulc95/rangeela/master/pic.png)

## Inspiration

[colorblobks](https://github.com/zzggbb/colorblocks)

## TODO:

1. Use `argparse` to get specific instructions
2. Add the wallpaper to Ubuntu's default Unity wallpaper manager

## Contact Me:

[twitter](https://twitter.com/anshulc95)
[GitHub](https://github.com/anshulc95)
