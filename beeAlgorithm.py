from bee import Bee


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
        self.fitness = []
        self.training = []
