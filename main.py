import numpy as np
from BeeAlgorithm import BeeAlgorithm
import INI
from matplotlib import pyplot as plt


available_coins = INI.available_coins
statistical_day = INI.statistical_day
coins_to_save = INI.coins_to_save

max_iterations = INI.max_iterations
required_cost = sum(statistical_day) / 1000
expected_quantity_of_coins = INI.expected_quantity_of_coins
amount_of_bees = INI.amount_of_bees

population = []
fitness = []
training = []


###FIGURE
fig_width = 10
fig_height = 10
max_iterations = INI.max_iterations

if __name__ == '__main__':
    bee_algorithm = BeeAlgorithm(available_coins, coins_to_save, amount_of_bees, expected_quantity_of_coins, statistical_day)
    #     #bee_algorithm.population = bee_algorithm.generate_population()
    #     #for bee in bee_algorithm.population:
    #      #   bee.calculate_change_randomly(statistical_day, available_coins)
      #  bee.calculate_bee_cost(coins_to_save, expected_quantity_of_coins)
       # bee.print_cost()
    for i in range(max_iterations):
        bee_algorithm.search_best_bee()
        bee_algorithm.print_best_bee()
        print('\n\n')
        for bee in bee_algorithm.population:
            bee.print_cost()

    print(bee_algorithm.list_of_best_cost_solutions)
    plt.figure(figsize=(10,10))
    plt.plot([_ for _ in range(max_iterations)], bee_algorithm.list_of_best_cost_solutions)
    plt.title('WYKRES')
    plt.xlabel('xLABEL')
    plt.ylabel('yLABEL')
    plt.show()
        #bee.print_solution()


def search_optimum():
    return 2;


def select_best_solution(best):
    return 1;


