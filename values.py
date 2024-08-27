# df = dataframe

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Title for pages in the sidebar
def display() -> None:
    st.title("Values")


# Choose whether to upload or edit the DataFrame
def choose() -> int:
    choice = st.selectbox("Choose an option", ["Upload a CSV", "Edit the DataFrame"])
    if choice == "Upload a CSV":
        return 1
    elif choice == "Edit the DataFrame":
        return 2


# Create the base DataFrame
def starter_table() -> pd.DataFrame:
    df = pd.DataFrame({'X': [1,2,3], 'Y': [2,10,4]}, columns=["X", "Y"])
    df = st.data_editor(df)
    return df


# Upload a CSV file, print table, and return the DataFrame
def upload_file() -> tuple[list[float], list[float]]:
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    try:
        df = pd.read_csv(file)
        df = st.data_editor(df)
        x_points, y_points = df['X'].tolist(), df['Y'].tolist()
        return x_points, y_points
    except:
        st.write("Please load a file to continue...")
        return [], []


# Display the chart
def display_chart(x: list[float], y: list[float]) -> None:
    plt.plot(x, y, 'ob')
    st.pyplot(plt)


#! Not implemented
# Adds a row to the uploaded DataFrame/table
def add_row():
    ...



display()
choice = choose()       

if choice == 2:
    starter_table()
    st.markdown('### Test Table')
    display_chart([1,2,3], [2,10,4])
else:
    x_points, y_points = upload_file()
    if x_points and y_points:
        st.markdown('### Uploaded Chart')
        display_chart(x_points, y_points)