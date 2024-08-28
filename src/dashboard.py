import streamlit as st
from src.monty_hall import monty_hall_simulation
import time


st.image("https://th.bing.com/th/id/OIP.whAZ0uMuM_HjlG8qj8T4LQHaES?rs=1&pid=ImgDetMain", width=400)
st.title("Monty Hall Simulation")
num_of_games = st.number_input("Enter the number of games you want to simulate:", min_value=1, max_value=100000, value=100)

col1, col2= st.columns(2)

col1.subheader("Win percentage with switching")
col2.subheader("Win percentage without switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)


wins_with_switch = 0
wins_without_switch = 0
for i in range(num_of_games):
    num_wins_with_switch, num_wins_without_switch = monty_hall_simulation(1)
    wins_with_switch += num_wins_with_switch
    wins_without_switch += num_wins_without_switch

    chart1.add_rows([wins_with_switch / (i + 1)])
    chart2.add_rows([wins_without_switch / (i + 1)])
    time.sleep(0.01)