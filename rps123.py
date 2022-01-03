import streamlit as st
import random

user_action = st.text_input('Enter a choice, (rock, paper, scissors):', '')

confirm_input = st.button('輸入確認')
if confirm_input:
    
    
    
    
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    st.write('Player choice is', user_action)  
   
    if user_action == computer_action:
        st.write(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            st.write("Computer choice scissor,Rock smashes scissors! You win!")
        else:
            st.write("Computer choice scissor,Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            st.write("Computer choice rock,Paper covers rock! You win!")
        else:
            st.write("Computer choice rock,Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            st.write("Computer choice paper,Scissors cuts paper! You win!")
        else:
            st.write("Computer choice paper,Rock smashes scissors! You lose.")
                
