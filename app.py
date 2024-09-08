import streamlit as st


st.set_page_config(page_title="Quadratic Regression", 
                   page_icon=":bar_chart:",
                   layout="centered")


st.markdown("# Quadratic Regression")
st.markdown(
        """
        ##### This is a simple application of a quadratic regression model.
        You can upload a CSV file or edit an example DataFrame directly.  
        **Click the Values tab to proceed!**
        
        - Values tab: Upload a CSV file or edit the DataFrame.
        - Graph tab: Display the scatter plot and regression curve.
        - Calculation tab: Does the calculation for the graph & explains the calculation.
""")


st.write('\n')
st.write('\n')
st.write('\n')
st.page_link(page="pages/_1_values.py", label="**Values**", help="Upload a CSV file or edit the DataFrame.")
