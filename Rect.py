class Rect:
    def __init__(self, a, b):
        self.x = a[0]
        self.y = a[1]
        self.w = b[0] - a[0]
        self.h = b[1] - a[1]

    def __str__(self):
        return 'Rect: ('+str(self.x)+', '+str(self.y)+'), ('+str(self.w)+', '+str(self.h)+')'