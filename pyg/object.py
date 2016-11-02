from pygame import Rect

class MyRect:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = Rect(left, top, width, height)
