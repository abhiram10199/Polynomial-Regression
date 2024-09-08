import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pages._1_values as values
import pages._3_calculation as calc


# Title for page in the sidebar
def display() -> None:
    st.title('Graph')


# Retrieves the values from session state
def retrieve_values() -> tuple:
    X_Points = st.session_state['X_Points']
    Y_Points = st.session_state['Y_Points']
    degree = st.session_state['Degree']
    return X_Points, Y_Points, degree


# Retrieves the values from session state and returns the coefficients
def find_coefficients(X_Points, Y_Points) -> np.ndarray:
    X_Matrix, X_Transpose, Y_Transpose = calc.creating_matrices(X_Points, Y_Points)
    A = calc.calculate_coefficients(X_Matrix, X_Transpose, Y_Points)
    values.session_state(A.tolist(), 'Coefficient_Matrix')
    return A


# Finds the points along the regression curve
def regression_curve_values(X_Points, Coefficient_Matrix, degree=2+1) -> tuple:
    x_range = np.linspace(X_Points[0], X_Points[-1], 100)
    y_range = np.empty(100)
    y_range[:] = 0
    for i in range(100):
        for j in range(degree):
            y_range[i] += Coefficient_Matrix[j] * x_range[i] ** j

    return x_range, y_range


# Plots the graph
def plotter(X_Points, Y_Points, xy_range) -> None:
    x_range, y_range = xy_range

    data_points = go.Scatter(
        x=X_Points,
        y=Y_Points, 
        name="Data Points", 
        mode='markers',
        fillcolor='blue')
        
    regression_curve = go.Scatter(
        x=x_range,
        y=y_range,
        name="Regression Curve",
        mode='lines',
        fillcolor='red',
        line=dict(color='red', width=2))
    
    fig = go.Figure(data=[data_points])
    fig.add_trace(regression_curve)
    fig.update_layout(title='Regression Curve', xaxis_title='X', yaxis_title='Y', showlegend=True)
                      
    st.plotly_chart(fig)



display()
X_Points, Y_Points, degree = retrieve_values()

try:
    Coefficient_Matrix = find_coefficients(X_Points, Y_Points)
except KeyError:
    st.error("You haven't uploaded a CSV file yet. \
             Please upload a CSV file in the Values tab")

plotter(X_Points, Y_Points, regression_curve_values(X_Points, Coefficient_Matrix))

st.markdown("If the Values page ghosted and appears along with graph, reclick on graph in the sidebar!")
st.write('\n')
st.write('\n')
st.write('\n')
st.page_link(page="pages/_1_values.py", label="**Values**", help="Upload a CSV file or edit the DataFrame.")
