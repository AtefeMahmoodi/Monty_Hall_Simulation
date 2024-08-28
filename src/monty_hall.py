import random

def monty_hall(switch_choice):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    
    selected_door = random.choice(range(3))

    if switch_choice:
        remained_doors = [i for i in range(3) if i != selected_door and doors[i] == 'goat'] 
        revealed_door = random.choice(remained_doors)
        final_choice = [i for i in range(3) if i != selected_door and i != revealed_door][0]
    else:
        final_choice = selected_door

    return doors[final_choice] == 'car'


def monty_hall_simulation(number_of_games):
    switch_win_rate = 0
    not_switch_win_rate = 0
    for _ in range(number_of_games):
        if monty_hall(True):
            switch_win_rate += 1
        if monty_hall(False):
            not_switch_win_rate += 1

    return switch_win_rate, not_switch_win_rate

if __name__ == '__main__':
    switch_win_rate, not_switch_win_rate = monty_hall_simulation(100000)
    print(switch_win_rate, not_switch_win_rate)