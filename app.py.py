import streamlit as st

def main():
    st.title("Square Calculator")
    
    # User input for number
    number = st.number_input("Enter a number:")
    
    # Calculate square
    square = number ** 2
    
    # Display square
    st.write(f"The square of {number} is: {square}")

if __name__ == "__main__":
    main()
