import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Title for pages in the sidebar
def display():
    st.title("Values")

# Create the base DataFrame
def starter() -> pd.DataFrame:
    df = pd.DataFrame({'X': [1,2,3], 'Y': [2,10,4]}, columns=["X", "Y"])
    df = st.data_editor(df)
    return df

# Choose whether to upload or edit the DataFrame
def choose():
    choice = st.selectbox("Choose an option", ["Upload a CSV", "Edit the DataFrame"])
    if choice == "Upload a CSV":
        uploaded_file = st.file_uploader("Choose a file")
    elif choice == "Edit the DataFrame":
        df = starter()
    return choice


# Display the chart
def chart():
    x = [1,2,3]
    y = [2,10,4]
    plt.plot(x, y, 'ob')
    st.pyplot(plt)


display()
choose()
st.title('Chart')
chart()