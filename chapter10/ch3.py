class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2


if __name__ == "__main__":
    triangle = Triangle(5, 3)
    print(triangle.area())