# df = dataframe
import streamlit as st
import pandas as pd
import plotly.express as px


st.session_state = {}       # Initialize the session state dictionary

# Title for pages in the sidebar
def display() -> None:
    st.title("Values")


# Decide the degree of the polynomial
def degree() -> int:
    st.markdown("#### What power do you want to use for the curve?")
    degree = st.text_input('Degree:')
    if degree < '2': 
        st.markdown("#### Please enter a natural number >2...")
        return 0
    try:
        degree = int(degree)
        st.session_state['Degree'] = int(degree)
        return degree
    except:
        st.write("#### Please enter a valid natural number >2...")
        return 0
    

# Add variables to the session state dictionary
def session_state(var, name='str(var)') -> None:
    st.session_state[name] = var
    

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
    session_state(df['X'].tolist(), 'X_Points')
    session_state(df['Y'].tolist(), 'Y_Points')
    return df


# Upload a CSV file, print table, and return the DataFrame
def upload_file() -> tuple[list[float], list[float]]:
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    try:
        df = pd.read_csv(file)
        df = st.data_editor(df)
        x_points, y_points = df['X'].tolist(), df['Y'].tolist()
        session_state(x_points, 'X_Points')              # Add x_points to the session state
        session_state(y_points, 'Y_Points')              # Add y_points to the session state
        return x_points, y_points
    except:
        st.write("Please load a file to continue...")
        return [], []


# Display the chart
def display_chart(x: list[float], y: list[float]) -> None:
    g = px.scatter(x=x, y=y)
    st.plotly_chart(g, use_container_width=True)


display()
degree()
st.write("")
st.write("")
choice = choose()

if choice == 2:
    starter_table()
    st.markdown('### Test Table')
    display_chart([1,2,3], [2,10,4])
else:
    x_points, y_points = upload_file()
    # display session state
    if x_points and y_points:
        st.markdown('### Uploaded Chart')
        display_chart(x_points, y_points)

st.write('\n')
st.write('\n')
st.write('\n')
st.page_link(page="pages/_2_graph.py", label="**Graph**", help="Display the scatter plot and regression curve.")
