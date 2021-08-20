class Horse:

    def __init__(self, height, weight, Rider):
        self.height = height
        self.weight = weight
        self.Rider = Rider
    

class Rider:

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":

    rider = Rider("Zezin")
    horse = Horse(23, 34, rider)
    print(horse.Rider.name)