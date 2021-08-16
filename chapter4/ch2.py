def print_string(string_to_print):
    """
    Prints a string, but only if it really is a string.
    :param string_to_print: string
    """
    if type(string_to_print) is str:
            print(string_to_print)
    else:
        print("Must be a string")

print_string("Joaozinho")
print_string('Mariazinha')
print_string(10)