import math

class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.calculate_area()
        self.hypotenuse = self.calculate_hypotenuse()

    def calculate_area(self):
        return self.length * self.width

    def calculate_hypotenuse(self):
        return math.sqrt(self.length**2 + self.width**2)

    def display_info(self):
        print(f"Length: {self.length} cm")
        print(f"Width: {self.width} cm")
        print(f"Area: {self.area} square cm")
        print(f"Hypotenuse: {self.hypotenuse} cm")


# Example usage:
if __name__ == "__main__":
    length_input = float(input("Enter the length of the square in cm: "))
    width_input = float(input("Enter the width of the square in cm: "))

    square1 = Square(length_input, width_input)
    square1.display_info()