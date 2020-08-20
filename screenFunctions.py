# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 07:26:43 2020

@author: Kanishk
"""

import pygame
import numpy as np
pygame.init()
import math
import time
import sys
import random

def rect(screen, color, x, y, w, h, fill=0):
    pygame.draw.rect(screen, color, (x, y, w, h), fill)

def square(screen, color, x, y, s, fill=0):
    rect(screen, color, x, y, s, s, fill)
    
def ellipse(screen, color, x, y, w, h, fill=0):
    pygame.draw.ellipse(screen, color, (x, y, w, h), fill)

def circle(screen, color, x, y, r, fill=0):
    ellipse(screen, color, x, y, r, r, fill)

def background(screen, color):
    rect(screen, color, 0, 0, WIDTH, HEIGHT)
    
def reset(n):
    board = [["" for i in range(n)] for j in range(n)]
    loop = True
    return board, loop, None, True