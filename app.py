import streamlit as st
import pandas as pd


st.title('Quadratic Regression')
st.write('This is a simple example of a quadratic regression model using Streamlit.')


coords = {'x': [0,0,0,], 'y': [0,0,0]}

# Code to get the values of x and y from the user
_ = '''
coords2 = []
for i in range(3):
    x = int(input('Enter x value: '))
    y = int(input('Enter y value: '))
    coords2.append([x, y])

for coord in coords:
    coords['x'].append(coord[0])
    coords['y'].append(coord[1])

f = pd.read_csv('values.csv')
d = pd.DataFrame(coords)
st.dataframe(d)'''


df = pd.DataFrame(coords) # pd.read_csv('values.csv')
edited_df = st.data_editor(df)

st.scatter_chart(edited_df)