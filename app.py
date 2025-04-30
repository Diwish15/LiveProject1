import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("My First Streamlit App")

# Sidebar input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name:")
slider_val = st.sidebar.slider("Pick a number", 1, 100, 50)

# Display user input
st.write(f"Hello, {user_name}! 👋")
st.write(f"You picked the number {slider_val}.")

# Generate some data
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum() + slider_val
})

# Show the chart
st.line_chart(data.set_index('x'))

# Additional info
st.info("This is a simple interactive Streamlit demo.")
