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

st.title("🚪 Generalized Monty Hall Problem — Simulator")
st.write("""
Explore how the probabilities behave when extending the classic Monty Hall problem
to **N doors**, with **K opened by the host**, and customizable **player strategies**.
""")


# Sidebar
st.sidebar.header("Simulation Parameters")

N = st.sidebar.number_input("Number of doors (N)", min_value=3, max_value=100, value=3)

K = st.sidebar.number_input("Number of doors opened by the host (K)", min_value=1, max_value=N-2, value=1)

strategy = st.sidebar.selectbox(
    "Player Strategy",
    ["stay", "switch", "random"]
)

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
        result = run_simulation(N, K, strategy, n_sim)

    st.success("Simulation completed!")

    win_rate = result["win_rate"]
    st.subheader("Results")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.metric(label="Win Rate", value=f"{win_rate:.2%}")

        # bayes table
        st.write("Bayes table in case 1")
        st.dataframe(result["bayes_table"])



    with col2:
        st.subheader("Raw Results")
        st.dataframe(result["dataframe"])

        # Show raw data table


# Strategy comparison
st.divider()
st.header("Compare Strategies")

compare_button = st.button("Run Strategy Comparison")

if compare_button:

    with st.spinner("Simulating all strategies..."):
        comp_df = compare_strategies(N, K, n_sim)

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

