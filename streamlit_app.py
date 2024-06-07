# streamlit_app.py

import streamlit as st
from game_logic import (
    counterfeit_coin_game,
    devilish_divisibility_game,
    combined_game_simulation,
    alternating_game_simulation
)

def run_simulations(initial_amount, num_rounds):
    st.write("Starting simulations with initial amount:", initial_amount)
    st.write("Number of rounds:", num_rounds)
    
    counterfeit_result, counterfeit_rounds = counterfeit_coin_game(initial_amount, num_rounds)
    if counterfeit_result == 0:
        st.write(f"Counterfeit Coin Game: Lost all money at round {counterfeit_rounds}")
    else:
        st.write(f"Counterfeit Coin Game Result: ${counterfeit_result} after {counterfeit_rounds} rounds")
    
    devilish_result, devilish_rounds = devilish_divisibility_game(initial_amount, num_rounds)
    if devilish_result == 0:
        st.write(f"Devilish Divisibility Game: Lost all money at round {devilish_rounds}")
    else:
        st.write(f"Devilish Divisibility Game Result: ${devilish_result} after {devilish_rounds} rounds")
    
    combined_result, combined_rounds = combined_game_simulation(initial_amount, num_rounds)
    if combined_result == 0:
        st.write(f"Combined Game Simulation: Lost all money at round {combined_rounds}")
    else:
        st.write(f"Combined Game Simulation Result: ${combined_result} after {combined_rounds} rounds")
    
    alternating_result, alternating_rounds = alternating_game_simulation(initial_amount, num_rounds)
    if alternating_result == 0:
        st.write(f"Alternating Game Simulation: Lost all money at round {alternating_rounds}")
    else:
        st.write(f"Alternating Game Simulation Result: ${alternating_result} after {alternating_rounds} rounds")

st.title("Perando's Paradox Simulation")
st.write("Each game is played with $1. counterfeit coin has a 49% chance of winning while devilish divisibilty has a 9.5% or 74.5% depending on the amount being divisible by 3. Both games lose over time. The combined simulation plays CC once then DD twice and repeats this pattern. Alternating is 1 and 1 continually.")

initial_amount = st.number_input("Initial Amount", min_value=1, value=100)
num_rounds = st.number_input("Number of Rounds", min_value=1, value=100000)

if st.button("Simulate"):
    run_simulations(initial_amount, num_rounds)