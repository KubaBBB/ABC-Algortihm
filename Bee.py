import numpy as np
from encoders import *


class Bee:
    def __init__(self):
        self.number_of_ways_to_give_change = 22
        self.number_of_used_bankotes_and_coins = 8
        self.solution_matrix = np.zeros((self.number_of_used_bankotes_and_coins, self.number_of_ways_to_give_change))
        self.cost = [10000]

    def calculate_bee_cost(self, coins_to_save, expected_quantity_of_coins):
        value_of_rows = np.zeros(len(coins_to_save))
        difference = np.zeros(len(coins_to_save))
        for i in range(len(coins_to_save)):
            value_of_rows[i] = sum(self.solution_matrix[rows_encoder[coins_to_save[i]]])
            difference[i] = abs(value_of_rows[i] - expected_quantity_of_coins[i])
        self.cost = sum(difference)
        return self.cost

    def calculate_change_randomly(self, statistical_day, available_coins):
        for change in statistical_day:
            divided_change = [get_digit(change, 2) * 100,
                              get_digit(change, 1) * 10,
                              get_digit(change, 0)]
            adjusted_available_coins = list(filter(lambda x: x < 10 ** len(str(change)), available_coins))

            for value in divided_change:
                self.divide_value(value, adjusted_available_coins)

    def divide_value(self, value, adjusted_available_coins):
        temp = 0
        while temp != value:
            generated_value = np.random.choice(adjusted_available_coins)
            if temp + generated_value <= value:
                temp = temp + generated_value
                self.solution_matrix[rows_encoder[generated_value]][cols_encoder[value]] += 1

    def print_cost(self):
        print('Bee cost: ' + str(self.cost))

    def print_solution(self):
        print('Solution: \n' + str(self.solution_matrix))


def get_digit(number, n):
    return number // 10 ** n % 10
