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
            st.write("Computer choice scissor,rock smashes scissors! You win!")
            st.title('🗿>✂ 😎')
        else:
            st.write("Computer choice paper,paper covers rock! You lose.")
            st.title('🗿<📄 😩')
    elif user_action == "paper":
        if computer_action == "rock":
            st.write("Computer choice rock,paper covers rock! You win!")
            st.title('📄>🗿 😎')
        else:
            st.write("Computer choice scissors,scissors cuts paper! You lose.")
            st.title('📄<✂ 😩')
    elif user_action == "scissors":
        if computer_action == "paper":
            st.write("Computer choice paper,scissors cuts paper! You win!")
            st.title('✂>📄 😎')
        else:
            st.write("Computer choice rock,rock smashes scissors! You lose.")
            st.title('✂<🗿 😩')
                
