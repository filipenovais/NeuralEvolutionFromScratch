from GeneticAlgorithm import GeneticAlgorithm
from nnfs.datasets import spiral_data, vertical_data
import numpy as np

def unison_shuffled(d):
    a, b = d
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]


if __name__ == '__main__':

    #data = np.random.rand(100, 2)
    #data = vertical_data(samples=20, classes=3)
    data = spiral_data(samples=20, classes=3)
    data = unison_shuffled(data)

    ga = GeneticAlgorithm(data)
    for gen_n in range(ga.gen_number):
        print('---------------------- GENERATION: ', gen_n+1)
        ga.evaluation()
        print('Maxfitness: ', max(list(ga.fitness_dict.values())))
        ga.selection()
        ga.reproduction()
        ga.mutation()
        print()

    print('FINISH')