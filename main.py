from BeeAlgorithm import BeeAlgorithm, BeeType
import INI
from matplotlib import pyplot as plt
import time
import encoders

available_coins = INI.available_coins
statistical_day = INI.statistical_day
coins_to_save = INI.coins_to_save

max_iterations = INI.max_iterations
required_cost = sum(statistical_day) / 1000
expected_quantity_of_coins = INI.expected_quantity_of_coins
amount_of_bees = INI.amount_of_bees
amount_of_best_bees = INI.amount_of_best_bees
patch_size = INI.patch_size

population = []

# FIGURE
fig_width = 10
fig_height = 10


def validation_input_data():
    if (amount_of_best_bees >= amount_of_bees or
            amount_of_bees < 0 or
            amount_of_best_bees < 0 or
            patch_size < 0 or
            len(sorted(coins for coins in coins_to_save if coins <= 0)) or
            len(sorted(coins for coins in available_coins if coins <= 0)) or
            len(sorted(day for day in statistical_day if day <= 0))):
        return False

    return True


if __name__ == '__main__':
    if validation_input_data():
        bee_algorithm = BeeAlgorithm(available_coins, coins_to_save, amount_of_bees, amount_of_best_bees,
                                     expected_quantity_of_coins, statistical_day, patch_size)
        bee_algorithm.generate_start_population();
        print(sum(bee_algorithm.statistical_day));
        for i in range(max_iterations):
            start = time.time()
            bee_algorithm.perform_next_iteration()
            if i == 0:
                bee_algorithm.print_bees_solution()
            end = time.time()
            print('Time of performing iteration: ' + str(end - start) + '\n')

        plt.figure(figsize=(fig_width, fig_height))
        plt.plot([_ for _ in range(max_iterations)], bee_algorithm.list_of_best_cost_solutions)
        plt.title('Artificial Bee Colony (ABC)')
        plt.xlabel('iteration')
        plt.ylabel('fitness value')
        bee_algorithm.print_bees_solution()
        axes = plt.gca()
        axes.set_xlim([1, max_iterations])
        axes.set_ylim([0, bee_algorithm.list_of_best_cost_solutions[0]])
        plt.show()
