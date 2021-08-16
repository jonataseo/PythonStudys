def convert_string_to_float(string_to_convert):
    """
    Return string_to_convert as a float if it can be a float. Raises an exception if can't
    :param string_to_convert: string.
    :return: float.
    """
    try:
        return float(string_to_convert)
    except(ValueError):
        print("Could not convert to float. CHeck your input")

correctly_usage_of_function = convert_string_to_float('10')
print(f"{correctly_usage_of_function}")

test_if_exception_works = convert_string_to_float("TEST")

