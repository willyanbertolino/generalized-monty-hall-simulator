import random

def goat_reveals(N, K, player_choice, prize_position):
    # Define which doors are available to reveal goats
    all_doors = set(range(N))
    forbidden = {player_choice, prize_position}

    candidates = list(all_doors - forbidden)

    # Reveal K random doors (goats)
    opened_doors = set(random.sample(candidates, K))
    return opened_doors


def apply_strategy(strategy, N, player_choice, opened_doors):
    all_doors = set(range(N))

    # Doors the player could switch to
    options = list(all_doors - opened_doors - {player_choice})
    
    # STRATEGY:
    # always stay
    if strategy == "stay":
        return player_choice

    # always switch
    elif strategy == "switch":
        return random.choice(options)

    # random stay/switch
    elif strategy == "random":
        if random.random() < 0.5:
            return player_choice
        else:
            return random.choice(options)

    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def play_once(N, K, strategy):
    # Set doors
    prize_door = random.randint(0, N - 1)
    player_choice = random.randint(0, N - 1)

    # Reveal goats
    opened_doors = goat_reveals(N, K, player_choice, prize_door)

    final_choice = apply_strategy(strategy, N, player_choice, opened_doors)
    return {
            'Prize door': prize_door,
            'Initial choice': player_choice,
            'Revealed': list(opened_doors),
            'Final choice': final_choice,
            'win': final_choice == prize_door
        }
