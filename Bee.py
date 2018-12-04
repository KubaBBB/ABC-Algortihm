import numpy as np
from encoders import *
from random import sample


class Bee:
    def __init__(self, bee_type):
        self.number_of_ways_to_give_change = 22
        self.number_of_used_bankotes_and_coins = 8
        self.solution_matrix = np.zeros((self.number_of_used_bankotes_and_coins, self.number_of_ways_to_give_change),
                                        dtype=int)
        self.cost = [10000]
        self.bee_type = bee_type;

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
        adjusted_available_coins = [i for i in adjusted_available_coins if i <= value];
        while temp != value:
            generated_value = np.random.choice(adjusted_available_coins)
            if temp + generated_value <= value:
                temp = temp + generated_value
                # print('generated value: ' + str(generated_value))
                # print('value: ' + str(value))
                # print('rows_encoder[generated_value]: ' + str(rows_encoder[generated_value]))
                # print('cols_encoder[value]: ' + str(cols_encoder[value]))
                self.solution_matrix[rows_encoder[generated_value]][cols_encoder[value]] += 1

    def search_food_with_patch_size(self, available_coins, patch_size):
        keys = list(rows_encoder.keys())
        patch = sorted(sample(range(22), patch_size), key=int)

        for column in patch:
            change = 0
            for row in range(rows_encoder.__len__()):
                if self.solution_matrix[row, column] != 0:
                    change += keys[row]*self.solution_matrix[row, column]
                    self.solution_matrix[row, column] = 0

            divided_change = [get_digit(change, 2) * 100,
                              get_digit(change, 1) * 10,
                              get_digit(change, 0)]
            adjusted_available_coins = list(filter(lambda x: x < 10 ** len(str(change)), available_coins))
            #print(divided_change)
            if divided_change[0] > 400:
                t = divided_change[0]/400
                for i in range(int(t)):
                    divided_change[0] -= divided_change[0]*t*400
            else:
                for value in divided_change:
                    self.divide_value(value, adjusted_available_coins)

    def set_to_be_onlooker(self):
        self.bee_type = BeeType.Onlooker;
        pass;

    def reload_solution_matrix(self):
        self.solution_matrix.fill(0)

    def print_cost(self):
        print('Bee cost: ' + str(self.cost))

    def print_solution(self):
        print('Solution: \n' + str(self.solution_matrix))


def get_digit(number, n):
    return number // 10 ** n % 10


class BeeType:
    Scout = "Scout";
    Onlooker = "Onlooker";