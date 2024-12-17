from .rectangle import Rectangle

class Square(Rectangle):
    figure_type="Квадрат"

    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)
    
    def __repr__(self):
        return "{} {} цвета, стороной {}, площадью {:.2f}".format(
            self.figure_type, self.color.color, self.width, self.area()
        )