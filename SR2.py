# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm
import sys

from SR1 import SoftwareRender
x = SoftwareRender('out.bmp')
x.glCreateWindow(1000, 800)
x.glViewPort(0, 0, 1000, 800)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)

#Polygon 1
"""
x.line_brese(165, 380, 185, 360)
x.line_brese(185, 360,180, 330)


x.line_brese(180, 330, 207, 345)
#x.monte_carlo(185, 360,180, 330)
#x.monte_carlo(185, 360, 207, 345)
x.line_brese(207, 345,233, 330)

x.line_brese(233, 330, 230, 360)
x.line_brese(230, 360,250, 380)

x.line_brese(250, 380, 220, 385)
x.line_brese(220, 385,205, 410)
x.line_brese(205, 410, 193, 383)

x.line_brese(193, 383,165, 380)
"""
a = x.read_poly('pol1.txt')
b = x.read_poly('pol2.txt')
c = x.read_poly('pol3.txt')
d = x.read_poly('pol4.txt')
e = x.read_poly('pol5.txt')
print("/////////")
print(a)
x.draw_poly(a)
x.draw_poly(b)
x.draw_poly(c)
x.draw_poly(d)
x.draw_poly(e)

x.monte_carlo3(a,True)
x.monte_carlo3(b,True)
x.monte_carlo3(c,True)
x.monte_carlo3(d,True)
x.monte_carlo3(e,False)
x.glFinish()
