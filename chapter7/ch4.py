number_to_guess = [12, 61, 2, 34, 72]
while True:
    player_guess = input("Guess a number or q to quit: ")
    if(player_guess == "q"):
        break
    try:
        player_guess = int(player_guess)
    except(ValueError):
        print("Error. Type a number or q")
    if player_guess in number_to_guess:
        print("Correct")
        break
    else:
        print("Wrong")