from Bee import Bee


class BeeAlgorithm:
    def __init__(self, available_coins, coins_to_save, amount_of_bees, expected_quantity_of_coins, statistical_day):
        self.available_coins = available_coins
        self.statistical_day = statistical_day
        self.coins_to_save = coins_to_save
        self.max_iterations = 200
        self.required_cost = sum(statistical_day) / 1000
        self.expected_quantity_of_coins = expected_quantity_of_coins
        self.amount_of_bees = amount_of_bees

        self.food_source_position = 0
        self.population = []
        self.cost = []
        self.list_of_best_solutions = []
        self.best_bee = None

    def generate_population(self):
        return [Bee() for _ in range(self.amount_of_bees)]

    def search_best_bee(self):
        self.population = self.generate_population()
        for bee in self.population:
            bee.calculate_change_randomly(self.statistical_day, self.available_coins)
        self.best_bee = self.choose_best_bee(self.best_bee)

    def choose_best_bee(self, best):
        for bee in self.population:
            bee.calculate_bee_cost(self.coins_to_save, self.expected_quantity_of_coins)
            bee.print_cost()
        self.population = sorted(self.population, key=lambda x: x.cost)
        self.list_of_best_solutions.append(self.population[0])
        if not best or self.population[0].cost < best.cost:
            best_bee = self.population[0]
        else:
            best_bee = best
        return best_bee

    def calculate_cost_for_population(self):
        for bee in self.population:
            bee.calculate_change_randomly(self.statistical_day, self.available_coins)
            bee.calculate_bee_cost(self.coins_to_save, self.expected_quantity_of_coins)

    def print_best_bee(self):
        if self.best_bee is not None:
            print('Best bee and its cost: ')
            self.best_bee.print_cost()
        else:
            print('Fail, get solution first')
        pass
