import numpy as np
from beeAlgorithm import BeeAlgorithm
from bee import Bee


available_coins = [1, 2, 5, 10, 20, 50, 100, 200]
statistical_day = np.random.randint(499, size=100)
coins_to_save = [2, 5, 20, 100]


max_iterations = 200
required_cost = sum(statistical_day) / 1000
expected_quantity_of_coins = [50, 25, 20, 10]
amount_of_bees = 100
food_source_position = 0;

population = []
fitness = []
training = []


if __name__ == '__main__':
    #bee_algorithm = BeeAlgorithm(available_coins, coins_to_save, amount_of_bees, expected_quantity_of_coins, statistical_day)
    for i in range(2):
        bee = Bee()
        bee.calculate_change_randomly(statistical_day, available_coins)
        bee.calculate_bee_cost(coins_to_save, expected_quantity_of_coins)
        bee.print_cost()
    #bee.print_solution()


def search_optimum():
    return 2;


def select_best_solution(best):
    return 1;


