class Figure_color:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
