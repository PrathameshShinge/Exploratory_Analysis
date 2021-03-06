#Effect of radio waves on human brain

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import time

RD.seed()

width = 50
height = 50

def widthF (val=width):
    """
    Grid width.
    The parameter change is effective only when model is reset.
    """
    global width
    width = int(val)
    return val

def heightF (val=height):
    """
    Grid height.
    The parameter change is effective only when model is reset.
    """
    global height
    height = int(val)
    return val

def init():
    """*** Rumor Spread ***"""
    global time, config

    time = 0

    config = SP.zeros([height, width])
    config[RD.randrange(height), RD.randrange(width)] = 1

def draw():
    PL.cla()
    cmap = matplotlib.cm.Spectral
    cmap.set_under()
    PL.pcolor(config, vmin = 1, vmax = width + height, cmap = cmap)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, nextConfig
    if time <50:
        time += 1

    height, width = config.shape

    tmp = config.copy()
    if 10 <time <50:
        for x in range(width):
            for y in range(height):
                if config[y, x] > 0:
                    dx = RD.randint(-1, 1)
                    dy = RD.randint(-1, 1)
                    if tmp[(y+dy)%height, (x+dx)%width] == 0:
                        tmp[(y+dy)%height, (x+dx)%width] = time
        config = tmp
       # time += 1
       

import pycxsimulator
pSetters = [widthF,heightF]
pycxsimulator.GUI(parameterSetters = pSetters).start(func=[init,draw,step])
