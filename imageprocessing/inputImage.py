from math import floor
from PIL import Image
from imageprocessing.segment import Segment


class InputImage:

    def __init__(self, image: Image):
        self.segments = []
        self.image = image
        self.makeSegments()

    def makeSegments(self):
        divNumW = self.findDivNum(self.image.width)
        divNumH = self.findDivNum(self.image.height)
        segmentWidth = floor(self.image.width / divNumW)
        segmentHeight = floor(self.image.height / divNumH)
        for x in range(0, divNumW):
            for y in range(0, divNumH):
                self.segments.append(Segment(self.image, (x * segmentWidth, y * segmentHeight), (segmentWidth, segmentHeight)))

    def findDivNum(self, number: int):
        maxDiv = 1
        for x in range(1, 100):
            if number % x == 0:
                maxDiv = x
        if maxDiv < 16:
            maxDiv = 64
        return maxDiv

    def compareAverages(self, sourceImages: []):
        for segment in self.segments:
            minDistance = 256
            for image in sourceImages:
                temp = segment.calcDistance(image)
                if temp < minDistance:
                    minDistance = temp
                    segment.similarSegment = image

    def makeMosaic(self):
        mosaic = Image.new('RGB', self.image.size)
        for segment in self.segments:
            temp = segment.similarSegment.image
            temp = temp.resize((segment.width, segment.height))
            mosaic.paste(temp, (segment.posX, segment.posY))
        return mosaic
