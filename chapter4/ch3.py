def optional_parameters_function(param1, param2, param3, param4_opt=1, param5_opt=1):
    """
    Print the value of the param to demonstrate the usage of optional paramenters
    """
    print(f"The {param1}, {param2} and {param3} are required. {param4_opt} and {param5_opt} are optional")

optional_parameters_function(2, 2, 2)