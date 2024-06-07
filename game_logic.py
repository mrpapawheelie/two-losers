# game_logic.py

import random

def counterfeit_coin_game(initial_amount, num_rounds):
    amount = initial_amount
    for i in range(num_rounds):
        if random.random() < 0.49:  # 49% win rate
            amount += 1
        else:
            amount -= 1
        if amount <= 0:
            return 0, i + 1
    return amount, num_rounds

def devilish_divisibility_game(initial_amount, num_rounds):
    amount = initial_amount
    for i in range(num_rounds):
        if amount % 3 == 0:
            if random.random() < 0.095:  # 9.5% win rate
                amount += 1
            else:
                amount -= 1
        else:
            if random.random() < 0.745:  # 74.5% win rate
                amount += 1
            else:
                amount -= 1
        if amount <= 0:
            return 0, i + 1
    return amount, num_rounds

def combined_game_simulation(initial_amount, num_rounds):
    amount = initial_amount
    for i in range(num_rounds):
        if i % 3 == 0:  # C-DD-C-DD pattern
            amount, _ = counterfeit_coin_game(amount, 1)
        else:
            amount, _ = devilish_divisibility_game(amount, 1)
        if amount <= 0:
            return 0, i + 1
    return amount, num_rounds

def alternating_game_simulation(initial_amount, num_rounds):
    amount = initial_amount
    for i in range(num_rounds):
        if i % 2 == 0:  # Alternating pattern
            amount, _ = counterfeit_coin_game(amount, 1)
        else:
            amount, _ = devilish_divisibility_game(amount, 1)
        if amount <= 0:
            return 0, i + 1
    return amount, num_rounds