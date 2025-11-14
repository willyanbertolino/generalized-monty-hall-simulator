import pandas as pd
from logic.montyhall import play_once


def run_simulation(N: int, K: int, strategy: str, n_sim: int):
    results = []

    for _ in range(n_sim):
        play = play_once(N, K, strategy)
        results.append(play)

    df = pd.DataFrame(results)
    win_rate = df["win"].mean()

    first_sim = df.iloc[0]
    bayes_df = bayes_table(N, first_sim)

    return {
        "win_rate": win_rate,
        "dataframe": df,
        "bayes_table": bayes_df
    }

def bayes_table(N, sim):
    df = pd.DataFrame(index=[f'Door {i+1}' for i in range(N)])
    df['prior'] = 1/N

    prize_door = sim['Prize door']
    revealed_doors = sim['Revealed']
    initial_door = sim['Initial choice']

    l = list(range(N))

    if prize_door == initial_door:
        # all door can be opened
        l[prize_door] = 1/(N-1)
    else:
        l[prize_door] = 0
        for i in revealed_doors:
            l[i] = 1

    df['likelihood'] = l
    return df

def compare_strategies(N: int, K: int, n_sim: int):
    strategies = ["stay", "switch", "random"]
    data = []

    for s in strategies:
        result = run_simulation(N, K, s, n_sim)
        data.append({
            "strategy": s,
            "win_rate": result["win_rate"]
        })

    return pd.DataFrame(data)
