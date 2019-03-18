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
