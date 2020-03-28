def crossover(chromosome1, chromosome2, i):
    return [f"{chromosome1[:i]}{chromosome2[i:]}", f"{chromosome2[:i]}{chromosome1[i:]}"]


# def crossover(chromosome1, chromosome2, index):
#     cross_chromosome1 = chromosome1[:index] + chromosome2[index:]
#     cross_chromosome2 = chromosome2[:index] + chromosome1[index:]
#     return [cross_chromosome1, cross_chromosome2]