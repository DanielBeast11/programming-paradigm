from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Style

def main():
    n = 1

    rectangle = Rectangle(n, n, "синего")
    print(Fore.BLUE + str(rectangle))

    circle = Circle(n, "зеленого")
    print(Fore.GREEN + str(circle))

    square = Square(n, "красного")
    print(Fore.RED + str(square) + Style.RESET_ALL)

if __name__ == "__main__":
    main()
