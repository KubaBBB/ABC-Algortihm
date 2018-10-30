import numpy as np
from BeeAlgorithm import BeeAlgorithm
import INI

from Bee import Bee


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


if __name__ == '__main__':
    bee_algorithm = BeeAlgorithm(available_coins, coins_to_save, amount_of_bees, expected_quantity_of_coins, statistical_day)
    bee_algorithm.population = bee_algorithm.generate_population()
    for bee in bee_algorithm.population:
        bee.calculate_change_randomly(statistical_day, available_coins)
        bee.calculate_bee_cost(coins_to_save, expected_quantity_of_coins)
        bee.print_cost()
    #bee.print_solution()


def search_optimum():
    return 2;


def select_best_solution(best):
    return 1;


