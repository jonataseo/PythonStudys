def divide_by_two(integer):
    """
    Returns integer divided by two
    :param integer: int.
    :return: int / 2
    """
    try:
        return int(integer) / 2
    except(ValueError):
        print(f"{integer} must be an integer")

def multiply_by_four(integer):
    """
    Return integer multiplied by four
    :param integer: int.
    :return: int * 4
    """
    return integer * 4

result = divide_by_two(10)
print(multiply_by_four(result))