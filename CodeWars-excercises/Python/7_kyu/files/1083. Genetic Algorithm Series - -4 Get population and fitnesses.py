def map_population_fit(population, _fitness):
    return [ChromosomeWrap(chromosome=chrm, fitness=_fitness(chrm)) for chrm in population]


# def mapPopulationFit(population, fitness):
#     return (ChromosomeWrap(chromosome, fitness(chromosome)) for chromosome in population)