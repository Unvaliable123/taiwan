import streamlit as st
import random

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

'''
while True:
    user_action = st.text_input("Enter a choice, (rock, paper, scissors):" )
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        st.write(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            st.write("Rock smashes scissors! You win!")
        else:
            st.write("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            st.write("Paper covers rock! You win!")
        else:
            st.write("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            st.write("Scissors cuts paper! You win!")
        else:
            st.write("Rock smashes scissors! You lose.")
'''