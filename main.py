import streamlit as st
import random

# Initialize session state to store inputs and clear the input field
if "elements" not in st.session_state:
    st.session_state.elements = []
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

st.title("Infinite Input Collector and Random Shuffler")

# Function to handle adding input to the list
def add_to_list():
    if st.session_state.input_value:  # Ensure there's something to add
        st.session_state.elements.append(st.session_state.input_value)
        st.session_state.input_value = ""  # Clear the input field

# Text input field that automatically adds input when pressing Enter
new_value = st.text_input("Enter a value:", key="input_value", on_change=add_to_list)

# Display current list of elements
if st.session_state.elements:
    st.write("Current List:")
    st.write(st.session_state.elements)

# Shuffle the list and display it
if st.button("Shuffle List"):
    if st.session_state.elements:
        random.shuffle(st.session_state.elements)
        st.write("Shuffled List:")
        st.write(st.session_state.elements)
    else:
        st.warning("List is empty! Add some elements first.")

# Clear the list (optional)
if st.button("Clear List"):
    st.session_state.elements = []
    st.success("List cleared!")
