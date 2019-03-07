# Carlos Calderon, 15219
# SR2 Lines
# Program that create a lines with bresenham algorithm
import sys

from SR1 import SoftwareRender
print(str(sys.argv[1]))
print(str(sys.argv[2]))
print(str(sys.argv[3]))
print(str(sys.argv[4]))
xo, yo, xf, yf = int(str(sys.argv[1])), int(str(sys.argv[2])), int(str(sys.argv[3])), int(str(sys.argv[4]))
x = SoftwareRender('out.bmp')
x.glCreateWindow(600, 600)
x.glViewPort(0, 0, 599, 599)
x.glClear()
x.glColor(1, 0, 0)
x.glVertex(0, 0)
x.line_brese(xo, yo, xf, yf)
x.glFinish()
