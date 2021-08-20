class Hexagon:

    def __init__(self, side_size):
        self.side_size = side_size
    
    def perimeter(self):
        return 6 * self.side_size

if __name__ == "__main__":
    hexagon = Hexagon(6)
    print(hexagon.perimeter())