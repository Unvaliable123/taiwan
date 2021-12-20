import streamlit as st
import random

while True:
    user_action = st.text_input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    st.write(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

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

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
