# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm
import sys

from SR1 import SoftwareRender
x = SoftwareRender('out.bmp')
x.glCreateWindow(600, 600)
x.glViewPort(0, 0, 599, 599)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)

#Polygon 1
x.line_brese(165, 380, 185, 360)
x.line_brese(185, 360,180, 330)
x.line_brese(180, 330, 207, 345)

x.line_brese(207, 345,233, 330)
x.line_brese(233, 330, 230, 360)
x.line_brese(230, 360,250, 380)

x.line_brese(250, 380, 220, 385)
x.line_brese(220, 385,205, 410)
x.line_brese(205, 410, 193, 383)

x.line_brese(193, 383,165, 380)
x.glFinish()
