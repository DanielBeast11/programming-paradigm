from .geometric_figure import Geometric_figure 
from .figure_color import Figure_color

class Rectangle(Geometric_figure):
    figure_type = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Figure_color(color)

    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return "{} {} цвета, шириной {}, высотой {}, площадью {:.2f}".format(
            self.figure_type, self.color.color, self.width, self.height, self.area()
        )