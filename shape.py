# import math if I we want use  (math.pi) for the area!

class Shape:
    def __init__(self):
        self.unit = "meters"
        self.pi = 3.14169

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        pass

    # the methods under Shape class are empty cause cicle and rectangel has thier own implementation for this!

# subclasses !!!!!!
class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

        # call the display function method during the __init__
        self.display()

    def area(self):

        # A = π * r^2
        # return the value and store in the area...BASIC!!!!
        return self.pi * self.r * self.r

    def perimeter(self):

        # C = 2 * π * r
        # BASIC AGAIN!!!!
        return  2 * self.pi * self.r

    def display(self):

        # Cicle = 5 (self.unit) that equals to meters
        print(f"Circle-Radius: {self.r} {self.unit}")

        # :.2f will display the 2 decimal number because it is a flot number!
        print(f"Area: {self.area():.2f} meter squared")

        # {} access the self.unit so that it can print!
        print(f"Perimeter: {self.perimeter():.2f} {self.unit}")

    # display() wrong!

# subclasses 
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h
        self.display()

    def area(self):
        # A = L * W
        return self.h * self.w
        
    def perimeter(self):
        # P = 2L + 2W
        return 2 * self.h + 2 *self.w

    def display(self):
        print("####################################")
        print(f"Rectangle-Width:{self.w}, Height:{self.h}")
        print(f"Area: {self.area()} {self.unit} squared")
        print(f"Perimeter: {self.perimeter()} {self.unit}")


circle = Circle(5)
rectangle = Rectangle(4,6)

