import pandas as pd
from logic.montyhall import play_once


def run_simulation(N: int, K: int, strategy: str, n_sim: int, switch: bool):
    results = []

    # Simulate
    for _ in range(n_sim):
        play = play_once(N, K, strategy, switch)
        results.append(play)

    df = pd.DataFrame(results)
    win_rate = df["win"].mean()

    # Construct the Bayes table for the first simulation
    first_sim = df.iloc[0]
    bayes_df = bayes_table(N, first_sim)

    return {
        "win_rate": win_rate,
        "dataframe": df,
        "bayes_table": bayes_df
    }

def bayes_table(N: int, sim):
    df = pd.DataFrame(index=[f'Door {i+1}' for i in range(N)])
    df['prior'] = 1/N

    prize_door = sim['Prize door']
    revealed_doors = sim['Revealed']
    initial_door = sim['Player choice'][0]

    # Calculate the likelihood
    l = [None] * N
    for i in range(N):
        if i in revealed_doors:
            l[i] = 0
            df.loc[f'Door {i+1}', 'Decision'] = 'Opened'

        elif i == initial_door:
            l[i] = 1/(N-1)
            df.loc[f'Door {i+1}', 'Decision'] = 'Stay'

        else:
            l[i] = 1/(N - len(revealed_doors) - 1)
            df.loc[f'Door {i+1}', 'Decision'] = 'Switch'

    df['likelihood'] = l

    df['unnorm'] = df['likelihood'] * df['prior']
    un_total = df['unnorm'].sum()
    df['posterior'] = df['unnorm']/un_total
    df['Decision'] = df.pop('Decision')
    return df

def compare_strategies(N: int, K: int, n_sim: int, switch:bool):
    strategies = ["stay", "switch", "random"]
    data = []

    # Simulate for all strategies
    for s in strategies:
        result = run_simulation(N, K, s, n_sim, switch)
        data.append({
            "strategy": s,
            "win_rate": result["win_rate"]
        })

    return pd.DataFrame(data)
