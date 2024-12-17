from math import pi
from .geometric_figure import Geometric_figure 
from .figure_color import Figure_color

class Circle(Geometric_figure):
    figure_type = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Figure_color(color)
    
    def area(self):
        return pi*(self.radius ** 2)
    

    def __repr__(self):
        return "{} {} цвета, радиусом {}, площадью {:.2f}".format(
            self.figure_type, self.color.color, self.radius, self.area()
        )