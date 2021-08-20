class Shape():
    
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")
    
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, size_a, size_b):
        self.size_a = size_a
        self.size_b = size_b
    
    def calculate_perimeter(self):
        return (2 * self.size_a) + (2 * self.size_b)

class Square(Shape):

    def __init__(self, size):
        self.size = size
    
    def calculate_perimeter(self):
        return 4 * self.size
    
    def change_size(self, number):
        self.size += number


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    square = Square(3)

    print(rectangle.calculate_perimeter())
    print(square.calculate_perimeter())

    square.change_size(-1)
    print(square.calculate_perimeter())

    square.change_size(3)
    print(square.calculate_perimeter())

    square.what_am_i()
    rectangle.what_am_i()