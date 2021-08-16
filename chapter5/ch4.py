def ask_about_me():
    """
    Returns a dict about the stuff i like
    :return: dict.
    """
    stuff_i_like = {}
    
    height = input("Height: ")
    stuff_i_like["height"] = float(height)

    favorite_author = input("Favorite Author: ")
    stuff_i_like["favorite_author"] = favorite_author

    favorite_color  = input("Favorite Color: ")
    stuff_i_like["favorite_color"] = favorite_color

    return stuff_i_like

my_favs = ask_about_me()
print(my_favs)