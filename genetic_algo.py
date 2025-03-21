import random

# Function to generate a random individual (chromosome)
def generate_individual():
    return [random.randint(0, 3) for _ in range(4)]

# Fitness function to evaluate the number of attacking pairs of queens
def fitness(individual):
    attacks = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j]:  # Same column
                attacks += 1
            elif abs(individual[i] - individual[j]) == abs(i - j):  # Same diagonal
                attacks += 1
    return attacks

# Selection function: Select the best individuals from the population
def selection(population, fitness_scores):
    selected_parents = random.choices(population, weights=[1 / (score + 1) for score in fitness_scores], k=2)
    return selected_parents

# Crossover function: Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function: Randomly change one queen's position
def mutate(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] = random.randint(0, 3)
    return individual

# Main Genetic Algorithm
def genetic_algorithm():
    population_size = 10
    generations = 100
    population = [generate_individual() for _ in range(population_size)]
    
    for generation in range(generations):
        fitness_scores = [fitness(individual) for individual in population]
        
        # Check if any individual has a fitness score of 0 (solution found)
        if 0 in fitness_scores:
            solution = population[fitness_scores.index(0)]
            print(f"Solution found in generation {generation}: {solution}")
            return solution
        
        new_population = []
        
        for _ in range(population_size // 2):
            # Select parents
            parent1, parent2 = selection(population, fitness_scores)
            
            # Perform crossover to create two children
            child1, child2 = crossover(parent1, parent2)
            
            # Perform mutation
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population
    
    print("No solution found after maximum generations.")
    return None

# Run the Genetic Algorithm
solution = genetic_algorithm()
