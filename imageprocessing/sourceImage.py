from PIL import Image
from imageprocessing.segment import Segment


class SourceImage(Segment):

    def __init__(self, image: Image):
        width, height = image.size
        super().__init__(image, (0, 0), (width, height))
