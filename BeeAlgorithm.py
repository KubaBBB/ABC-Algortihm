from Bee import *
from copy import deepcopy
import encoders


def generate_population(bee_type, num_of_bees):
    print('Population created. Amount: ' + str(num_of_bees) + ' Type of bees: ' + bee_type)
    return [Bee(bee_type) for _ in range(num_of_bees)]


class BeeAlgorithm:
    def __init__(self, available_coins, coins_to_save, amount_of_bees, amount_of_best_bees, expected_quantity_of_coins,
                 statistical_day, patch_size):
        self.available_coins = available_coins
        self.statistical_day = statistical_day
        self.coins_to_save = coins_to_save
        self.required_cost = sum(statistical_day) / 1000
        self.expected_quantity_of_coins = expected_quantity_of_coins
        self.amount_of_bees = amount_of_bees
        self.amount_of_bees_searching_patch = amount_of_best_bees
        self.patch_size = patch_size
        self.population = []
        self.list_of_best_cost_solutions = []
        self.best_bee = None

    def generate_start_population(self):
        self.population = generate_population(BeeType.Scout, self.amount_of_bees);
        return

    def create_scout_bees(self, amount_of_scouts):
        print('Population of created scouts: ' + str(self.amount_of_bees-self.amount_of_bees_searching_patch))
        return [Bee(BeeType.Scout) for _ in range(amount_of_scouts)]

    def calculate_change(self):
        for bee in self.population:
            if bee.bee_type == BeeType.Scout:
                print('hey')
                bee.calculate_change_randomly(self.statistical_day, self.available_coins);
            elif bee.bee_type == BeeType.Onlooker:
                bee.search_food_with_patch_size(self.available_coins, self.patch_size);

    def perform_next_iteration(self):
        self.calculate_change()
        self.calculate_fitness_cost()
        self.best_bee = self.choose_best_bee(self.best_bee)
        self.print_best_bee()
        self.update_population()
        self.reload_solution()
        self.print_amount_of_population()
        return

    def update_population(self):
        onlookers = 0;
        for bee in self.population:
            if bee.bee_type == BeeType.Onlooker:
                onlookers+=1;
        if onlookers == 0:
            onlooker_bees = [deepcopy(self.best_bee) for _ in range(self.amount_of_bees_searching_patch)]
            for bee in onlooker_bees:
                bee.set_to_be_onlooker();
            self.population += onlooker_bees;

    def reload_solution(self):
        for bee in self.population:
            bee.reload_solution_matrix();

    def calculate_fitness_cost(self):
        for bee in self.population:
            bee.calculate_bee_cost(self.coins_to_save, self.expected_quantity_of_coins)
        self.population = sorted(self.population, key=lambda x: x.cost)

    def choose_best_bee(self, best):
        if not best or self.population[0].cost < best.cost:
            best_bee = deepcopy(self.population[0])
        else:
            best_bee = best
        self.list_of_best_cost_solutions.append(best_bee.cost)
        return best_bee

    def search_best_bee(self):
        for bee in self.population:
            bee.calculate_change_randomly(self.statistical_day, self.available_coins)
        self.best_bee = self.choose_best_bee(self.best_bee)

    def print_best_bee(self):
        if self.best_bee is not None:
            print('Best bee and its cost: ')
            self.best_bee.print_cost()
        else:
            print('Fail, get solution first')
        pass

    def print_amount_of_population(self):
        print('Population: ' + str(self.population.__len__()))

    def print_bees_solution(self):
        print('onlookers' + str(sum((i.bee_type == BeeType.Onlooker) for i in self.population)))
        print('Scouts' + str(sum((i.bee_type == BeeType.Scout) for i in self.population)))
        print('sekowska: ' + str(sum(sum(self.best_bee.solution_matrix))))
        change = 0;
        r = list(encoders.rows_encoder.keys());
        for column in range(encoders.cols_encoder.values().__len__()):
            for row in range(encoders.rows_encoder.__len__()):
                if self.best_bee.solution_matrix[row, column] != 0:
                   change += r[row] * self.best_bee.solution_matrix[row, column];
        print('solution: ' + str(change))
