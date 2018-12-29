from BeeAlgorithm import BeeAlgorithm, BeeType
import INI
from matplotlib import pyplot as plt
import time
from BeeAlgorithm import SelectPatch
from BeeAlgorithm import FitnessFunction
import numpy as np
import encoders

available_coins = INI.available_coins
statistical_day = INI.statistical_day
coins_to_save = INI.coins_to_save

max_iterations = INI.max_iterations
required_cost = sum(statistical_day) / 1000
expected_quantity_of_coins = INI.expected_quantity_of_coins
amount_of_scouts = INI.amount_of_scouts
amount_of_best_bees = INI.amount_of_best_bees
patch_size = INI.patch_size

population = []

# FIGURE
fig_width = 10
fig_height = 10


def validation_input_data():
    if (amount_of_scouts < 0 or
            amount_of_best_bees < 0 or
            patch_size < 0 or
            len(sorted(coins for coins in coins_to_save if coins <= 0)) or
            len(sorted(coins for coins in available_coins if coins <= 0)) or
            len(sorted(day for day in statistical_day if day <= 0))):
        return False

    return True


def plot_bar(time_of_performing_every_iter, select_type_patch):
    index = np.arange(len(select_type_patch))
    bar_width = 0.35
    for i in range(len(select_type_patch)):
        plt.bar(index[i]+bar_width, time_of_performing_every_iter[i], width=bar_width)
    plt.xticks(index+bar_width, select_type_patch)
    plt.title("Wpływ metody presuzkiwania otoczenia na czas obliczeń")
    plt.ylabel("Czas wykonywania się iteracji[t]")
    plt.xlabel("Metoda przeszukiwania otoczenia")
    plt.show()

if __name__ == '__main__':
    if validation_input_data():
        patch_type = SelectPatch()
        y_lim = []
        fitness_types = [FitnessFunction.QuantityOfCoins, FitnessFunction.ValueOfCoins]
        time_of_performing_iteration_for_each_type_patch = []
        selecting_type_patch = [patch_type.RandomColumns, patch_type.RandomCells, patch_type.IntelligentColumns,
                                patch_type.IntelligentCells]
        for fitness in fitness_types:
            #selecting_type_patch = [patch_type.IntelligentCells]
            plt.figure(figsize=(fig_width, fig_height))
            #time_plot = plt.figure(figsize=(fig_width/2, fig_height/2))
            for select_patch in selecting_type_patch:
                bee_algorithm = BeeAlgorithm(available_coins, coins_to_save, amount_of_scouts, amount_of_best_bees,
                                             expected_quantity_of_coins, statistical_day, patch_size,
                                             select_patch, fitness)
                bee_algorithm.generate_start_population()
                print(sum(bee_algorithm.statistical_day))
                time_of_performing_iterations =[]
                for i in range(max_iterations):
                    start = time.time()
                    bee_algorithm.perform_next_iteration()
                    if i == 0:
                        bee_algorithm.print_bees_solution()
                    end = time.time()
                    print('Time of performing iteration: ' + str(end - start) + '\n')
                    time_of_performing_iterations.append(end-start)
                plt.plot([_ for _ in range(max_iterations)], bee_algorithm.list_of_best_cost_solutions)
                time_of_performing_iteration_for_each_type_patch.append(sum(time_of_performing_iterations)/max_iterations)
                y_lim.append(bee_algorithm.list_of_best_cost_solutions[0])
                print (f'Method of selecting patch: {select_patch}')

            print(f'Method of fitness function: {fitness}')
            plt.legend(selecting_type_patch)
            plt.title('Bees Algorithm (BA)')
            plt.xlabel('iteration')
            plt.ylabel('fitness value')
            bee_algorithm.print_bees_solution()
            axes = plt.gca()
            axes.set_xlim([1, max_iterations])
            axes.set_ylim([0, max(y_lim) + 10])
            plt.show()
            plot_bar(time_of_performing_iteration_for_each_type_patch, selecting_type_patch)
            time_of_performing_iteration_for_each_type_patch = []
            #time_plot.title("Medium time of performing iteration for each selecting type patch")
            #time_plot = plt.legend(selecting_type_patch)
            #time_plot.show()
    else:
        print("Wrong input data")
        if amount_of_scouts < 0 :
            print (f'Wrong amount of scouts: {amount_of_scouts}')
        if amount_of_best_bees < 0 :
            print(f'Wrong amount of best bees: {amount_of_best_bees}')
        if patch_size < 0 :
            print(f'Wrong patch size: {patch_size}')
        if len(sorted(coins for coins in coins_to_save if coins <= 0)):
            print(f'Wrong coins to save: {coins_to_save}')
        if len(sorted(coins for coins in available_coins if coins <= 0)):
            print(f'Wrong available coins: {available_coins}')
        if len(sorted(day for day in statistical_day if day <= 0)):
            print(f'Wrong statistical day: {statistical_day}')


