from Bee import Bee


class BeeAlgorithm:
    def __init__(self, available_coins, coins_to_save, amount_of_bees, amount_of_best_bees, expected_quantity_of_coins, statistical_day):
        self.available_coins = available_coins
        self.statistical_day = statistical_day
        self.coins_to_save = coins_to_save
        self.max_iterations = 200
        self.required_cost = sum(statistical_day) / 1000
        self.expected_quantity_of_coins = expected_quantity_of_coins
        self.amount_of_bees = amount_of_bees
        self.amount_of_bees_searching_patch = amount_of_best_bees

        self.population = []
        self.cost = []
        self.list_of_best_cost_solutions = []
        self.best_bee = None

    def generate_population(self):
        print('Population of bees created: ' + str(self.amount_of_bees))
        return [Bee() for _ in range(self.amount_of_bees)]

    def create_scout_bees(self, amount_of_scouts):
        print('Population of created scouts: ' + str(self.amount_of_bees-self.amount_of_bees_searching_patch))
        return [Bee() for _ in range(amount_of_scouts)]

    def perform_next_iteration(self):
        self.population = self.generate_population()
        self.search_best_bee()
        self.print_best_bee()
        self.update_population()
        self.print_amount_of_population()
        return

    def update_population(self):
        scouts = self.create_scout_bees(self.amount_of_bees - self.amount_of_bees_searching_patch)
        self.population += scouts

    def search_best_bee(self):
        for bee in self.population:
            bee.calculate_change_randomly(self.statistical_day, self.available_coins)
        self.best_bee = self.choose_best_bee(self.best_bee)

    def choose_best_bee(self, best):
        for bee in self.population:
            bee.calculate_bee_cost(self.coins_to_save, self.expected_quantity_of_coins)
        self.population = sorted(self.population, key=lambda x: x.cost)

        if not best or self.population[0].cost < best.cost:
            best_bee = self.population[0]
        else:
            best_bee = best
        self.list_of_best_cost_solutions.append(best_bee.cost)
        return best_bee

    def print_best_bee(self):
        if self.best_bee is not None:
            print('Best bee and its cost: ')
            self.best_bee.print_cost()
        else:
            print('Fail, get solution first')
        pass

    def print_amount_of_population(self):
        print('Population: ' + str(self.population.__len__()))
