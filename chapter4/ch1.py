def square(x):
    """
    Returns x squared.
    :param x: int or float.
    :return: int or float.
    """
    return x*x


try:
    number_to_square = int(input("type a number:"))
    print(square(number_to_square))
except(ValueError):
    print("Invalid input. Must be a integer")
    