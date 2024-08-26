import streamlit as st
import pandas as pd

import values, calculation


st.title('Quadratic Regression')
st.write('This is a simple application of a quadratic regression model.')












# Create a dictionary of pages
pages = {
    "Values": values.display,
    "Chart": calculation.display,
}

# Render the page selection as a radio button
page = st.sidebar.radio("Choose a page", tuple(pages.keys()))

# Display the selected page with the help of the dictionary
pages[page]()




_ = '''

coords = {'x': [1,2,3,], 'y': [2,10,4]}

# Code to get the values of x and y from the user
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
st.dataframe(d)



df = pd.DataFrame(coords, columns=['X', 'Y']) # pd.read_csv('values.csv')
df.loc[0] = [1, 2]
df.loc[1] = [2, 10]
df.loc[2] = [3, 4]
edited_df = st.data_editor(df)


st.scatter_chart(edited_df, x_label='X', y_label='Y')

'''