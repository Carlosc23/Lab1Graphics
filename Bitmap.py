# Carlos Calderon, 15219
# Bitmap.py
# Inspired in the class render made in Graphics Course C3044
import math
import random
import struct
import sys

from math import ceil
#import numpy as np  # importando numpy


def char(c):
    return struct.pack("=c", c.encode('ascii'))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([b, g, r])


def read_poly(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    vertices = []
    for line in lines:
        if line:
            prefix, value = line.split(' ', 1)
            if prefix == 'v':
                vertices.append(list(map(int, value.split(' '))))
    return vertices


class Bitmap(object):
    """
    Class that abstract a bitmap
    """

    def __init__(self, width, height):
        """
        Constructor that initialize necessary variables for
        render images
        :param width: width of the image that will be render
        :param height: height of the image that will be render
        """
        self.width = width
        self.height = height
        self.pixels = []
        self.r = 255
        self.g = 0
        self.b = 0
        self.pointSize = 2
        self.vr = 255
        self.vg = 200
        self.vb = 200
        self.glclear()

    def glclear(self):
        """
        Fill the the pixels object with a color
        :return:
        """
        self.pixels = [
            [color(self.r, self.g, self.b) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glViewPort(self, x, y, width, height):
        """
        Define the area of the image where the glVertex will draw
        :param x: number that represent the horizontal coord where the viewport will be drawn
        :param y: number that represent the vertical coord where the viewport will be drawn
        :param width: width of the viewport
        :param height: heigth of the viewport
        :return:
        """
        if height <= 0 or width <= 0:
            print('Height and width must be positives')
        elif x < 0 or y < 0 or x > self.width or y > self.height:
            print('x and y must be positives and smaller tha height and width')
        else:
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x
            self.vpY = y

    def glClearColor(self, r, g, b):
        """
        change the default colors that uses glClear to fill
        :param r: amount of red
        :param g: amount of green
        :param b: amount of blue
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.r = ceil(r * 255)
            self.g = ceil(g * 255)
            self.b = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def glVertex(self, x, y):
        """
        Change the color of a point of the screen, relative to ViewPort
        :param x: relative horizontal coord of the point
        :param y: relative vertical coord of the point
        :return:
        """
        #print("pointSize")
        #print(self.pointSize)
        if self.vpHeight != 0 and self.vpWidth != 0:
            xx = x * ((self.vpWidth - self.pointSize) / 2)
            yy = y * ((self.vpHeight - self.pointSize) / 2)
            localX = self.vpX + int((self.vpWidth - self.pointSize) / 2) + int(xx)
            localY = self.vpY + int((self.vpHeight - self.pointSize) / 2) + int(yy)
            #print(x, y, localX, localY)
            for x in range(self.pointSize):
                for y in range(self.pointSize):
                    self.point(localX + x, localY + y, color(self.vr, self.vb, self.vg))
        else:
            print('Initialize glViewPort')
            sys.exit()

    def set_point_size(self, pointSize):
        """
        change the size of the global point, default is 5
        :param pointSize: size of the class point
        :return:
        """
        self.pointSize = pointSize

    def glColor(self, r, g, b):
        """
        Change the color of glVertex
        :param r: amount of red
        :param g: amount of green
        :param b: amount of b
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.vr = ceil(r * 255)
            self.vg = ceil(g * 255)
            self.vb = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def write(self, filename):
        """
        Save the image in a file
        :param filename: name of the file that will be saved
        :return:
        """
        f = open(filename, 'bw')

        # file header (14)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header (40)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
        f.close()

    def point(self, x, y, color=color(255, 200, 200)):
        """
        function that fills a pixel of a color
        :param x: position of the pixel
        :param y: position of the pixel
        :param color: color that will fill the pixel
        :return:
        """
        self.pixels[y][x] = color

    def square(self, size):
        cordx = int((self.vpWidth / 2)) - int(size / 2)
        cordy = int((self.vpWidth / 2)) - int(size / 2)
        for x in range(cordx, cordx + size):
            for y in range(cordy, cordy + size):
                self.point(x, y)

    def drawLeftLine(self, padding):
        x = padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawRightLine(self, padding):
        x = self.vpWidth - padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawTopLine(self, padding):
        y = padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def drawBottomLine(self, padding):
        y = self.vpHeight - padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def diagonal(self):
        for cord in range(self.vpX, self.vpWidth):
            self.point(cord, cord)

    def random_point(self):
        whiteColor = [1, 1, 1]
        blackColor = [0, 0, 0]
        for y in range(self.height):
            for x in range(self.width):
                self.glColor(*random.choice([whiteColor, blackColor]))
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def random_point_color(self):

        for y in range(self.height):
            for x in range(self.width):
                list_random = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                list_random_norm = [float(i) / 255 for i in list_random]
                self.glColor(list_random_norm[0], list_random_norm[1], list_random_norm[2])
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def sky(self, stars):
        counter = 0
        while counter < stars:
            counter += 1
            size = random.randint(1, 3)
            x = random.randint(0, self.vpWidth - size - 2)
            y = random.randint(0, self.vpHeight - size - 2)
            self.printStar(x, y, size)

    def printStar(self, x, y, size):
        for cordX in range(size):
            for cordY in range(size):
                self.point(cordX + x, cordY + y)

    def transform_x(self, x):
        dx = x * (self.vpWidth / 2)
        realX_vp_size = (self.vpWidth / 2) + dx
        realX = realX_vp_size + self.vpX
        return realX

    def transform_y(self, y):
        dy = y * (self.vpHeight / 2)
        realY_vp_size = (self.vpHeight / 2) + dy
        realY = realY_vp_size + self.vpY
        return realY

    def transform_xn(self, realX):
        realX_vp_size = realX - self.vpX
        dx = realX_vp_size - ((self.vpWidth / 2))
        x = dx / (self.vpWidth / 2)
        return x

    def transform_yn(self, realY):
        realY_vp_size = realY - self.vpY
        dy = realY_vp_size - ((self.vpHeight / 2))
        y = dy / (self.vpHeight / 2)
        return y

    def line(self, xo, yo, xf, yf):

        x1 = math.floor(xo)
        x2 = math.floor(xf)
        y1 = math.floor(yo)
        y2 = math.floor(yf)

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        if dx == 0:
            print("Undefined slope")
            sys.exit()
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx

        y = y1
        for x in range(x1, x2 + 1):
            if steep:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += 1 * 2 * dx

    def draw_poly(self, vertices):

        size_list_vertices = len(vertices)
        for i in range(size_list_vertices):
            xo, yo = vertices[i]
            if i == size_list_vertices - 1:
                xf, yf = vertices[0]
            else:
                xf, yf = vertices[i + 1]
            self.line(xo, yo, xf, yf)

    def div_vertices(self, vertices):
        list_x = []
        list_y = []
        size_list_vertices = len(vertices)
        for i in range(size_list_vertices):
            xo, yo = vertices[i]
            list_x.append(xo)
            list_y.append(yo)
        return list_x, list_y

    def draw_poly2(self, vertices):
        linesx = []
        linesy = []
        size_list_vertices = len(vertices)
        for i in range(size_list_vertices):
            xo, yo = vertices[i]
            if i == size_list_vertices - 1:
                xf, yf = vertices[0]
            else:
                xf, yf = vertices[i + 1]
            linesx.append([xo, xf])
            linesy.append([yo, yf])
        return linesx, linesy


    def point_polygon(self, vertices, polyX, polyY, x, y):
        i = 0
        j = vertices - 1
        oddNodes = False
        for i in range(0, vertices, 1):
            if ((polyY[i] < y and polyY[j] >= y
                 or polyY[j] < y and polyY[i] >= y)
                    and (polyX[i] <= x or polyX[j] <= x)):
                if (polyX[i] + (y - polyY[i]) / (polyY[j] - polyY[i]) * (polyX[j] - polyX[i]) < x):
                    oddNodes = not oddNodes
            j = i
        return oddNodes

    def monte_carlo_method3(self, vertices,color=False):
        if color:
            self.glColor(1, 1, 1)
        else:
            self.glColor(1, 0, 0)
        print("--------------------")
        print(len(vertices))
        vertices_size = len(vertices)
        list_x, list_y = self.div_vertices(vertices)
        lim_xo2, lim_xf2 = min(list_x), max(list_x)
        lim_yo2, lim_yf2 = min(list_y), max(list_y)
        lim_xo2, lim_xf2 = self.transform_xn(lim_xo2), self.transform_xn(lim_xf2)
        lim_yo2, lim_yf2 = self.transform_yn(lim_yo2), self.transform_yn(lim_yf2)
        listax, listay = self.draw_poly2(vertices)

        listax = list(map(lambda x: self.transform_xn(x), list_x))
        listay = list(map(lambda y: self.transform_yn(y), list_y))
        print(listax)
        print(listay)
        for i in range(250000):
            x = random.uniform(lim_xo2, lim_xf2)
            y = random.uniform(lim_yo2, lim_yf2)
            a = self.point_polygon(vertices_size, listax, listay, x, y)
            if a:
                self.glVertex(x, y)