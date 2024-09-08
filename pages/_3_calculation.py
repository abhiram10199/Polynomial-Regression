import streamlit as st
import numpy as np
from numpy.linalg import inv


# Title for pages in the sidebar
def display() -> None:
    st.title("Calculation")


# Creates the matrices for the calculation + transposes them
def creating_matrices(x_coords: list[float], y_coords: list[float], degree=2):
    # X is a matrix of size 'n x Degree'
    X = np.empty((len(x_coords), degree+1))

    for i, row in enumerate(X):
        for j in range(degree+1):
            X[i][j] = x_coords[i] ** j
    
    # Y is in row form, yT to coloumn form
    X_transpose, Y_transpose = np.transpose(X), np.transpose(y_coords)
    
    return X, X_transpose, Y_transpose


# Calculates the coefficients of the polynomial
def calculate_coefficients(X, X_transpose, y_coords):
    try:
        # A = (X^T * X)^-1 * X^T * Y = ((X^T * X)^-1 * X^T) * yT
        A = np.dot(np.dot(inv(np.dot(X_transpose, X)), X_transpose), np.transpose(y_coords))
        return A
    except np.linalg.LinAlgError:
        print("ERROR: Matrix is not invertible")
        return


# Display the explanation of the calculation
def explanation():
    st.write("A quadratic regression model won't always be the best fit for the data, but it's a good starting point.")
    st.write("Changing the degree of the polynomial will change the shape of the curve. Sometimes better fitting the data points.")
    st.write("Although overfitting can occur if the degree is too high, leading to a less accurate model.")

    st.write("Using matricies to calculate the coefficients of the polynomial is a more efficient method than using the normal equations.")
    st.write("Given 3 data points, the matrices for a quadratic calculation would be:")
    x_matrix = (r'''
                \begin{bmatrix}
                1 & x_1 & x_1^2 \\
                1 & x_2 & x_2^2 \\
                1 & x_3 & x_3^2 \\
                    \end{bmatrix}
                ''')
    a_matrix = (r'''
                \begin{bmatrix}
                a_0 \\
                a_1 \\
                a_2 \\
                    \end{bmatrix}
                ''')
    y_matrix = (r'''
                \begin{bmatrix}
                y_1 \\
                y_2 \\
                y_3 \\
                    \end{bmatrix}
                ''')
    st.latex(f"{x_matrix} * {a_matrix} = {y_matrix}")

    st.write("This would be scaled up for higher degrees. Eg: A cubic regression would be:")
    x_matrix = (r'''
                \begin{bmatrix}
                1 & x_1 & x_1^2 & x_1^3 \\
                1 & x_2 & x_2^2 & x_2^3 \\
                1 & x_3 & x_3^2 & x_3^3 \\
                    \end{bmatrix}
                ''')
    a_matrix = (r'''
                \begin{bmatrix}
                a_0 \\
                a_1 \\
                a_2 \\
                a_3 \\
                    \end{bmatrix}
                ''')
    y_matrix = (r'''
                \begin{bmatrix}
                y_1 \\
                y_2 \\
                y_3 \\
                    \end{bmatrix}
                ''')
    st.latex(f"{x_matrix} * {a_matrix} = {y_matrix}")

    st.write("The coefficients are calculated by rewriting the normal equation:")
    st.latex(r"X * A * X^T = Y * X^T"); st.write("To - ")
    st.latex(r"A = (X^T * X)^{-1} * X^T * Y")

    st.write("The regression curve is calculated by using the coefficients and the x values of the data points.")
    st.write("This is a simple explanation of the calculation behind the quadratic regression model.")


display()
explanation()
