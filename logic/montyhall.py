import random

def goat_reveals(N: int, revealed: set, player_choice: int, prize_position: int):
    all_doors = set(range(N))
    forbidden = {player_choice, prize_position} | revealed
    candidates = list(all_doors - forbidden)
    return random.choice(candidates)


def apply_strategy(strategy, N, player_choice, revealed):
    all_doors = set(range(N))

    # Doors the player could switch to
    options = list(all_doors - revealed - {player_choice})
    
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


def play_once(N, K, strategy, switch):
    # Set doors
    prize_door = random.randint(0, N - 1)
    player_choice = random.randint(0, N - 1)
    player_choices = [player_choice]
    revealed_doors = []
    final_choice = player_choice

    # Reveal goats
    revealed_set = set()
    for i in range(K):
        reveal_one = goat_reveals(N, revealed_set, final_choice, prize_door)
        revealed_doors.append(reveal_one)
        revealed_set.add(reveal_one)
        
        if switch:
            final_choice = apply_strategy(strategy, N, final_choice, revealed_set)
            player_choices.append(final_choice)

    if not switch:
        final_choice = apply_strategy(strategy, N, player_choice, revealed_set)

    return {
            'Prize door': prize_door,
            'Player choice': player_choices,
            'Revealed': revealed_doors,
            'Final choice': final_choice,
            'win': final_choice == prize_door
        }
