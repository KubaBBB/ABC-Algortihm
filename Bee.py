import numpy as np
from encoders import *
from random import sample


class Bee:
    def __init__(self, bee_type):
        self.number_of_ways_to_give_change = 22
        self.number_of_used_banknotes_and_coins = 8
        self.solution_matrix = np.zeros((self.number_of_used_banknotes_and_coins, self.number_of_ways_to_give_change), dtype=int)
        self.solution = np.sum(self.solution_matrix)
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

    def calculate_bee_cost_modifided_fitness(self, coins_to_save, expected_quantity_of_coins):
        value_of_rows = np.zeros(len(coins_to_save), dtype = int)
        difference = np.zeros(len(coins_to_save))
        for i in range(len(coins_to_save)):
            value_of_rows[i] = sum(self.solution_matrix[rows_encoder[coins_to_save[i]]]) * coins_to_save[i]
        self.cost = sum(value_of_rows)
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
                self.solution_matrix[rows_encoder[generated_value]][cols_encoder[value]] += 1

    def search_food_with_patch_size_by_random_column(self, available_coins, patch_size):
        keys = list(rows_encoder.keys())
        patch = sorted(sample(range(22), patch_size), key=int)

        for column in patch:
            change = 0
            for row in range(rows_encoder.__len__()):
                if self.solution_matrix[row, column] != 0:
                    change += keys[row]*self.solution_matrix[row, column]
                    self.solution_matrix[row, column] = 0

            if change < 499:
                self.calculate_for_every_divided_change(change, available_coins)
            else:
                adjusted_change = break_the_rest_to_exchange(change)
                for ch in adjusted_change:
                    self.calculate_for_every_divided_change(ch, available_coins)

    def search_food_with_patch_size_by_selecting_random_cells(self, available_coins, patch_size):
        keys = list(rows_encoder.keys())
        columns = sorted(sample(range(22), patch_size), key=int)
        rows = sorted(sample(range(8), patch_size), key=int)
        change = 0
        for index in range(patch_size):
            change += keys[rows[index]] * self.solution_matrix[rows[index], columns[index]]
            self.solution_matrix[rows[index], columns[index]] = 0

        if change < 499:
            self.calculate_for_every_divided_change(change, available_coins)
        else:
            adjusted_change = break_the_rest_to_exchange(change)
            for ch in adjusted_change:
                self.calculate_for_every_divided_change(ch, available_coins)

    def search_food_with_patch_size_by_intelligent_column(self, available_coins, patch_size, coins_to_save):
        rows = []
        for element in coins_to_save:
            rows.append(rows_encoder[element])
        patch = []
        coins_to_change_ranking = []

        for col in range(np.shape(self.solution_matrix)[1]):
            change = 0
            iterator = 0
            for row in rows:
                change += coins_to_save[iterator] * self.solution_matrix[row, col]
                iterator += 1
            coins_to_change_ranking.append(change)
        column_indexes_to_save = np.argsort(coins_to_change_ranking)[-patch_size:]

        patch = sorted(column_indexes_to_save)

        keys = list(rows_encoder.keys())
        money_to_change = 0
        for column in patch:
            for row in range(rows_encoder.__len__()):
                if self.solution_matrix[row, column] != 0:
                    money_to_change = money_to_change + keys[row]*self.solution_matrix[row, column]
                    self.solution_matrix[row, column] = 0
        if money_to_change < 499:
            self.calculate_for_every_divided_change(money_to_change, available_coins)
        else:
            adjusted_change = break_the_rest_to_exchange(money_to_change)
            sum = np.sum(adjusted_change)
            for ch in adjusted_change:
                self.calculate_for_every_divided_change(ch, available_coins)

    def search_food_with_patch_size_by_selecting_intelligent_cells(self, available_coins, patch_size, coins_to_save):
        keys = list(rows_encoder.keys())
        sum_rows = []
        for i in range(len(coins_to_save)):
            sum_rows.append(sum(self.solution_matrix[rows_encoder[coins_to_save[i]]])*coins_to_save[i])
        best_rows = []
        sorted_rows = sorted(sum_rows)
        sorted_rows.reverse()
        for i in range(patch_size):
            if i <= patch_size:
                best_rows.append(sum_rows[i])

        rows = []
        for i in range(patch_size):
                max_val = max(sorted_rows)
                index = sum_rows.index(max_val)
                rows.append(index)
                sorted_rows.remove(max_val)
        cols = [np.random.randint(7) + 15 for i in range(patch_size)]

        change = 0
        for index in range(patch_size):
            change += keys[rows[index]] * self.solution_matrix[rows[index], cols[index]]
            self.solution_matrix[rows[index], cols[index]] = 0

        if change < 499:
            self.calculate_for_every_divided_change(change, available_coins)
        else:
            adjusted_change = break_the_rest_to_exchange(change)
            for ch in adjusted_change:
                self.calculate_for_every_divided_change(ch, available_coins)

    def calculate_for_every_divided_change(self, change, available_coins):
        divided_change = [get_digit(change, 2) * 100,
                          get_digit(change, 1) * 10,
                          get_digit(change, 0)]
        adjusted_available_coins = list(filter(lambda x: x < 10 ** len(str(change)), available_coins))
        for value in divided_change:
            self.divide_value(value, adjusted_available_coins)

    def set_to_be_onlooker(self):
        self.bee_type = BeeType.Onlooker
        pass

    def reload_solution_matrix(self):
        self.solution_matrix.fill(0)

    def calc_solution(self):
        self.solution=np.sum(self.solution_matrix)

    def print_cost(self):
        print('Bee cost: ' + str(self.cost))

    def print_solution(self):
        print('Solution: \n' + str(self.solution_matrix))


def break_the_rest_to_exchange(value):
    exchange_list =[np.random.randint(499)]
    while sum(exchange_list) != value:
        max_val = 499 if value - sum(exchange_list) > 499 else value - sum(exchange_list)
        generated_value = np.random.randint(max_val+1)
        exchange_list.append(generated_value)

    return exchange_list


def get_digit(number, n):
    return number // 10 ** n % 10


class BeeType:
    Scout = "Scout";
    Onlooker = "Onlooker";