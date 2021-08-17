question = input("Whats your age? ")

with open("anwser.txt", "w") as f:
    f.write(question)