from NotNeuralNetwork import NeuralNetwork, crossover
#from NeuralNetwork import NeuralNetwork, crossover

class Population:
    def __init__(self, pop_number, nn_inputs, nn_outputs):
        self.pop_number = pop_number
        self.nn_inputs = nn_inputs
        self.nn_outputs = nn_outputs
        self.fitness_dict = {}
        self.number = pop_number
        self.chromossomes = [NeuralNetwork(nn_inputs, nn_outputs) for _ in range(pop_number)]

    def get_fitness(self, data):
        self.fitness_dict = {}
        for i in range(len(self.chromossomes)):
            fitness = self.chromossomes[i].fitness(data)
            self.fitness_dict[i] = fitness
        return self.fitness_dict

    def reproduce(self, combination):
        if combination[0] == combination[1]:
            return self.chromossomes[combination[0]]
        else:
            parent1 = self.chromossomes[combination[0]]
            parent2 = self.chromossomes[combination[1]]
            child = crossover(NeuralNetwork(self.nn_inputs, self.nn_outputs), parent1, parent2)
            return child

    def __getitem__(self, i):
        return self.chromossomes[i]

    def __str__(self):
        return str(self.chromossomes)