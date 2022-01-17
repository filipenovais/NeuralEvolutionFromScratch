import random
random.seed(12)


def crossover(child, parent1, parent2):
    for i in range(len(parent1.genelist)):
        if random.random() < 0.5:
            child.genelist[i] = parent1.genelist[i]
        else:
            child.genelist[i] = parent2.genelist[i]

    return child


class NeuralNetwork:
    def __init__(self, n_inputs, n_outputs):
        self.genelist = [random.random(), random.random(), random.random()]

    def mutate(self):
        randomi = random.randint(0, len(self.genelist) - 1)
        self.genelist[randomi] = random.random()

    def fitness(self, data):
        fit = 3 - (abs(0.1 - self.genelist[0]) + abs(0.1 - self.genelist[1]) + abs(0.8 - self.genelist[2]))
        return fit

    def __str__(self):
        return str(self.genelist)
