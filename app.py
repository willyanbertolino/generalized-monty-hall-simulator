import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from simulation import run_simulation, compare_strategies

# pages
st.set_page_config(
    page_title="Generalized Monty Hall Simulator",
    page_icon="🚪",
    layout="wide"
)

st.title("Generalized Monty Hall Problem — Simulator 🚪🚪🚪")

with st.expander("About This Simulation"):
    st.markdown("""
    This application explores the **generalized Monty Hall problem**, a probability
    puzzle where a player chooses one door among many, the host reveals doors
    without the prize, and the player may reconsider their choice.

    Unlike the classic version with **3 doors and 1 revealed door**, real-world
    scenarios often involve:

    - **Many doors** (N > 3)  
    - **Several doors revealed by the host** (K ≥ 1)  
    - **Different player strategies**, such as staying, switching once,
      switching after each reveal, or making a random choice.

    Because probabilities become more complex as **N** and **K** grow,
    analytical formulas are not always simple or practical.
    This is where simulation becomes a powerful tool.
    """)

with st.expander("When is this simulation useful?"):
    st.markdown("""
    You can use this simulation when:

    - Comparing decision strategies under uncertainty  
    - Understanding how partial information affects probabilities  
    - Teaching probability or Bayesian reasoning  
    - Extending Monty Hall logic to more complex real-world situations  
    - Illustrating how simulation approximates theoretical probabilities  

    This app helps visualize how winning chances change as **N**, **K**,
    and the player’s strategy vary.
    """)



# Sidebar
st.sidebar.header("Simulation Parameters")

N = st.sidebar.number_input("Number of doors (N)", min_value=3, max_value=100, value=3)

K = st.sidebar.number_input("Number of doors opened by the host (K)", min_value=1, max_value=N-2, value=1)

strategy = st.sidebar.selectbox(
    "Player Strategy",
    ["stay", "switch", "random"]
)

switch = False

if strategy == "switch" and K > 1:
    switch = st.sidebar.checkbox("Switch strategy", value=False)

    if switch:
        st.sidebar.write("**Switch after each revealed door.**")
    else:
        st.sidebar.write("**Reveal all goats first, then switch.**")


n_sim = st.sidebar.number_input(
    "Number of simulations",
    min_value=100,
    max_value=500_000,
    value=10_000,
    step=1000
)


run_button = st.sidebar.button("Run Simulation")


# Run simulation
if run_button:

    with st.spinner("Running simulation..."):
        result = run_simulation(N, K, strategy, n_sim, switch)

    st.success("Simulation completed!")

    win_rate = result["win_rate"]
    st.subheader("Results")

    col1, col2, col3 = st.columns([1.2, 0.1, 0.8])

    with col1:
        st.metric(label="Win Rate - Simulation Result", value=f"{win_rate:.2%}")

        if switch:
            st.write("""
                ### About the General Formula

                The probability for the strategy **“switch after each reveal”** does *not* have a simple closed-form 
                expression for general values of \(N\) and \(K\).

                This happens because the outcome depends on **all possible sequences** of doors the host might reveal, 
                and each sequence has its own probability. Computing the final win probability requires applying the 
                **full law of total probability** over these sequences, which becomes combinatorially complex. 
                """)

            st.page_link("pages/explanation.py", label="See more")

            st.write("""
                For this reason, the analytical formula goes beyond the scope of this app.  
                Instead, the win rate shown here is obtained through **simulation**, which accurately 
                approximates the true probability even in complex scenarios.
                """)

        else:
            # bayes table
            st.write("Bayes Table for the First Simulation — Numerical Results")
            st.dataframe(result["bayes_table"])



    with col3:
        st.subheader("Raw Results")
        st.dataframe(result["dataframe"])

        # Show raw data table


    # Strategy comparison
    st.divider()
    st.header("Compare Strategies")



    with st.spinner("Simulating all strategies..."):
        comp_df = compare_strategies(N, K, n_sim, switch)

    st.success("Comparison completed!")

    col1, spacer, col2 = st.columns([1,0.2, 1])

    with col1:
        st.write("### Win rates for multiple strategies")
        st.dataframe(comp_df)
    
    with col2:
        # Plot comparison
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        ax2.bar(comp_df["strategy"], comp_df["win_rate"], width=0.6)
        ax2.set_ylim(0, 1)
        ax2.set_xticklabels(comp_df["strategy"], rotation=30)
        st.pyplot(fig2)

