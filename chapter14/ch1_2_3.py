class Square:
    squares_created = []
    # ch1
    def __init__(self, size):
        self.size = size
        self.squares_created.append(self.size)
    
    def calculate_perimeter(self):
        return self.size * 4
    # ch2
    def __repr__(self):
        return (f"{self.size} by {self.size} by {self.size} by {self.size}")
    # ch3
    def is_me(self, another):
        return self is another

if __name__ == "__main__":
    # ch1 test
    square_one = Square(2)
    square_two = Square(4)
    square_three = Square(8)
    print(Square.squares_created)

    # ch2 test
    print(square_one)
    print(square_two)
    print(square_three)

    # ch3 test
    print(square_one.is_me(square_two))
    another_one = square_one
    print(square_one.is_me(another_one))