from Population import Population
import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, data):
        self.pop_number = 500
        self.gen_number = 1000
        self.mutation_rate = 0.1
        nn_inputs = len(data[0][0])
        nn_outputs = np.amax(data[1])+1
        self.data = data
        self.pop = Population(self.pop_number, nn_inputs, nn_outputs)

        self.fitness_dict = {}
        self.combinantions = []

    def evaluation(self):
        self.fitness_dict = self.pop.get_fitness(self.data)
        #print(self.pop[max(self.fitness_dict, key=self.fitness_dict.get)])

    def selection(self):
        self.combinantions = []
        sumvalues = sum(self.fitness_dict.values())
        sorted_dict = {k: v/sumvalues for k, v in sorted(self.fitness_dict.items(), key=lambda item: item[1], reverse=True)}
        cumsum_norm_fit = np.cumsum(np.array(list(sorted_dict.values())))
        random_selection = []
        for _ in range(self.pop_number):
            aux = [np.argmin(np.abs(np.array(cumsum_norm_fit) < random.random())) for _ in range(2)]
            random_selection.append(aux)
        dict_items = list(sorted_dict.items())
        for p in random_selection:
            aux = [dict_items[i][0] for i in p]
            self.combinantions.append(aux)
        #print(self.fitness_dict)
        #print(self.combinantions)
        #exit()

    def reproduction(self):
        new_pop = []
        for c in self.combinantions:
            child = self.pop.reproduce(c)
            new_pop.append(child)
        self.pop.chromossomes = new_pop

    def mutation(self):
        for chrom in self.pop.chromossomes:
            if random.random() < self.mutation_rate:
                chrom.mutate()