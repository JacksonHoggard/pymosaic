from math import sqrt
from PIL import Image


class Segment:

    def __init__(self, image: Image, pos: (int, int), size: (int, int)):
        self.image = image
        self.similarSegment = Segment
        self.posX, self.posY = pos
        self.width, self.height = size
        self.pix = image.load()
        self.average = (0, 0, 0)
        self.calcAverage()

    def calcAverage(self):
        counter = 0
        totalR, totalG, totalB = (0, 0, 0)
        for x in range(self.posX, self.posX + self.width):
            for y in range(self.posY, self.posY + self.height):
                temp = self.pix[x, y]
                totalR += temp[0]
                totalG += temp[1]
                totalB += temp[2]
                counter += 1
        totalR = round(totalR / counter)
        totalG = round(totalG / counter)
        totalB = round(totalB / counter)
        self.average = (totalR, totalG, totalB)

    def calcDistance(self, segment):
        return sqrt(pow(segment.average[0] - self.average[0], 2)
                    + pow(segment.average[1] - self.average[1], 2)
                    + pow(segment.average[2] - self.average[2], 2))
