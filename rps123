import streamlit as st

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        st.write(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            st.write("Rock smashes scissors! You win!")
        else:
            st.write("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            st.write("Paper covers rock! You win!")
        else:
            st.write("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            st.write("Scissors cuts paper! You win!")
        else:
            st.write("Rock smashes scissors! You lose.")
